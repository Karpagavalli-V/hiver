import os
import sys
import pandas as pd
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'retrieval')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'generation')))

from historical_retriever import HistoricalRetriever
from reply_generator import ReplyGenerator, LLMReplyProvider

def main():
    load_dotenv(override=True)
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: API key not set.")
        sys.exit(1)

    print("Loading validation examples...")
    val_df = pd.read_csv("data/splits/amazon_val.csv")
    val_df = val_df[val_df['weak_label'].notna() & (val_df['weak_label'] != 'AMBIGUOUS')]
    twcs_df = pd.read_csv("data/twcs.csv")
    merged = pd.merge(val_df, twcs_df[['tweet_id', 'text']], on='tweet_id', how='inner')
    merged['created_at_dt'] = pd.to_datetime(merged['created_at'], format='%a %b %d %H:%M:%S +0000 %Y', errors='coerce')
    
    # 2 representative AmazonHelp validation examples
    sample_df = merged.sample(n=2, random_state=42)

    retriever = HistoricalRetriever()
    generator = ReplyGenerator(provider=LLMReplyProvider(mock_mode=False))
    
    print("\n--- RUNNING REAL REPLY-GENERATION SMOKE TEST (2 EXAMPLES) ---\n")
    for idx, row in sample_df.iterrows():
        print(f"\nEvaluating target message: {row['text']}")
        try:
            # Obtain historical evidence from TRAIN only (enforced by HistoricalRetriever initialization)
            retrieved_evidence = retriever.retrieve(
                query_message=row['text'],
                intent=row['weak_label'],
                top_k=3,
                query_root_id=row['root_id'],
                query_timestamp=row['created_at_dt']
            )
            
            # Generate reply via LLM
            reply_dict = generator.generate(
                customer_message=row['text'],
                intent=row['weak_label'],
                retrieved_examples=retrieved_evidence
            )
            
            # Constraints Verification
            assert "reply" in reply_dict and str(reply_dict["reply"]).strip(), "Reply is empty or missing"
            assert "evidence_used" in reply_dict, "evidence_used is missing"
            assert "grounding_summary" in reply_dict and str(reply_dict["grounding_summary"]).strip(), "grounding_summary is missing"
            
            print("SUCCESS: JSON Parsed & Schema Validated")
            print(f"Reply: {reply_dict['reply']}")
            print(f"Grounding Summary: {reply_dict['grounding_summary']}")
            print(f"Evidence Used: {reply_dict['evidence_used']}")
            print(f"Warnings: {reply_dict['warnings']}")
            
        except Exception as e:
            print(f"FAILED: {e}")

    print("\n--- VERIFICATION COMPLETED ---")
    
if __name__ == "__main__":
    main()
