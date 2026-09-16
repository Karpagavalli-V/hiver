import pandas as pd
import time

def main():
    print("Loading dataset...")
    df = pd.read_csv("data/twcs.csv")
    print(f"Loaded {len(df)} rows")
    
    start = time.time()
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
    print(f"Root finding took {time.time() - start:.2f} seconds")
    
    brand = "AmazonHelp"
    brand_roots = df[df['author_id'] == brand]['root_id'].unique()
    brand_convs = df[df['root_id'].isin(brand_roots)]
    
    print(f"Total {brand} convs: {len(brand_roots)}")
    print(f"Total tweets in {brand} convs: {len(brand_convs)}")

if __name__ == "__main__":
    main()
