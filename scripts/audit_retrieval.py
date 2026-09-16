import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')
from src.retrieval.historical_retriever import HistoricalRetriever

def main():
    print("Loading Retriever for Audit...")
    retriever = HistoricalRetriever()
    
    val_df = pd.read_csv("data/splits/amazon_val.csv")
    twcs_df = pd.read_csv("data/twcs.csv")
    val_df = val_df[val_df['weak_label'].notna() & (val_df['weak_label'] != 'AMBIGUOUS')]
    
    merged = pd.merge(val_df, twcs_df[['tweet_id', 'text']], on='tweet_id', how='inner')
    merged['created_at_dt'] = pd.to_datetime(merged['created_at'], format='%a %b %d %H:%M:%S +0000 %Y', errors='coerce')
    
    sample_df = merged.sample(n=20, random_state=123)
    
    print("\n--- AUDIT OF 20 RETRIEVAL EXAMPLES ---")
    
    # We will also load train_df to strictly verify splits
    train_df = pd.read_csv("data/splits/amazon_train.csv")
    train_roots = set(train_df['root_id'].dropna())
    
    for idx, row in sample_df.iterrows():
        print(f"\nTARGET QUERY (Root: {row['root_id']}): {row['text']}")
        print(f"Target Intent: {row['weak_label']}")
        
        results = retriever.retrieve(
            query_message=row['text'],
            query_root_id=row['root_id'],
            query_timestamp=row['created_at_dt'],
            top_k=1
        )
        
        if not results:
            print("  -> No results.")
            continue
            
        res = results[0]
        print(f"  -> RETRIEVED CUSTOMER (Root: {res['root_id']}): {res['customer_message']}")
        print(f"  -> RETRIEVED RESPONSE: {res['historical_response']}")
        print(f"  -> Retrieved Intent: {res['intent']} (Sim: {res['similarity_score']:.3f})")
        
        # Verify conditions
        is_train = res['root_id'] in train_roots
        print(f"  -> Verification: Belongs to TRAIN split? {is_train}")
        if not is_train:
            print("  !!! FAIL: Retrieved item not in train split !!!")
            
        if res['root_id'] == row['root_id']:
            print("  !!! FAIL: Retrieved target conversation !!!")

if __name__ == "__main__":
    main()
