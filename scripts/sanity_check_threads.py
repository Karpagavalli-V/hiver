import pandas as pd

def main():
    print("Loading dataset...")
    df = pd.read_csv("data/twcs.csv", nrows=1000000) # Load a subset for speed, or full. Actually let's load full.
    df = pd.read_csv("data/twcs.csv")
    
    brand = "AmazonHelp"
    
    print("Reconstructing using Phase 1 logic...")
    brand_tweets = df[df['inbound'] == False]
    b_outbound = brand_tweets[brand_tweets['author_id'] == brand]
    b_out_ids = set(b_outbound['tweet_id'])
    
    brand_replied_to = b_outbound['in_response_to_tweet_id'].dropna().unique()
    customer_replies = df[(df['inbound'] == True) & (df['in_response_to_tweet_id'].isin(b_out_ids))]
    
    relevant_inbound = df[df['tweet_id'].isin(brand_replied_to)]
    b_inbound = pd.concat([relevant_inbound, customer_replies]).drop_duplicates(subset=['tweet_id'])
    b_all = pd.concat([b_outbound, b_inbound])
    
    b_parent_map = dict(zip(b_all['tweet_id'], b_all['in_response_to_tweet_id']))
    b_roots = {}
    for t_id in b_parent_map:
        curr = t_id
        visited = set()
        while pd.notna(curr) and curr in b_parent_map:
            p = b_parent_map[curr]
            if pd.isna(p) or p == curr or p in visited:
                break
            visited.add(curr)
            curr = p
        b_roots[t_id] = curr
        
    b_all['root_id'] = b_all['tweet_id'].map(b_roots)
    
    # Pick a few multi-turn conversations
    conv_groups = b_all.groupby('root_id')
    sizes = conv_groups.size()
    multi_turn_roots = sizes[sizes >= 4].index.tolist()
    
    import random
    random.seed(42)
    sample_roots = random.sample(multi_turn_roots, 5)
    
    for root in sample_roots:
        print(f"\n=== Thread Root: {root} ===")
        thread_df = b_all[b_all['root_id'] == root].copy()
        
        # Sort by tweet_id or somewhat chronologically
        # Tweet IDs are generally chronological
        thread_df = thread_df.sort_values('tweet_id')
        
        for idx, row in thread_df.iterrows():
            parent = row['in_response_to_tweet_id']
            # Also check if parent is in thread
            parent_in_thread = parent in thread_df['tweet_id'].values
            parent_str = f" [-> replies to {parent}]" if pd.notna(parent) else " [ROOT]"
            warning = "" if parent_in_thread or pd.isna(parent) else " !!PARENT MISSING!!"
            
            print(f"{row['tweet_id']} | {row['author_id']}{parent_str}{warning}: {row['text'][:80]}...")

if __name__ == "__main__":
    main()
