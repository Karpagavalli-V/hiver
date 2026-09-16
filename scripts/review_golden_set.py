import pandas as pd
import json
import os

def check_priorities(row):
    msg = str(row['customer_message']).lower()
    intent = row['human_intent']
    conf = row['human_intent_confidence']
    auto = row['human_auto_handle']
    
    qual = None
    try:
        qual = int(float(row['human_reply_quality']))
    except:
        pass
        
    ctx_str = str(row['conversation_context'])
    
    p1_flags = []
    p2_flags = []
    
    # Priority 1 Logic
    # Ambiguous intent
    if ("refund" in msg or "return" in msg) and ("damaged" in msg or "broken" in msg):
        p1_flags.append("Ambiguous intent between RefundsAndReturns and DamagedOrDefective")
    if ("track" in msg or "missing" in msg) and ("refund" in msg):
        p1_flags.append("Ambiguous intent between DeliveryStatus and RefundsAndReturns")
        
    # Security/account compromise
    sec_kw = ["hacked", "unauthorized", "password", "security", "locked", "stolen account"]
    if any(k in msg for k in sec_kw):
        p1_flags.append("Security/account compromise issue")
        
    # Financial/unauthorized payment
    fin_kw = ["charge", "fee", "bank", "credit card", "billed", "money", "paid"]
    if any(k in msg for k in fin_kw):
        p1_flags.append("Unauthorized financial/payment issue")
        
    # Legal, safety, injury, property-damage, or threat-of-legal-action cases
    leg_kw = ["lawyer", "police", "sue", "injury", "damage", "attorney", "court", "threat", "danger"]
    if any(k in msg for k in leg_kw):
        p1_flags.append("Legal/safety/injury/threat issue")
        
    # Explicit manager/human escalation or repeated unresolved support cases
    esc_kw = ["manager", "supervisor", "agent", "hold", "spoke to", "called", "representative"]
    if any(k in msg for k in esc_kw):
        p1_flags.append("Explicit manager/supervisor/human escalation or repeated unresolved support issue")
        
    # Potentially incorrect intent based on the customer message/context
    if intent == "DeliveryStatus" and "delivery" not in msg and "track" not in msg and "arrived" not in msg and "package" not in msg:
         if len(msg.split()) > 5:
             p1_flags.append("Potentially incorrect intent based on the customer message/context")
             
    # Potentially incorrect AUTO-HANDLE decision
    if auto == "AUTO-HANDLE" and (any(k in msg for k in sec_kw + leg_kw + esc_kw) or intent in ["AccountAndPayment", "CustomerServiceEscalation"]):
        p1_flags.append("Potentially incorrect AUTO-HANDLE decision")
        
    # Potentially incorrect ESCALATE decision
    if auto == "ESCALATE" and intent == "OTHER" and conf == "LOW":
        p1_flags.append("Potentially incorrect ESCALATE decision")
        
    # Reply quality score 1 or 2 where the historical reply may actually be useful
    if qual in [1, 2]:
        p1_flags.append("Reply quality score 1 or 2 where the historical reply may actually be useful")
        
    # Reply quality score 5 where the reply may not genuinely deserve a 5
    if qual == 5:
        p1_flags.append("Reply quality score 5 where the reply may not genuinely deserve a 5")
        
    # Missing/insufficient context that makes the proposed judgment unreliable
    if not ctx_str or ctx_str == "[]" or ctx_str.lower() in ["nan", "none"]:
        p1_flags.append("Missing/insufficient context that makes the proposed judgment unreliable")
        
        
    # Priority 2 Logic
    if conf == 'MEDIUM':
        p2_flags.append("MEDIUM confidence")
    if conf == 'LOW':
        p2_flags.append("LOW confidence")
    if intent == 'OTHER' and any(k in msg for k in ["issue", "help", "problem", "broken", "late", "where"]):
        p2_flags.append("OTHER where the message appears to contain an actual support issue")
        
    if p1_flags:
        return 1, p1_flags
    elif p2_flags:
        return 2, p2_flags
    else:
        return 3, []

def main():
    print("Loading Golden Set Annotations...")
    df = pd.read_csv("data/golden_set/golden_set_annotation.csv")
    
    p1_queue = []
    p2_queue = []
    p3_count = 0
    
    reason_counts = {}
    
    for idx, row in df.iterrows():
        priority, flags = check_priorities(row)
        
        for f in flags:
            reason_counts[f] = reason_counts.get(f, 0) + 1
            
        item = {
            'row': row,
            'flags': flags
        }
            
        if priority == 1:
            p1_queue.append(item)
        elif priority == 2:
            p2_queue.append(item)
        else:
            p3_count += 1
                
    # Generate Markdown Report
    os.makedirs("reports", exist_ok=True)
    report_path = "reports/golden_set_review_queue.md"
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Golden Set Review Queue\n\n")
        f.write("> **Methodology Note**: The labels present in the Golden Set currently represent AI-assisted pre-annotations. To maximize human review efficiency and evaluation validity, this queue specifically prioritizes cases where a human correction is most likely to affect the final benchmark accuracy (e.g., safety issues, ambiguous intents, unsupported automation routing). Straightforward cases require no manual review and are placed in Priority 3.\n\n")
        
        f.write("## Summary\n")
        f.write(f"- **Total Rows**: {len(df)}\n")
        f.write(f"- **Priority 1 (MUST REVIEW)**: {len(p1_queue)}\n")
        f.write(f"- **Priority 2 (REVIEW IF TIME)**: {len(p2_queue)}\n")
        f.write(f"- **Priority 3 (NO MANUAL REVIEW NEEDED)**: {p3_count}\n\n")
        
        f.write("### Counts by Review Reason\n")
        for reason, count in sorted(reason_counts.items(), key=lambda x: x[1], reverse=True):
            f.write(f"- {reason}: {count}\n")
            
        f.write("\n### Counts by Proposed Intent (Full Dataset)\n")
        for intent, count in df['human_intent'].value_counts().items():
            f.write(f"- {intent}: {count}\n")
            
        f.write("\n### Counts by Proposed AUTO-HANDLE/ESCALATE (Full Dataset)\n")
        for auto, count in df['human_auto_handle'].value_counts().items():
            f.write(f"- {auto}: {count}\n")
            
        f.write("\n### Counts by Proposed Reply Quality (Full Dataset)\n")
        for qual, count in df['human_reply_quality'].value_counts().items():
            f.write(f"- {int(qual)}: {count}\n")
            
        def write_queue(title, queue):
            f.write(f"\n## {title}\n\n")
            for item in queue:
                row = item['row']
                flags = item['flags']
                
                f.write(f"### {row['golden_id']}\n")
                f.write(f"**Customer Message**: `{row['customer_message']}`\n\n")
                
                # Format context safely
                ctx_str = ""
                try:
                    ctx_list = json.loads(row['conversation_context'])
                    if ctx_list:
                        ctx_str = "\\n".join([f"[{m.get('author', 'Unknown')}] {m.get('text', '')}" for m in ctx_list])
                    else:
                        ctx_str = "*Empty Context*"
                except:
                    ctx_str = "*Unparseable Context*"
                    
                f.write(f"**Context**:\n```text\n{ctx_str}\n```\n\n")
                f.write(f"- **Proposed Intent**: {row['human_intent']}\n")
                f.write(f"- **Proposed Confidence**: {row['human_intent_confidence']}\n")
                f.write(f"- **Proposed Resolution Support**: {row['human_resolution_supported']}\n")
                f.write(f"- **Proposed Auto-Handle**: {row['human_auto_handle']}\n")
                f.write(f"- **Proposed Reply Quality**: {int(float(row['human_reply_quality'])) if pd.notna(row['human_reply_quality']) else 'N/A'}\n")
                f.write(f"- **Reasons Flagged**:\n")
                for flg in flags:
                    f.write(f"  - {flg}\n")
                f.write("\n---\n\n")
                
        write_queue("Priority 1 — MUST REVIEW", p1_queue)
        write_queue("Priority 2 — REVIEW IF TIME", p2_queue)
            
    print(f"Generated review queue.")
    print(f"P1: {len(p1_queue)}")
    print(f"P2: {len(p2_queue)}")
    print(f"P3: {p3_count}")
    print(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
