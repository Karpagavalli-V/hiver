import os
import sys
import pandas as pd

CSV_PATH = "data/human_judge/human_judge_20.csv"

def print_header(title: str):
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)

def prompt_score(dimension_name: str, current_val: str) -> int:
    while True:
        prompt_text = f"Rate {dimension_name} (1-5)"
        if current_val and current_val != "nan":
            prompt_text += f" [Current: {current_val}]"
        prompt_text += ": "
        
        user_input = input(prompt_text).strip()
        if not user_input and current_val and current_val != "nan":
            try:
                return int(float(current_val))
            except ValueError:
                pass
                
        try:
            val = int(user_input)
            if 1 <= val <= 5:
                return val
            print("Score must be an integer between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

def main():
    if not os.path.exists(CSV_PATH):
        print(f"Error: {CSV_PATH} not found. Please run scripts/sample_human_judge_20.py first.")
        sys.exit(1)

    df = pd.read_csv(CSV_PATH, dtype=str)
    total_rows = len(df)

    # Detect the first unrated example to resume automatically
    rating_cols = ["human_relevance", "human_groundedness", "human_helpfulness", "human_safety", "human_tone"]
    current_idx = total_rows
    for idx in range(total_rows):
        row = df.iloc[idx]
        is_complete = all(
            str(row.get(col, "")).strip() not in ("", "nan", "None")
            for col in rating_cols
        )
        if not is_complete:
            current_idx = idx
            break

    print_header("HUMAN-AS-A-JUDGE RATING WORKFLOW (20 EXAMPLES)")
    print("Commands at rating prompt:")
    print("  - Enter 1-5 for each rating dimension")
    print("  - Type 'p' or 'prev' to go back to the previous example")
    print("  - Type 'q' or 'quit' at any prompt to save and exit")
    print("-" * 80)

    while 0 <= current_idx < total_rows:
        row = df.iloc[current_idx]
        gid = row.get("golden_id", "")
        customer_msg = row.get("customer_message", "")
        reply = row.get("generated_reply", "")
        pred_intent = row.get("predicted_intent", "")
        pred_esc = row.get("predicted_escalation", "")
        evidence = row.get("retrieved_evidence_summary", "")

        print_header(f"EXAMPLE {current_idx + 1} OF {total_rows} [Golden ID: {gid}]")
        print(f"CUSTOMER MESSAGE:\n  {customer_msg}\n")
        print(f"PREDICTED INTENT:     {pred_intent}")
        print(f"PREDICTED ESCALATION: {pred_esc}\n")
        print(f"HISTORICAL EVIDENCE:\n  {evidence[:300]}...\n" if len(evidence) > 300 else f"HISTORICAL EVIDENCE:\n  {evidence}\n")
        print(f"AI-GENERATED REPLY:\n  {reply}\n")
        print("-" * 80)
        print("Provide your independent ratings (1-5 scale, 1=Poor, 5=Excellent):\n")

        # Relevance
        rel_str = str(row.get("human_relevance", ""))
        rel_input = input(f"1. RELEVANCE (1-5) [Addresses customer issue?] {f'[Current: {rel_str}]' if rel_str and rel_str!='nan' else ''}: ").strip().lower()
        if rel_input in ['q', 'quit']:
            df.to_csv(CSV_PATH, index=False)
            print("\nProgress saved. Exiting annotation session.")
            return
        if rel_input in ['p', 'prev'] and current_idx > 0:
            current_idx -= 1
            continue
            
        try:
            rel = int(rel_input) if rel_input else (int(float(rel_str)) if rel_str and rel_str!='nan' else None)
        except ValueError:
            rel = None

        if rel is None or not (1 <= rel <= 5):
            print("Invalid rating. Retry example.")
            continue

        # Groundedness
        gnd_str = str(row.get("human_groundedness", ""))
        gnd_input = input(f"2. GROUNDEDNESS (1-5) [Supported by evidence?] {f'[Current: {gnd_str}]' if gnd_str and gnd_str!='nan' else ''}: ").strip().lower()
        try:
            gnd = int(gnd_input) if gnd_input else (int(float(gnd_str)) if gnd_str and gnd_str!='nan' else None)
        except ValueError:
            gnd = None

        if gnd is None or not (1 <= gnd <= 5):
            print("Invalid rating. Retry example.")
            continue

        # Helpfulness
        hlp_str = str(row.get("human_helpfulness", ""))
        hlp_input = input(f"3. HELPFULNESS (1-5) [Useful response/next step?] {f'[Current: {hlp_str}]' if hlp_str and hlp_str!='nan' else ''}: ").strip().lower()
        try:
            hlp = int(hlp_input) if hlp_input else (int(float(hlp_str)) if hlp_str and hlp_str!='nan' else None)
        except ValueError:
            hlp = None

        if hlp is None or not (1 <= hlp <= 5):
            print("Invalid rating. Retry example.")
            continue

        # Safety
        sft_str = str(row.get("human_safety", ""))
        sft_input = input(f"4. SAFETY (1-5) [No risk/unsupported claims?] {f'[Current: {sft_str}]' if sft_str and sft_str!='nan' else ''}: ").strip().lower()
        try:
            sft = int(sft_input) if sft_input else (int(float(sft_str)) if sft_str and sft_str!='nan' else None)
        except ValueError:
            sft = None

        if sft is None or not (1 <= sft <= 5):
            print("Invalid rating. Retry example.")
            continue

        # Tone
        tne_str = str(row.get("human_tone", ""))
        tne_input = input(f"5. TONE (1-5) [Professional & concise?] {f'[Current: {tne_str}]' if tne_str and tne_str!='nan' else ''}: ").strip().lower()
        try:
            tne = int(tne_input) if tne_input else (int(float(tne_str)) if tne_str and tne_str!='nan' else None)
        except ValueError:
            tne = None

        if tne is None or not (1 <= tne <= 5):
            print("Invalid rating. Retry example.")
            continue

        # Notes
        notes_str = str(row.get("human_notes", ""))
        notes_input = input(f"Notes (Optional) {f'[Current: {notes_str}]' if notes_str and notes_str!='nan' else ''}: ").strip()
        notes = notes_input if notes_input else (notes_str if notes_str and notes_str!='nan' else "")

        # Update dataframe
        df.at[current_idx, "human_relevance"] = str(rel)
        df.at[current_idx, "human_groundedness"] = str(gnd)
        df.at[current_idx, "human_helpfulness"] = str(hlp)
        df.at[current_idx, "human_safety"] = str(sft)
        df.at[current_idx, "human_tone"] = str(tne)
        df.at[current_idx, "human_notes"] = notes

        # Save progress
        df.to_csv(CSV_PATH, index=False)
        print(f"Saved rating for {gid}.")
        current_idx += 1

    print_header("ALL 20 EXAMPLES RATED SUCCESSFULLY!")
    print(f"Ratings saved to {CSV_PATH}.")
    print("Next step: Run 'python scripts/validate_human_judge_20.py'")

if __name__ == "__main__":
    main()
