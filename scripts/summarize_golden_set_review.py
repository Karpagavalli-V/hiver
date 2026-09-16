import os
import pandas as pd

REVIEWED_FILE = "data/golden_set/golden_set_human_reviewed.csv"
ORIGINAL_FILE = "data/golden_set/golden_set_annotation.csv"

def main():
    if not os.path.exists(REVIEWED_FILE):
        print(f"Error: {REVIEWED_FILE} does not exist yet. Please start the review process first.")
        return

    rev_df = pd.read_csv(REVIEWED_FILE)
    orig_df = pd.read_csv(ORIGINAL_FILE)
    
    total = len(rev_df)
    unreviewed = len(rev_df[rev_df['review_status'] == 'UNREVIEWED'])
    reviewed = total - unreviewed
    confirmed = len(rev_df[rev_df['review_status'] == 'REVIEWED_CONFIRMED'])
    corrected = len(rev_df[rev_df['review_status'] == 'REVIEWED_CORRECTED'])
    
    print("=" * 60)
    print("GOLDEN SET HUMAN REVIEW SUMMARY")
    print("=" * 60)
    print(f"Total Examples: {total}")
    print(f"Reviewed: {reviewed}")
    print(f"Unreviewed: {unreviewed}")
    print("-" * 60)
    print(f"Confirmed (No Changes): {confirmed}")
    print(f"Corrected (Changes Made): {corrected}")
    
    if corrected > 0:
        print("\nBREAKDOWN OF CORRECTIONS:")
        
        # We need to compare rev_df vs orig_df to see what changed
        # We assume golden_ids match exactly in order
        intent_changes = 0
        auto_changes = 0
        qual_changes = 0
        
        for idx, rev_row in rev_df.iterrows():
            if rev_row['review_status'] == 'REVIEWED_CORRECTED':
                orig_row = orig_df[orig_df['golden_id'] == rev_row['golden_id']].iloc[0]
                
                if str(rev_row['human_intent']) != str(orig_row['human_intent']):
                    intent_changes += 1
                if str(rev_row['human_auto_handle']) != str(orig_row['human_auto_handle']):
                    auto_changes += 1
                if str(rev_row['human_reply_quality']) != str(orig_row['human_reply_quality']):
                    qual_changes += 1
                    
        print(f"  - Intent Corrections: {intent_changes}")
        print(f"  - Auto-Handle Corrections: {auto_changes}")
        print(f"  - Reply Quality Corrections: {qual_changes}")
        
    print("=" * 60)

if __name__ == "__main__":
    main()
