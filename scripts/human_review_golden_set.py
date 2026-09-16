import pandas as pd
import os
import sys

ALLOWED_INTENTS = [
    "DeliveryStatus",
    "RefundsAndReturns",
    "DamagedOrDefective",
    "WrongItem",
    "CourierFeedback",
    "AccountAndPayment",
    "DigitalServices",
    "CustomerServiceEscalation",
    "OTHER"
]

ALLOWED_ESCALATION = ["AUTO-HANDLE", "ESCALATE"]

def update_progress_report(df):
    report_path = "reports/golden_set_human_review_progress.md"
    total = len(df)
    verified = len(df[df['human_verified_status'] == 'HUMAN_VERIFIED'])
    ai_assisted = len(df[df['human_verified_status'] == 'AI_ASSISTED_ONLY'])
    remaining = total - verified
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Golden Set Human Review Progress\n\n")
        f.write(f"- Total Examples: {total}\n")
        f.write(f"- Human Verified (`HUMAN_VERIFIED`): {verified}\n")
        f.write(f"- AI-Assisted Remaining (`AI_ASSISTED_ONLY`): {ai_assisted}\n\n")
        
        f.write("### Intent Distribution (Verified Only)\n")
        verified_df = df[df['human_verified_status'] == 'HUMAN_VERIFIED']
        for k, v in verified_df['human_intent'].value_counts().items():
            f.write(f"- {k}: {v}\n")
            
        f.write("\n### Escalation Decisions (Verified Only)\n")
        for k, v in verified_df['human_auto_handle'].value_counts().items():
            f.write(f"- {k}: {v}\n")

def initialize_dataset():
    output_file = "data/golden_set/golden_set_final.csv"
    input_file = "data/golden_set/golden_set_human_reviewed.csv"
    
    if os.path.exists(output_file):
        df = pd.read_csv(output_file)
    else:
        df = pd.read_csv(input_file)
        if 'human_verified_status' not in df.columns:
            df['human_verified_status'] = "UNREVIEWED"
        df.to_csv(output_file, index=False)
    
    return output_file, df

def get_valid_input(prompt_text, valid_options):
    while True:
        val = input(prompt_text).strip()
        if val in valid_options:
            return val
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

def select_intent(current_intent):
    print("\nAllowed Intents:")
    for i, intent in enumerate(ALLOWED_INTENTS, 1):
        print(f"{i}. {intent}")
    while True:
        try:
            choice = input(f"Select intent [1-{len(ALLOWED_INTENTS)}] (Current: {current_intent}): ").strip()
            idx = int(choice) - 1
            if 0 <= idx < len(ALLOWED_INTENTS):
                return ALLOWED_INTENTS[idx]
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a number.")

def select_escalation(current_esc):
    print("\nAllowed Escalations:")
    for i, esc in enumerate(ALLOWED_ESCALATION, 1):
        print(f"{i}. {esc}")
    while True:
        try:
            choice = input(f"Select escalation [1-{len(ALLOWED_ESCALATION)}] (Current: {current_esc}): ").strip()
            idx = int(choice) - 1
            if 0 <= idx < len(ALLOWED_ESCALATION):
                return ALLOWED_ESCALATION[idx]
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a number.")

def review_loop():
    output_file, df = initialize_dataset()
    
    # Find first unreviewed or AI_ASSISTED_ONLY row
    start_idx = len(df)
    for idx, row in df.iterrows():
        if row.get('human_verified_status') != 'HUMAN_VERIFIED':
            start_idx = idx
            break
            
    idx = start_idx
    if idx >= len(df):
        print("\nAll 200 Golden Set examples are already marked as HUMAN_VERIFIED!")
        return

    while idx < len(df):
        row = df.iloc[idx]
        
        print("\n" + "="*60)
        print(f"REVIEWING: {row['golden_id']} ({idx+1}/{len(df)})")
        print("="*60)
        print(f"\nCUSTOMER MESSAGE:\n{row['customer_message']}\n")
        print(f"CONVERSATION CONTEXT:\n{row.get('conversation_context', 'None')}\n")
        
        print("-" * 60)
        print(f"PROVENANCE STATUS: {row.get('human_verified_status', 'AI_ASSISTED_ONLY')}")
        print(f"Current Intent: {row['human_intent']}")
        print(f"Current Escalation: {row['human_auto_handle']}")
        print(f"AI Reasoning / Notes: {row.get('human_intent_notes', row.get('human_review_notes', 'None'))}")
        print("-" * 60)
        
        while True:
            print("\nOptions:")
            print("[S] Save and mark as HUMAN_VERIFIED")
            print("[I] Change Intent")
            print("[E] Change Escalation")
            print("[N] Edit Human Notes")
            print("[P] Previous example")
            print("[Q] Quit and resume later")
            
            choice = input("Enter choice: ").strip().upper()
            
            if choice == 'S':
                df.at[idx, 'human_verified_status'] = 'HUMAN_VERIFIED'
                df.at[idx, 'review_status'] = 'HUMAN_VERIFIED'
                df.to_csv(output_file, index=False)
                update_progress_report(df)
                print(f"✓ Saved {row['golden_id']} as HUMAN_VERIFIED.")
                
                # Advance to next non-HUMAN_VERIFIED example
                next_idx = idx + 1
                while next_idx < len(df) and df.at[next_idx, 'human_verified_status'] == 'HUMAN_VERIFIED':
                    next_idx += 1
                idx = next_idx
                break
            elif choice == 'I':
                new_intent = select_intent(df.at[idx, 'human_intent'])
                df.at[idx, 'human_intent'] = new_intent
                print(f"Intent updated to: {new_intent}")
            elif choice == 'E':
                new_esc = select_escalation(df.at[idx, 'human_auto_handle'])
                df.at[idx, 'human_auto_handle'] = new_esc
                print(f"Escalation updated to: {new_esc}")
            elif choice == 'N':
                current_notes = df.at[idx, 'human_review_notes']
                print(f"Current Notes: {current_notes}")
                new_notes = input("Enter new notes: ").strip()
                df.at[idx, 'human_review_notes'] = new_notes
            elif choice == 'P':
                if idx > 0:
                    idx -= 1
                else:
                    print("Already at the first example.")
                break
            elif choice == 'Q':
                df.to_csv(output_file, index=False)
                update_progress_report(df)
                print("Progress saved. Quitting.")
                sys.exit(0)
            else:
                print("Invalid choice. Try again.")
                
    print("\nAll 200 Golden Set examples have been reviewed and verified!")
    
if __name__ == '__main__':
    review_loop()
