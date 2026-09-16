import pandas as pd
from src.retrieval.historical_retriever import HistoricalRetriever

def main():
    print("Loading Validation Split...")
    val_df = pd.read_csv("data/splits/amazon_val.csv")
    twcs_df = pd.read_csv("data/twcs.csv")
    
    # Filter valid targets
    val_df = val_df[val_df['weak_label'].notna() & (val_df['weak_label'] != 'AMBIGUOUS')]
    
    # Merge for text and timestamp
    merged = pd.merge(val_df, twcs_df[['tweet_id', 'text']], on='tweet_id', how='inner')
    merged['created_at_dt'] = pd.to_datetime(merged['created_at'], format='%a %b %d %H:%M:%S +0000 %Y', errors='coerce')
    
    # Deterministic sample
    sample_df = merged.sample(n=min(500, len(merged)), random_state=42)
    
    retriever = HistoricalRetriever()
    
    total_queries = 0
    top1_match = 0
    top3_match = 0
    empty_results = 0
    total_sim_score = 0.0
    
    print(f"Evaluating on {len(sample_df)} queries...")
    for idx, row in sample_df.iterrows():
        total_queries += 1
        
        results = retriever.retrieve(
            query_message=row['text'],
            intent=None,
            top_k=3,
            query_root_id=row['root_id'],
            query_timestamp=row['created_at_dt']
        )
        
        if not results:
            empty_results += 1
            continue
            
        target_intent = row['weak_label']
        
        top1_intent = results[0]['intent']
        if top1_intent == target_intent:
            top1_match += 1
            
        if any(r['intent'] == target_intent for r in results):
            top3_match += 1
            
        total_sim_score += results[0]['similarity_score']
        
    print("\n=== RETRIEVAL EVALUATION (WEAK-LABEL DEVELOPMENT) ===")
    print(f"Total Queries Evaluated: {total_queries}")
    print(f"Empty Retrieval %: {(empty_results / total_queries * 100):.1f}%")
    
    valid_queries = total_queries - empty_results
    if valid_queries > 0:
        print(f"Top-1 Intent Match Rate: {(top1_match / valid_queries * 100):.1f}%")
        print(f"Top-3 Intent Match Rate: {(top3_match / valid_queries * 100):.1f}%")
        print(f"Avg Top-1 Similarity Score: {(total_sim_score / valid_queries):.4f}")

if __name__ == "__main__":
    main()
