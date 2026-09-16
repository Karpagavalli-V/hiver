import pandas as pd
import json

def main():
    print("Loading dataset...")
    df = pd.read_csv("data/twcs.csv")
    
    with open("reports/brand_analysis.json") as f:
        analysis = json.load(f)
        
    top_brands = [b['brand'] for b in analysis['brand_stats'][:5]]
    print(f"Top 5 brands: {top_brands}")
    
    parent_map = dict(zip(df['tweet_id'], df['in_response_to_tweet_id']))
    
    with open("reports/conversations_sample.md", "w", encoding="utf-8") as out_f:
        for brand in top_brands:
            out_f.write(f"\n=========================================\n")
            out_f.write(f"BRAND: {brand}\n")
            out_f.write(f"=========================================\n\n")
            
            # Find some outbound tweets from this brand that are part of a conversation
            brand_outbound = df[(df['author_id'] == brand) & (df['inbound'] == False)]
            
            brand_responded_to = brand_outbound['in_response_to_tweet_id'].dropna().unique()
            inbound = df[(df['tweet_id'].isin(brand_responded_to)) & (df['inbound'] == True)]
            
            # Let's pick 2 random conversations
            sample_inbounds = inbound.sample(2, random_state=42)
            
            for idx, row in sample_inbounds.iterrows():
                thread = []
                
                curr_id = row['tweet_id']
                backward_path = []
                while pd.notna(curr_id) and curr_id in parent_map:
                    p_id = parent_map[curr_id]
                    if pd.isna(p_id) or p_id == curr_id:
                        break
                    backward_path.append(p_id)
                    curr_id = p_id
                    
                backward_path.reverse()
                
                for t_id in backward_path:
                    t_row = df[df['tweet_id'] == t_id]
                    if not t_row.empty:
                        t_row = t_row.iloc[0]
                        author = t_row['author_id']
                        text = t_row['text'].replace('\n', ' ')
                        role = "BRAND" if author == brand else "CUSTOMER"
                        out_f.write(f"{role} ({author}):\n\"{text}\"\n\n")
                
                queue = [row['tweet_id']]
                visited = set()
                
                while queue:
                    curr_id = queue.pop(0)
                    if curr_id in visited: continue
                    visited.add(curr_id)
                    
                    t_row = df[df['tweet_id'] == curr_id]
                    if not t_row.empty:
                        t_row = t_row.iloc[0]
                        author = t_row['author_id']
                        text = t_row['text'].replace('\n', ' ')
                        role = "BRAND" if author == brand else "CUSTOMER"
                        out_f.write(f"{role} ({author}):\n\"{text}\"\n\n")
                        
                        responses_str = t_row['response_tweet_id']
                        if pd.notna(responses_str):
                            responses = [int(r) for r in str(responses_str).split(',')]
                            queue.extend(responses)
                out_f.write("---\n")

if __name__ == "__main__":
    main()
