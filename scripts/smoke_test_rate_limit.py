import os
import sys
import time
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'classification')))
from llm_classifier import LLMClassifier
from data_utils import build_dataset

def main():
    load_dotenv(override=True)
    
    print("Building dataset for rate-limit smoke test...")
    val_df = build_dataset("data/twcs.csv", "data/splits/amazon_val.csv", max_context=3)
    # Using 10 examples to force ~20 API calls
    val_df = val_df.sample(n=10, random_state=123) 
    
    X_msg = val_df['message_only'].tolist()
    X_ctx = val_df['context_aware'].tolist()
    
    classifier = LLMClassifier(mock_mode=False)
    # Flush cache temporarily for this run if we want to hit the API?
    # The prompt says: "Use the existing cache where possible."
    # So we don't clear the cache, but to ensure we test rate limits, 
    # we use a new random state (123) which likely has uncached examples.
    
    successful = 0
    err_429 = 0
    err_other = 0
    cache_hits_start = classifier.cache_hits
    
    start_time = time.time()
    
    print("Running 10 examples (20 API calls max). Watch for retries...")
    for i in range(10):
        target = X_msg[i]
        
        raw_ctx_parts = X_ctx[i].split(" ||| ")
        actual_ctx = " ||| ".join(raw_ctx_parts[:-1]) if len(raw_ctx_parts) > 1 else None
        
        # 1. MESSAGE ONLY
        try:
            res = classifier.classify(target, context=None)
            if res.intent == "FAIL" or "Failed to parse" in res.reason:
                err_other += 1
            else:
                successful += 1
        except Exception as e:
            if "RateLimitError" in type(e).__name__ or "429" in str(e):
                err_429 += 1
            else:
                err_other += 1
                
        # 2. CONTEXT AWARE
        try:
            res = classifier.classify(target, context=actual_ctx)
            if res.intent == "FAIL" or "Failed to parse" in res.reason:
                err_other += 1
            else:
                successful += 1
        except Exception as e:
            if "RateLimitError" in type(e).__name__ or "429" in str(e):
                err_429 += 1
            else:
                err_other += 1
                
    elapsed = time.time() - start_time
    cache_hits_total = classifier.cache_hits - cache_hits_start
    
    print("\n--- SMOKE TEST RESULTS ---")
    print(f"Total Attempted: 20")
    print(f"Successful Calls: {successful}")
    print(f"429 RateLimit Errors: {err_429}")
    print(f"Other Errors: {err_other}")
    print(f"Cache Hits: {cache_hits_total}")
    print(f"Elapsed Time: {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()
