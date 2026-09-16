import pandas as pd
import json
import os

def main():
    print("Loading datasets...")
    test_df = pd.read_csv("data/splits/amazon_test.csv")
    twcs_df = pd.read_csv("data/twcs.csv")
    
    # Exclude AMBIGUOUS and null weak_labels
    valid_test_df = test_df[test_df['weak_label'].notna() & (test_df['weak_label'] != 'AMBIGUOUS')]
    
    print("Stratified sampling...")
    # There are 9 intents. 200 total examples.
    # ~22 per intent.
    intents = valid_test_df['weak_label'].unique()
    samples = []
    
    # We want exactly 200. 9 * 22 = 198. We will take 22 from each, and 2 extra from OTHER.
    target_counts = {intent: 22 for intent in intents}
    target_counts["OTHER"] += 2
    
    for intent, count in target_counts.items():
        intent_df = valid_test_df[valid_test_df['weak_label'] == intent]
        n = min(count, len(intent_df))
        samples.append(intent_df.sample(n=n, random_state=42))
        
    sample_df = pd.concat(samples).sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Ensure exactly 200
    assert len(sample_df) == 200, f"Expected 200 examples, got {len(sample_df)}"
    
    print("Reconstructing context...")
    # twcs indexed by tweet_id for fast lookup
    twcs_dict = twcs_df.set_index('tweet_id').to_dict('index')
    
    golden_annotations = []
    golden_metadata = []
    
    for idx, row in sample_df.iterrows():
        target_tweet_id = row['tweet_id']
        golden_id = f"G-{1000 + idx}"
        
        # Walk back to root
        path = []
        curr = target_tweet_id
        while pd.notna(curr) and curr in twcs_dict:
            path.append({
                "tweet_id": curr,
                "author": twcs_dict[curr]['author_id'],
                "text": twcs_dict[curr]['text'],
                "timestamp": twcs_dict[curr]['created_at'],
                "inbound": twcs_dict[curr]['inbound']
            })
            curr = twcs_dict[curr]['in_response_to_tweet_id']
            if curr == path[-1]["tweet_id"]: # Prevent loop
                break
                
        # path is from target back to root. Reverse it to chronological
        path.reverse()
        
        # The target message is the last one in the path
        target_msg = path[-1]['text']
        
        # Context is everything before the target message
        context = path[:-1]
        
        # Format context nicely
        formatted_context = [{"author": m["author"], "text": m["text"], "timestamp": m["timestamp"]} for m in context]
        
        # Annotation record
        golden_annotations.append({
            "golden_id": golden_id,
            "customer_message": target_msg,
            "conversation_context": json.dumps(formatted_context),
            "human_intent": "",
            "human_intent_confidence": "",
            "human_intent_notes": "",
            "human_resolution_supported": "",
            "human_resolution_notes": "",
            "human_auto_handle": "",
            "human_auto_handle_notes": "",
            "human_reply_quality": "",
            "human_reply_quality_notes": "",
            "annotation_complete": ""
        })
        
        # Metadata record
        golden_metadata.append({
            "golden_id": golden_id,
            "tweet_id": int(target_tweet_id),
            "root_id": int(row['root_id']),
            "source_split": "INTERNAL_TEST",
            "weak_label": row['weak_label'],
            "created_at": row['created_at']
        })
        
    os.makedirs("data/golden_set", exist_ok=True)
    
    # Save Annotation CSV
    pd.DataFrame(golden_annotations).to_csv("data/golden_set/golden_set_annotation.csv", index=False)
    
    # Save Metadata JSON
    with open("data/golden_set/golden_set_metadata.json", "w") as f:
        json.dump(golden_metadata, f, indent=2)
        
    print("Golden Set created successfully.")

if __name__ == "__main__":
    main()
