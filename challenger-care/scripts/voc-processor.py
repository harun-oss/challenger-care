#!/usr/bin/env python3
"""
Challenger Care · VOC Processor

Re-runs theme coding, sentiment analysis, and quote curation on any review CSV.
Combines all CSVs in assets/voc/exports/ into a unified corpus.

Usage:
    python3 scripts/voc-processor.py

Input:  assets/voc/exports/*.csv (any JudgeMe or Amazon review export format)
Output: assets/voc/voc-corpus.csv + JSON analytics + refreshed quote rankings
"""

import os, csv, json, re, glob
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPORTS_DIR = ROOT / "assets" / "voc" / "exports"
OUTPUT_DIR = ROOT / "assets" / "voc"

THEMES = {
    'hold': ['hold', 'holds', 'all day', 'lasting', 'control', 'firm'],
    'fragrance_free': ['unscented', 'fragrance free', 'fragrance-free', 'no scent', 'no smell'],
    'grease_free': ['no grease', 'not greasy', 'no shine', 'no residue', 'matte finish'],
    'grease_problem': ['greasy', 'grease', 'sticky', 'oily', 'shiny'],
    'irritation_free': ['no irritation', 'sensitive skin', 'gentle'],
    'irritation_problem': ['irritated', 'rash', 'breakout', 'reaction', 'allergic'],
    'humidity': ['humid', 'humidity', 'sweat', 'gym', 'workout'],
    'acne_skin': ['acne', 'pimple', 'comedogenic', 'forehead'],
    'natural_clean': ['clean ingredient', 'natural', 'sulfate', 'paraben'],
    'packaging': ['container', 'jar', 'packaging', 'lid'],
    'wash_out': ['wash out', 'rinse out', 'washes out', 'water based'],
    'value': ['price', 'value', 'worth it', 'expensive'],
    'subscribe_repeat': ['subscribe', 'reorder', 'years', 'second time', 'third time'],
    'works_results': ['works great', 'works well', 'effective', 'as advertised'],
    'easy_use': ['easy to use', 'goes a long way', 'little goes', 'one minute'],
    'style_finish': ['natural look', 'matte finish', 'looks natural'],
    'comparison': ['compared to', 'better than', 'switched from', 'used to use'],
    'quality': ['high quality', 'premium', 'best ever', 'amazing'],
}

PRODUCT_CATS = {
    'pomade': ['pomade', 'clean', 'matte', 'styling', 'cream'],
    'shampoo': ['shampoo'],
    'conditioner': ['conditioner'],
    'body_wash': ['body-wash', 'bodywash'],
    'face': ['eye-cream', 'face', 'primo'],
    'combo': ['combo', 'pack', 'bundle'],
}


def categorize_product(handle):
    h = (handle or '').lower()
    for cat, keys in PRODUCT_CATS.items():
        if any(k in h for k in keys):
            return cat
    return 'other'


def code_themes(body):
    text = (body or '').lower()
    matched = []
    for theme, kws in THEMES.items():
        if any(kw in text for kw in kws):
            matched.append(theme)
    return matched


def sentiment(rating):
    try:
        r = int(rating)
    except:
        return 'unknown'
    if r >= 4: return 'positive'
    if r == 3: return 'neutral'
    return 'negative'


def ad_ready_score(body, rating, word_count, title):
    score = 0
    if re.search(r'\b\d+\s*(year|month|week|day|hour|minute|jar|bottle|pack)\b', body, re.I): score += 3
    if re.search(r'\$\d+', body): score += 2
    if re.search(r'\b(love|hands down|best|finally|never|always|amazing|game changer)\b', body, re.I): score += 2
    if re.search(r'\b(gym|work|meeting|interview|wedding|date|morning|workout)\b', body, re.I): score += 2
    if re.search(r'\b(compared to|better than|switched from|used to|other brand)\b', body, re.I): score += 3
    if 25 <= word_count <= 100: score += 3
    elif 15 <= word_count <= 150: score += 1
    if rating == 'positive': score += 2
    if 3 <= len(title.split()) <= 8: score += 1
    return score


def main():
    print(f"VOC Processor · Challenger Care\n")
    print(f"Reading from: {EXPORTS_DIR}")

    csv_files = list(EXPORTS_DIR.glob("*.csv"))
    if not csv_files:
        print("No CSV files found in assets/voc/exports/")
        return

    all_reviews = []
    for csv_file in csv_files:
        print(f"  - {csv_file.name}")
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                title = row.get('title', '') or ''
                body = row.get('body', '') or ''
                wc = len(body.split())
                rating_str = row.get('rating', '5')
                sent = sentiment(rating_str)
                all_reviews.append({
                    'title': title,
                    'body': body,
                    'rating': rating_str,
                    'date': (row.get('review_date', '') or '')[:10],
                    'source': csv_file.stem,
                    'reviewer': row.get('reviewer_name', ''),
                    'product_handle': row.get('product_handle', ''),
                    'product_cat': categorize_product(row.get('product_handle', '')),
                    'themes': code_themes(body),
                    'sentiment': sent,
                    'word_count': wc,
                    'ad_score': ad_ready_score(body, sent, wc, title),
                })

    print(f"\nTotal reviews processed: {len(all_reviews)}")

    # Write corpus
    with open(OUTPUT_DIR / "voc-corpus.csv", "w", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title','body','rating','date','source','reviewer','product_handle','product_cat','themes','sentiment','word_count','ad_score'])
        writer.writeheader()
        for r in all_reviews:
            r2 = dict(r)
            r2['themes'] = '|'.join(r['themes'])
            writer.writerow(r2)

    # Theme counts
    theme_counts = Counter()
    for r in all_reviews:
        for t in r['themes']:
            theme_counts[t] += 1
    with open(OUTPUT_DIR / "theme-counts.json", "w") as f:
        json.dump(dict(theme_counts.most_common()), f, indent=2)

    # Top 50 quotes
    top_50 = sorted(all_reviews, key=lambda x: -x['ad_score'])[:50]
    with open(OUTPUT_DIR / "top-50-quotes.json", "w") as f:
        json.dump([{
            'rank': i+1, 'score': r['ad_score'], 'rating': r['rating'],
            'product_cat': r['product_cat'], 'date': r['date'],
            'title': r['title'], 'body': r['body'], 'themes': r['themes'],
        } for i, r in enumerate(top_50)], f, indent=2)

    # Quotes by theme
    theme_groups = defaultdict(list)
    for r in all_reviews:
        for t in r['themes']:
            theme_groups[t].append(r)
    theme_top = {}
    for theme, items in theme_groups.items():
        items_sorted = sorted(items, key=lambda x: -x['ad_score'])
        theme_top[theme] = [{
            'rating': r['rating'], 'date': r['date'], 'title': r['title'],
            'body': r['body'], 'product_cat': r['product_cat'], 'score': r['ad_score'],
        } for r in items_sorted[:7]]
    with open(OUTPUT_DIR / "quotes-by-theme.json", "w") as f:
        json.dump(theme_top, f, indent=2)

    # Reviews processed (full)
    with open(OUTPUT_DIR / "reviews-processed.json", "w") as f:
        json.dump(all_reviews, f, indent=2)

    print(f"\n✓ Outputs written to {OUTPUT_DIR}")
    print(f"  voc-corpus.csv ({len(all_reviews)} reviews)")
    print(f"  theme-counts.json")
    print(f"  top-50-quotes.json")
    print(f"  quotes-by-theme.json")
    print(f"  reviews-processed.json")
    print(f"\nTop 10 themes:")
    for t, c in theme_counts.most_common(10):
        print(f"  {t}: {c}")


if __name__ == "__main__":
    main()
