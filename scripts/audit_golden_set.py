import pandas as pd
import json
import sys

def main():
    print("Running Golden Set Audit...")
    
    # 1. Load splits and files
    train_df = pd.read_csv("data/splits/amazon_train.csv")
    val_df = pd.read_csv("data/splits/amazon_val.csv")
    twcs_df = pd.read_csv("data/twcs.csv")
    
    anno_df = pd.read_csv("data/golden_set/golden_set_annotation.csv")
    with open("data/golden_set/golden_set_metadata.json", "r") as f:
        meta_list = json.load(f)
    meta_df = pd.DataFrame(meta_list)
    
    # Assert exactly 200
    assert len(anno_df) == 200, f"Expected 200 annotations, got {len(anno_df)}"
    assert len(meta_df) == 200, f"Expected 200 metadata, got {len(meta_df)}"
    print("Pass: Exactly 200 examples.")
    
    # Assert all from INTERNAL_TEST
    assert all(meta_df['source_split'] == "INTERNAL_TEST"), "Not all from INTERNAL_TEST"
    print("Pass: All examples sourced from INTERNAL_TEST.")
    
    # Assert no root_id in TRAIN or VALIDATION
    train_roots = set(train_df['root_id'])
    val_roots = set(val_df['root_id'])
    meta_roots = set(meta_df['root_id'])
    
    assert len(meta_roots.intersection(train_roots)) == 0, "Leakage: root_id in TRAIN"
    assert len(meta_roots.intersection(val_roots)) == 0, "Leakage: root_id in VALIDATION"
    print("Pass: Zero conversational root_id leakage into TRAIN or VALIDATION.")
    
    # Assert no duplicate target tweet IDs
    assert len(meta_df['tweet_id'].unique()) == 200, "Duplicate target tweet IDs found"
    print("Pass: All target tweet IDs are unique.")
    
    # Assert weak labels are absent from human CSV
    for col in anno_df.columns:
        assert 'weak_label' not in col, "Weak label leaked into annotation CSV header"
    
    print("Pass: Weak label column excluded from human annotation file.")
    
    # Verify no response in context
    for idx, row in meta_df.iterrows():
        tweet_id = row['tweet_id']
        anno_row = anno_df[anno_df['golden_id'] == row['golden_id']].iloc[0]
        
        # Are there any brand responses in the dataset that reply to this tweet?
        responses = twcs_df[(twcs_df['in_response_to_tweet_id'] == tweet_id) & (twcs_df['author_id'] == 'AmazonHelp')]
        if not responses.empty:
            response_texts = responses['text'].tolist()
            # Ensure none of these texts are in the context
            context_str = str(anno_row['conversation_context'])
            for r_text in response_texts:
                assert r_text not in context_str, f"Leakage: Brand response '{r_text}' found in context!"
                
        # Also ensure no model predictions or generated replies
        assert 'evidence_used' not in context_str, "Model artifact found in context"
        
    print("Pass: No target responses or future messages included in context.")
    print("Pass: No model predictions or retrieval evidence included.")
    
    print("\nAUDIT SUCCESSFUL. Golden Set is clean and ready for annotation.")

if __name__ == "__main__":
    main()
