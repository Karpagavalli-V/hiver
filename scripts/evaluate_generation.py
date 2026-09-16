import pandas as pd
from src.retrieval.historical_retriever import HistoricalRetriever
from src.generation.reply_generator import ReplyGenerator, MockReplyProvider

def main():
    print("Loading Validation Split for Generation Evaluation...")
    val_df = pd.read_csv("data/splits/amazon_val.csv")
    twcs_df = pd.read_csv("data/twcs.csv")
    
    val_df = val_df[val_df['weak_label'].notna() & (val_df['weak_label'] != 'AMBIGUOUS')]
    
    merged = pd.merge(val_df, twcs_df[['tweet_id', 'text']], on='tweet_id', how='inner')
    merged['created_at_dt'] = pd.to_datetime(merged['created_at'], format='%a %b %d %H:%M:%S +0000 %Y', errors='coerce')
    
    sample_df = merged.sample(n=min(500, len(merged)), random_state=42)
    
    retriever = HistoricalRetriever()
    generator = ReplyGenerator(provider=MockReplyProvider())
    
    total_cases = 0
    valid_output_count = 0
    fallback_count = 0
    missing_evidence_count = 0
    evidence_attachment_count = 0
    
    print(f"Evaluating {len(sample_df)} generation pipelines offline...")
    
    for idx, row in sample_df.iterrows():
        total_cases += 1
        
        results = retriever.retrieve(
            query_message=row['text'],
            intent=row['weak_label'],
            top_k=3,
            query_root_id=row['root_id'],
            query_timestamp=row['created_at_dt']
        )
        
        reply_dict = generator.generate(
            customer_message=row['text'],
            intent=row['weak_label'],
            retrieved_examples=results
        )
        
        # Check schema
        expected_keys = {"reply", "grounding_summary", "evidence_used", "confidence", "warnings"}
        if expected_keys.issubset(set(reply_dict.keys())):
            valid_output_count += 1
            
        if not results:
            missing_evidence_count += 1
            
        if "[MOCK]" not in reply_dict['reply'] and "I apologize" in reply_dict['reply']:
            fallback_count += 1
            
        if len(reply_dict.get('evidence_used', [])) > 0:
            evidence_attachment_count += 1

    print("\n=== OFFLINE PIPELINE GENERATION METRICS ===")
    print("Note: These are pipeline/infrastructure checks via MockProvider, NOT human-rated LLM quality results.")
    print(f"Total test cases: {total_cases}")
    print(f"Valid schema output rate: {(valid_output_count / total_cases * 100):.1f}%")
    print(f"Missing-evidence rate (retrieval empty): {(missing_evidence_count / total_cases * 100):.1f}%")
    print(f"Fallback rate: {(fallback_count / total_cases * 100):.1f}%")
    print(f"Evidence attachment rate: {(evidence_attachment_count / total_cases * 100):.1f}%")

if __name__ == "__main__":
    main()
