import os
import sys
import json
import pandas as pd
from review_golden_set import check_priorities

ORIGINAL_FILE = "data/golden_set/golden_set_annotation.csv"
REVIEWED_FILE = "data/golden_set/golden_set_human_reviewed.csv"

def init_review_file():
    if not os.path.exists(REVIEWED_FILE):
        print(f"Creating new review file at {REVIEWED_FILE}...")
        df = pd.read_csv(ORIGINAL_FILE)
        df['review_status'] = 'UNREVIEWED'
        df['human_review_notes'] = ''
        df.to_csv(REVIEWED_FILE, index=False)
    else:
        print(f"Resuming review from {REVIEWED_FILE}...")

def format_context(ctx_str):
    try:
        ctx_list = json.loads(ctx_str)
        if ctx_list:
            return "\n".join([f"[{m.get('author', 'Unknown')}] {m.get('text', '')}" for m in ctx_list])
        return "*Empty Context*"
    except:
        return "*Unparseable Context*"

def prompt_override(field_name, current_val):
    print(f"{field_name} [AI PRE-ANNOTATION: {current_val}]")
    new_val = input("  Press Enter to confirm, or type new value: ").strip()
    return new_val if new_val else current_val

def prompt_quality(current_val):
    while True:
        print(f"Reply Quality (1-5) [AI PRE-ANNOTATION: {current_val}]")
        new_val = input("  Press Enter to confirm, or type new value (1, 2, 3, 4, 5): ").strip()
        
        val_to_check = new_val if new_val else str(current_val)
        
        # Extract just the integer part if it was a float string like "3.0"
        if val_to_check.endswith('.0'):
            val_to_check = val_to_check[:-2]
            
        if val_to_check in ['1', '2', '3', '4', '5']:
            return int(val_to_check)
        elif val_to_check in ["N/A", "nan", "NaN"]:
            return current_val
        else:
            print("  Invalid input. Please enter exactly 1, 2, 3, 4, or 5.")

def main():
    if not os.path.exists(ORIGINAL_FILE):
        print("Error: Original annotation file not found.")
        sys.exit(1)
        
    init_review_file()
    df = pd.read_csv(REVIEWED_FILE)
    
    # Cast to object to prevent any dtype assignment errors
    df['human_reply_quality'] = df['human_reply_quality'].astype('object')
    
    # Priority sorting
    # We want to iterate P1 -> P2 -> P3
    # We calculate priority for all rows to sort them
    
    print("Calculating review queue priorities...")
    priorities = []
    for _, row in df.iterrows():
        p, _ = check_priorities(row)
        priorities.append(p)
        
    df['temp_priority'] = priorities
    
    # Find unreviewed items
    unreviewed = df[df['review_status'] == 'UNREVIEWED'].sort_values(by='temp_priority')
    
    if len(unreviewed) == 0:
        print("\nAll 200 examples have been reviewed!")
        sys.exit(0)
        
    print(f"\nFound {len(unreviewed)} remaining unreviewed examples.")
    
    for idx, row in unreviewed.iterrows():
        print("\n" + "="*80)
        print(f"REVIEWING: {row['golden_id']} (Priority {row['temp_priority']})")
        print("="*80)
        print(f"\nCUSTOMER MESSAGE:\n{row['customer_message']}\n")
        print(f"CONVERSATION CONTEXT:\n{format_context(row['conversation_context'])}\n")
        print("-" * 80)
        print("PLEASE REVIEW AI PRE-ANNOTATIONS:\n")
        
        orig_intent = row['human_intent']
        orig_auto = row['human_auto_handle']
        orig_qual = row['human_reply_quality']
        orig_reason = row.get('human_intent_notes', '')
        
        new_intent = prompt_override("Intent", orig_intent)
        new_auto = prompt_override("Auto-Handle", orig_auto)
        
        # Reason (combining intent/resolution/auto-handle reasoning into one human review note if desired)
        new_reason = prompt_override("Reason/Notes", orig_reason)
        
        # Qual could be NaN
        qual_str = str(int(float(orig_qual))) if pd.notna(orig_qual) else "N/A"
        new_qual = prompt_quality(qual_str)
        
        new_review_notes = input("Any additional human review notes (optional): ").strip()
        
        # Determine status
        if new_intent == orig_intent and new_auto == orig_auto and str(new_qual) == qual_str:
            status = 'REVIEWED_CONFIRMED'
        else:
            status = 'REVIEWED_CORRECTED'
            
        # Save to DF
        df.at[idx, 'human_intent'] = new_intent
        df.at[idx, 'human_auto_handle'] = new_auto
        df.at[idx, 'human_intent_notes'] = new_reason # Override the pre-annotation notes
        df.at[idx, 'human_reply_quality'] = new_qual
        df.at[idx, 'human_review_notes'] = new_review_notes
        df.at[idx, 'review_status'] = status
        
        # Save file immediately
        df.drop(columns=['temp_priority']).to_csv(REVIEWED_FILE, index=False)
        
        print(f"\n--> Saved as {status}. Moving to next...")
        
        cont = input("\nContinue to next example? (Y/n): ").strip().lower()
        if cont == 'n':
            print("Exiting review tool. Progress saved.")
            break

if __name__ == "__main__":
    main()
