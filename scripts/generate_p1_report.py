import pandas as pd
import json
import os
import sys

# Import priority logic
sys.path.append(os.path.join(os.path.dirname(__file__)))
from ai_review_queue import determine_priority

def main():
    df = pd.read_csv("data/golden_set/golden_set_ai_reviewed.csv")
    
    p1_rows = []
    
    for idx, row in df.iterrows():
        p, reasons = determine_priority(row)
        if p == 1:
            p1_rows.append((row, reasons))
            
    print(f"Total P1 rows found: {len(p1_rows)}")
    
    out_file = "reports/golden_set_p1_review.md"
    
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# Golden Set P1 Review Queue\n\n")
        f.write(f"Total Examples: {len(p1_rows)}\n\n")
        
        for row, reasons in p1_rows:
            f.write(f"## {row['golden_id']}\n\n")
            f.write(f"**P1 Reasons/Flags**: {', '.join(reasons)}\n\n")
            
            f.write("### Content\n")
            f.write(f"**Customer Message**:\n```\n{row['customer_message']}\n```\n\n")
            f.write(f"**Conversation Context**:\n```\n{row['conversation_context']}\n```\n\n")
            
            f.write("### AI-Assisted Annotations\n")
            f.write(f"- **Intent**: {row['human_intent']}\n")
            f.write(f"- **Auto-Handle Decision**: {row['human_auto_handle']}\n")
            f.write(f"- **Reason**: {row['human_intent_notes']}\n")
            f.write(f"- **Reply Quality**: {row['human_reply_quality']}\n")
            f.write(f"- **Confidence**: {row['human_intent_confidence']}\n")
            f.write(f"- **Uncertainty Flags**: {row['ai_uncertainty_flags']}\n\n")
            f.write("---\n\n")
            
    print(f"Created {out_file} with exactly {len(p1_rows)} examples.")

if __name__ == "__main__":
    main()
