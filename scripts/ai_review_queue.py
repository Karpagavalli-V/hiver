import json
import pandas as pd
import os

def determine_priority(row):
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
    
    try:
        flags = json.loads(str(row['ai_uncertainty_flags']))
    except:
        flags = []
        
    p1_reasons = []
    p2_reasons = []
    
    # Priority 1: Security/financial, legal/safety, manager escalation
    sec_kw = ["hacked", "unauthorized", "password", "security", "locked", "stolen account", "charge", "fee", "bank", "credit card", "billed", "money", "paid"]
    leg_kw = ["lawyer", "police", "sue", "injury", "damage", "attorney", "court", "threat", "danger"]
    esc_kw = ["manager", "supervisor", "agent", "hold", "spoke to", "called", "representative"]
    
    if any(k in msg for k in sec_kw):
        p1_reasons.append("Security/account/financial compromise issue")
    if any(k in msg for k in leg_kw):
        p1_reasons.append("Legal/safety/injury/threat issue")
    if any(k in msg for k in esc_kw):
        p1_reasons.append("Explicit manager/human escalation request")
        
    # Ambiguous intent, low confidence, conflicting context, poor reply logic
    if conf == 'LOW':
        p1_reasons.append("Low confidence")
        
    if flags:
        # If AI found uncertainty
        p1_reasons.append(f"AI Uncertainty Flags: {', '.join(flags)}")
        
    # Missing context making judgment unreliable
    # Note: AI can handle empty context better, so maybe only P1 if AI had low confidence. But requirements say P1 for "missing/insufficient context that makes proposed judgement unreliable". We will link it to AI confidence.
    if (not ctx_str or ctx_str == "[]" or ctx_str.lower() in ["nan", "none"]) and (conf in ['LOW', 'MEDIUM']):
        p1_reasons.append("Missing/insufficient context")
        
    if auto == "AUTO-HANDLE" and intent in ["AccountAndPayment", "CustomerServiceEscalation"]:
        p1_reasons.append("Ambiguous AUTO-HANDLE vs ESCALATE (Auto-handling an escalation intent)")
        
    if qual in [1, 2, 5]:
        p1_reasons.append(f"Unclear or poor reply-quality judgment ({qual})")
        
    # Priority 2:
    if conf == 'MEDIUM':
        p2_reasons.append("Moderate uncertainty (MEDIUM confidence)")
        
    if p1_reasons:
        return 1, p1_reasons
    elif p2_reasons:
        return 2, p2_reasons
    else:
        return 3, []

def main():
    df = pd.read_csv("data/golden_set/golden_set_ai_reviewed.csv")
    
    p1_queue = []
    p2_queue = []
    p3_count = 0
    
    for idx, row in df.iterrows():
        p, reasons = determine_priority(row)
        if p == 1:
            p1_queue.append({'id': row['golden_id'], 'reasons': reasons})
        elif p == 2:
            p2_queue.append({'id': row['golden_id'], 'reasons': reasons})
        else:
            p3_count += 1
            
    print("AI Review Queue Generated:")
    print(f"P1 (Must Review): {len(p1_queue)}")
    print(f"P2 (Review If Time): {len(p2_queue)}")
    print(f"P3 (Clear): {p3_count}")

if __name__ == "__main__":
    main()
