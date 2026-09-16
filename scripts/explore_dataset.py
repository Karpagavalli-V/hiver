import pandas as pd
import json
import os
import argparse
import numpy as np
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/twcs.csv", help="Input dataset path")
    args = parser.parse_args()

    print(f"Loading dataset from {args.input}...")
    df = pd.read_csv(args.input)
    print("Dataset loaded. Computing dataset-level stats...")
    
    # 1. Dataset exploration
    num_rows = len(df)
    num_cols = len(df.columns)
    column_names = df.columns.tolist()
    data_types = {col: str(dt) for col, dt in df.dtypes.items()}
    missing_values = df.isnull().sum().to_dict()
    duplicate_tweet_ids = int(df['tweet_id'].duplicated().sum())
    duplicate_rows = int(df.duplicated().sum())
    num_unique_authors = int(df['author_id'].nunique())
    num_inbound = int(df['inbound'].sum())
    num_outbound = num_rows - num_inbound
    
    print("Parsing dates...")
    df['created_at_dt'] = pd.to_datetime(df['created_at'], format='%a %b %d %H:%M:%S +0000 %Y', errors='coerce')
    date_min = str(df['created_at_dt'].min())
    date_max = str(df['created_at_dt'].max())

    print("Identifying threads/conversations across full dataset...")
    # Fix: To avoid leakage, we trace roots for ALL tweets globally.
    parent_map = dict(zip(df['tweet_id'], df['in_response_to_tweet_id']))
    
    roots = {}
    for t_id in df['tweet_id']:
        curr = t_id
        path = []
        while pd.notna(curr) and curr in parent_map:
            if curr in roots:
                curr = roots[curr]
                break
            p = parent_map[curr]
            if pd.isna(p) or p == curr:
                break
            path.append(curr)
            curr = p
            
        for node in path:
            roots[node] = curr
        roots[t_id] = curr
        
    df['root_id'] = df['tweet_id'].map(roots)
    num_unique_conversations = int(df['root_id'].nunique())
    
    print("Identifying Brands...")
    brand_tweets = df[df['inbound'] == False]
    brand_counts = brand_tweets.groupby('author_id').size()
    
    top_brands = brand_counts.nlargest(10).index.tolist()
    print(f"Top 10 brands: {top_brands}")
    
    brand_stats = []
    
    for brand in top_brands:
        print(f"Analyzing brand: {brand}")
        
        # All roots involving this brand
        b_roots = df[df['author_id'] == brand]['root_id'].unique()
        
        # All tweets belonging to these conversations
        b_all = df[df['root_id'].isin(b_roots)]
        
        conv_groups = b_all.groupby('root_id')
        total_convs = len(conv_groups)
        conv_sizes = conv_groups.size()
        multi_turn_convs = (conv_sizes > 2).sum()
        avg_conv_length = float(conv_sizes.mean())
        
        # Outbound tweets are tweets by the brand
        b_outbound = b_all[b_all['author_id'] == brand]
        # Inbound tweets are all other tweets in these threads
        b_inbound = b_all[b_all['author_id'] != brand]
        
        outbound_count = len(b_outbound)
        inbound_count = len(b_inbound)
        
        score = np.log1p(total_convs) + (multi_turn_convs / total_convs) * 10 if total_convs > 0 else 0
        
        brand_stats.append({
            "brand": brand,
            "outbound_tweets": outbound_count,
            "inbound_tweets": inbound_count,
            "total_conversations": int(total_convs),
            "multi_turn_conversations": int(multi_turn_convs),
            "avg_conv_length": avg_conv_length,
            "score": float(score)
        })

    brand_stats.sort(key=lambda x: x['score'], reverse=True)

    results = {
        "dataset_stats": {
            "num_rows": num_rows,
            "num_cols": num_cols,
            "column_names": column_names,
            "data_types": data_types,
            "missing_values": missing_values,
            "duplicate_tweet_ids": duplicate_tweet_ids,
            "duplicate_rows": duplicate_rows,
            "num_unique_authors": num_unique_authors,
            "num_inbound": num_inbound,
            "num_outbound": num_outbound,
            "date_range": [date_min, date_max],
            "num_unique_conversations": num_unique_conversations
        },
        "brand_stats": brand_stats
    }
    
    os.makedirs("reports", exist_ok=True)
    with open("reports/brand_analysis.json", "w") as f:
        json.dump(results, f, indent=2)
        
    pd.DataFrame(brand_stats).to_csv("reports/brand_analysis.csv", index=False)
    
    print("Analysis complete. Check reports/brand_analysis.json and reports/brand_analysis.csv")

if __name__ == "__main__":
    main()
