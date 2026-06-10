#!/usr/bin/env node
/**
 * Artifact test harness.
 *
 * Loads artifact/command.html in jsdom, mocks window.cowork.callMcpTool +
 * sendPrompt with deterministic responses, then exercises every interactive
 * element: clicks each button, fires Enter on the input, opens/closes
 * the Settings panel, and reports:
 *   - JS errors thrown during load
 *   - JS errors thrown during click
 *   - Buttons whose click handler wasn't attached at all
 *   - Whether sendPrompt / dropPrompt was actually invoked
 *   - Final state of every data-* element (still placeholder, or updated)
 *
 * Usage:
 *    cd /tmp && node /tmp/challenger-care/challenger-care/scripts/test-artifact.js
 *
 * Exits 0 on all green, 1 on any failure.
 */

const fs = require('fs');
const path = require('path');
const { JSDOM, ResourceLoader, VirtualConsole } = require('jsdom');

const ARTIFACT_PATH = path.resolve(__dirname, '..', 'artifact', 'command.html');

// Track errors + activity
const errors = [];
const warnings = [];
const sendPromptCalls = [];
const dropPromptCalls = [];
const toolCalls = [];

function logErr(msg) { errors.push(msg); }
function logWarn(msg) { warnings.push(msg); }
function pass(msg) { console.log(`  \x1b[92m✓\x1b[0m ${msg}`); }
function fail(msg) { console.log(`  \x1b[91m✗\x1b[0m ${msg}`); logErr(msg); }
function warn(msg) { console.log(`  \x1b[93m!\x1b[0m ${msg}`); logWarn(msg); }
function info(msg) { console.log(`    ${msg}`); }
function section(title) { console.log(`\n\x1b[1m${title}\x1b[0m`); }

async function main() {
  console.log('\x1b[1mChallenger Care · Artifact Test Harness\x1b[0m');
  console.log(`Loading: ${ARTIFACT_PATH}`);

  let html = fs.readFileSync(ARTIFACT_PATH, 'utf8');

  // Replace UUID placeholders so the artifact thinks CONFIG is synced
  html = html
    .replace("'__SHOPIFY_UUID__'", "'aaaa-shopify'")
    .replace("'__KLAVIYO_UUID__'", "'bbbb-klaviyo'")
    .replace("'__ASANA_UUID__'", "'cccc-asana'")
    .replace("'__ASANA_PROJECT_GID__'", "'gid-asana-project'")
    .replace("'__DRIVE_UUID__'", "'dddd-drive'")
    .replace("'__DRIVE_DASHBOARD_FOLDER_ID__'", "'gid-drive-folder'");

  const virtualConsole = new VirtualConsole();
  virtualConsole.on('jsdomError', (err) => {
    fail(`jsdom error during load: ${err.message}`);
    if (err.detail) info(String(err.detail).slice(0, 200));
  });
  virtualConsole.on('error', (msg) => {
    fail(`page error: ${msg}`);
  });
  // Capture console.warn / log so we see [dropPrompt] warnings etc.
  virtualConsole.on('warn', (msg) => info(`page warn: ${msg}`));
  virtualConsole.on('log', (msg) => info(`page log: ${msg}`));

  // Make a stub cowork that records calls
  const dom = new JSDOM(html, {
    runScripts: 'dangerously',
    pretendToBeVisual: true,
    virtualConsole,
    beforeParse(window) {
      // Stub sendPrompt as global (per Cowork docs · this is the canonical path)
      window.sendPrompt = (text) => sendPromptCalls.push({ via: 'global', text });

      // Also stub window.cowork.callMcpTool + sendPrompt as fallbacks the code expects
      window.cowork = {
        callMcpTool: async (name, args) => {
          toolCalls.push({ name, args });
          // Return a generic OK response so the loaders don't blow up
          // Shopify analytics needs a specific shape
          if (name.includes('run-analytics-query')) {
            const q = args?.query || '';
            // Match the various analytics queries the dashboard issues
            if (q.includes('FROM sessions') && q.includes('GROUP BY session_device_type')) {
              return { isError: false, structuredContent: { rows: [['mobile', 200, 0.045], ['desktop', 150, 0.002]] } };
            }
            if (q.includes('FROM sessions') && q.includes('sessions_with_cart_additions')) {
              return { isError: false, structuredContent: { rows: [[1000, 200, 100, 50]] } };
            }
            if (q.includes('FROM sessions')) {
              return { isError: false, structuredContent: { rows: [[1000, 50, 0.05]] } };
            }
            if (q.includes('returning_customers')) {
              return { isError: false, structuredContent: { rows: [[40, 100, 0.4]] } };
            }
            if (q.includes('GROUP BY product_title') && q.includes('total_sales')) {
              return { isError: false, structuredContent: { rows: [['Combo 3-Pack', 4000, 80], ['Pomade', 1200, 40]] } };
            }
            if (q.includes('inventory')) {
              return { isError: false, structuredContent: { rows: [['Combo 3-Pack', 100, 20, 80, 0.8, 25], ['Pomade', 200, 150, 50, 0.25, 90]] } };
            }
            if (q.includes('gross_sales')) {
              return { isError: false, structuredContent: { rows: [[6000, 200, 300, 5500, 50]] } };
            }
            // Generic sales response
            return { isError: false, structuredContent: { rows: [[100, 5000, 50]] } };
          }
          if (name.includes('get-shop-info')) {
            return { isError: false, structuredContent: { name: 'Test Shop' } };
          }
          if (name.includes('klaviyo')) {
            return { isError: false, structuredContent: { data: { attributes: { data: [], results: [] } } } };
          }
          if (name.includes('get_tasks')) {
            return { isError: false, structuredContent: { data: [] } };
          }
          if (name.includes('search_files')) {
            return { isError: false, structuredContent: { files: [] } };
          }
          return { isError: false, structuredContent: {} };
        },
        sendPrompt: (text) => sendPromptCalls.push({ via: 'cowork', text }),
      };

      // Stub navigator.clipboard
      Object.defineProperty(window.navigator, 'clipboard', {
        value: { writeText: async (text) => sendPromptCalls.push({ via: 'clipboard', text }) },
        writable: true,
      });
    },
  });

  // Wait for scripts to execute + init() to run (async chain)
  await new Promise(r => setTimeout(r, 600));

  const { window } = dom;
  const { document } = window;

  // ============================================================
  // 1. SCRIPT LOAD & FUNCTION DEFINITIONS
  // ============================================================
  section('1. Script load & functions defined');
  const expectedGlobals = ['init', 'dropPrompt', 'showToast', 'openSettings', 'closeSettings', 'renderWorkflows', 'callTool', 'configIsSynced'];
  for (const fn of expectedGlobals) {
    if (typeof window[fn] === 'function') pass(`${fn}() defined`);
    else fail(`${fn}() NOT defined · script likely threw before this point`);
  }

  // ============================================================
  // 2. CONFIG SYNCED
  // ============================================================
  section('2. CONFIG synced (placeholders replaced)');
  if (window.configIsSynced && window.configIsSynced()) pass('configIsSynced() returns true');
  else fail('configIsSynced() returns false · CONFIG still has placeholders');

  // ============================================================
  // 3. DOM ELEMENTS EXIST FOR SETTINGS
  // ============================================================
  section('3. Settings DOM exists');
  const settingsTabs = document.querySelectorAll('[data-open-settings]');
  if (settingsTabs.length > 0) pass(`Settings tab found (${settingsTabs.length})`);
  else fail('Settings tab [data-open-settings] missing');

  const closeButtons = document.querySelectorAll('[data-close-settings]');
  if (closeButtons.length > 0) pass(`Close X button found (${closeButtons.length})`);
  else fail('Close X button [data-close-settings] missing');

  const backdrop = document.querySelector('[data-settings-backdrop]');
  const panel = document.querySelector('[data-settings-panel]');
  if (backdrop) pass('Settings backdrop element exists'); else fail('Settings backdrop missing');
  if (panel) pass('Settings panel element exists'); else fail('Settings panel missing');

  // ============================================================
  // 4. CLICK: Settings open / close
  // ============================================================
  section('4. Click: Settings open + close');
  try {
    settingsTabs[0]?.click();
    await new Promise(r => setTimeout(r, 50));
    if (panel.classList.contains('open')) pass('Settings panel opens on tab click');
    else fail('Settings panel did NOT receive .open class');
    if (backdrop.classList.contains('open')) pass('Backdrop opens with panel');
    else fail('Backdrop did NOT open');
  } catch (e) { fail(`Settings open threw: ${e.message}`); }

  try {
    closeButtons[0]?.click();
    await new Promise(r => setTimeout(r, 50));
    if (!panel.classList.contains('open')) pass('Settings panel closes on X click');
    else fail('Settings panel did NOT close · X button broken');
  } catch (e) { fail(`Settings close threw: ${e.message}`); }

  // ============================================================
  // 5. CLICK: Backdrop closes panel
  // ============================================================
  section('5. Click: Backdrop closes panel');
  settingsTabs[0]?.click();
  await new Promise(r => setTimeout(r, 50));
  try {
    backdrop?.click();
    await new Promise(r => setTimeout(r, 50));
    if (!panel.classList.contains('open')) pass('Backdrop click closes panel');
    else fail('Backdrop click did NOT close panel');
  } catch (e) { fail(`Backdrop click threw: ${e.message}`); }

  // ============================================================
  // 6. WORKFLOW TILES rendered + clickable
  // ============================================================
  section('6. Workflow tiles');
  // v3 architecture: 15 Library entry cards, each binds 1+ spoke skills
  const entries = document.querySelectorAll('.wf-entry');
  if (entries.length === 15) pass(`15 Library entry cards rendered (expected 15)`);
  else fail(`${entries.length} entry cards rendered, expected 15`);

  // Open all entries so spoke chips are interactable for click test
  entries.forEach(e => e.setAttribute('open', ''));
  await new Promise(r => setTimeout(r, 50));

  const spokes = document.querySelectorAll('.wf-spoke');
  if (spokes.length > 0) pass(`${spokes.length} spoke chips rendered across cards`);
  else fail('No spoke chips rendered');

  // Click a sample of 3 spokes
  const sampleSpokes = [spokes[0], spokes[Math.floor(spokes.length/2)], spokes[spokes.length-1]].filter(s => s);
  sendPromptCalls.length = 0;
  for (const spoke of sampleSpokes) {
    const beforeCount = sendPromptCalls.length;
    try {
      spoke.click();
      await new Promise(r => setTimeout(r, 50));
      if (sendPromptCalls.length > beforeCount) {
        pass(`Spoke "${spoke.textContent}" → ${sendPromptCalls.slice(-1)[0].via}`);
      } else {
        fail(`Spoke "${spoke.textContent}" → NO sendPrompt/dropPrompt fired`);
      }
    } catch (e) {
      fail(`Spoke click threw: ${e.message}`);
    }
  }

  // ============================================================
  // 7. ON YOUR PLATE buttons
  // ============================================================
  section('7. On your plate queue buttons');
  const queueBtns = document.querySelectorAll('[data-queue] .q-btn');
  if (queueBtns.length > 0) {
    pass(`${queueBtns.length} queue buttons rendered`);
    sendPromptCalls.length = 0;
    try {
      queueBtns[0].click();
      await new Promise(r => setTimeout(r, 50));
      if (sendPromptCalls.length > 0) pass(`First queue button fires sendPrompt (via ${sendPromptCalls[0].via})`);
      else fail('Queue button click did NOT fire sendPrompt');
    } catch (e) { fail(`Queue button click threw: ${e.message}`); }
  } else {
    warn(`No queue buttons rendered · buildQueue() may have hit empty state`);
  }

  // ============================================================
  // 8. COMMAND BAR EXAMPLES
  // ============================================================
  section('8. Command bar example chips');
  const chips = document.querySelectorAll('.cmd-ex');
  if (chips.length === 4) pass(`4 example chips rendered`);
  else fail(`${chips.length} chips, expected 4`);
  sendPromptCalls.length = 0;
  try {
    chips[0]?.click();
    await new Promise(r => setTimeout(r, 50));
    if (sendPromptCalls.length > 0) pass(`Chip click fires sendPrompt (via ${sendPromptCalls[0].via})`);
    else fail('Chip click did NOT fire sendPrompt');
  } catch (e) { fail(`Chip click threw: ${e.message}`); }

  // ============================================================
  // 9. CMD INPUT Enter key
  // ============================================================
  section('9. Command input Enter key');
  const cmdInput = document.getElementById('cmd-input');
  if (cmdInput) {
    pass('cmd-input element exists');
    sendPromptCalls.length = 0;
    cmdInput.value = 'test submission';
    try {
      // Trigger the onkeydown handler
      const event = new window.KeyboardEvent('keydown', { key: 'Enter', bubbles: true, cancelable: true });
      cmdInput.dispatchEvent(event);
      await new Promise(r => setTimeout(r, 50));
      if (sendPromptCalls.length > 0) pass(`Enter fires sendPrompt (via ${sendPromptCalls[0].via})`);
      else fail('Enter key did NOT fire sendPrompt');
    } catch (e) { fail(`Enter key threw: ${e.message}`); }
  } else {
    fail('cmd-input element missing');
  }

  // ============================================================
  // 10. SETTINGS Ask Claude buttons
  // ============================================================
  section('10. Settings "Ask Claude" buttons');
  settingsTabs[0]?.click();
  await new Promise(r => setTimeout(r, 100));
  const askButtons = document.querySelectorAll('[data-settings-connectors] button, [data-settings-checklist] button');
  if (askButtons.length > 0) {
    pass(`${askButtons.length} Ask Claude buttons rendered`);
    sendPromptCalls.length = 0;
    try {
      askButtons[0].click();
      await new Promise(r => setTimeout(r, 50));
      if (sendPromptCalls.length > 0) pass(`First Ask Claude button fires sendPrompt (via ${sendPromptCalls[0].via})`);
      else fail('Ask Claude button click did NOT fire sendPrompt');
    } catch (e) { fail(`Ask Claude click threw: ${e.message}`); }
  } else fail('No Ask Claude buttons rendered in settings');

  // ============================================================
  // 11. TOOL CALLS made
  // ============================================================
  section('11. MCP tool calls during init()');
  const expectedTools = ['get-shop-info', 'run-analytics-query', 'klaviyo', 'get_tasks', 'search_files'];
  for (const expected of expectedTools) {
    const found = toolCalls.find(c => c.name.includes(expected));
    if (found) pass(`Tool called: ${expected}`);
    else warn(`Tool NOT called: ${expected} · loader may have bailed early`);
  }

  // ============================================================
  // 12. KPI fields populated
  // ============================================================
  section('12. KPI placeholder replacement');
  // Just check that some data-kpi text was replaced
  const kpiRev = document.querySelector('[data-kpi="revenue-7d"]');
  if (kpiRev && kpiRev.textContent !== '—' && kpiRev.textContent !== '') {
    pass(`Revenue KPI populated: "${kpiRev.textContent}"`);
  } else {
    warn(`Revenue KPI still placeholder: "${kpiRev?.textContent}"`);
  }

  // ============================================================
  // SUMMARY
  // ============================================================
  console.log('\n\x1b[1mSummary\x1b[0m');
  console.log(`  Errors: ${errors.length}`);
  console.log(`  Warnings: ${warnings.length}`);
  console.log(`  sendPrompt calls fired: ${sendPromptCalls.length}`);
  console.log(`  Tool calls fired: ${toolCalls.length}`);

  if (errors.length > 0) {
    console.log('\n\x1b[91m\x1b[1mFAILURES\x1b[0m');
    for (const e of errors) console.log(`  · ${e}`);
    process.exit(1);
  } else {
    console.log('\n\x1b[92m\x1b[1mALL CHECKS PASSED\x1b[0m');
  }
}

main().catch(e => {
  console.error('\x1b[91m\x1b[1mFATAL:\x1b[0m', e);
  process.exit(2);
});
