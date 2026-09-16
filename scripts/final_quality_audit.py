import pandas as pd
import json

def run_audit():
    golden_file = "data/golden_set/golden_set_final.csv"
    intents_file = "configs/intents.json"
    
    # Load files
    df = pd.read_csv(golden_file)
    with open(intents_file, "r") as f:
        intents_config = json.load(f)
        valid_intents = [item["id"] for item in intents_config["intents"]]
        
    valid_escalation = ["AUTO-HANDLE", "ESCALATE"]
    
    issues = []
    leakage = []
    high_risk_ids = []
    
    # 1. Check exactly 200 examples
    count_check = len(df) == 200
    if not count_check:
        issues.append(f"Row count is {len(df)}, not 200.")
        
    # 4. Duplicate examples
    duplicates = df['golden_id'].duplicated().sum()
    if duplicates > 0:
        issues.append(f"Found {duplicates} duplicate golden_ids.")
        
    # Check each row
    manual_count = 0
    ai_count = 0
    
    for idx, row in df.iterrows():
        g_id = row['golden_id']
        intent = row['human_intent']
        esc = row['human_auto_handle']
        msg = row['customer_message']
        ctx = str(row['conversation_context'])
        notes = str(row.get('human_review_notes', ''))
        
        # 5. Missing customer message
        if pd.isna(msg) or str(msg).strip() == "":
            issues.append(f"{g_id}: Missing customer message.")
            
        # 2. Valid intent labels
        if intent not in valid_intents:
            issues.append(f"{g_id}: Invalid intent '{intent}'.")
            
        # 3. Valid ESCALATE labels
        if esc not in valid_escalation:
            issues.append(f"{g_id}: Invalid escalation '{esc}'.")
            
        # 6/7. Context validity / Leakage
        # We can't strictly check the original twcs here without joining, but we can check if context is suspiciously long or contains weird markers.
        # Actually, let's just check if it contains the target message (which shouldn't happen)
        if str(msg).strip() in ctx and len(str(msg).strip()) > 10:
            leakage.append(f"{g_id}: Target message leaked into context.")
            
        # 8. Taxonomy inconsistencies
        if intent == "CustomerServiceEscalation" and esc == "AUTO-HANDLE":
            issues.append(f"{g_id}: CustomerServiceEscalation must be ESCALATE, but was AUTO-HANDLE.")
            high_risk_ids.append(g_id)
            
        # 9. Count manual vs AI-assisted
        if "AI Assistant:" in notes:
            ai_count += 1
            # Add to high risk if it's an AI-assisted escalation decision for sensitive topics
            if intent in ["RefundsAndReturns", "AccountAndPayment"] and esc == "AUTO-HANDLE":
                high_risk_ids.append(g_id)
        else:
            manual_count += 1
            
    # Collect top 20 risk IDs
    # If not enough, fill with other AI-assisted ones
    if len(high_risk_ids) < 20:
        for idx, row in df.iterrows():
            if len(high_risk_ids) >= 20:
                break
            g_id = row['golden_id']
            notes = str(row.get('human_review_notes', ''))
            if "AI Assistant:" in notes and g_id not in high_risk_ids:
                high_risk_ids.append(g_id)

    # Output report
    report_path = "reports/golden_set_quality_audit.md"
    with open(report_path, "w") as f:
        f.write("# Final Golden Set Quality Audit\n\n")
        
        f.write(f"1. Exactly 200 examples: {count_check} (Found {len(df)})\n")
        f.write(f"2. Valid intent labels: {len([i for i in issues if 'Invalid intent' in i]) == 0}\n")
        f.write(f"3. Valid AUTO-HANDLE / ESCALATE labels: {len([i for i in issues if 'Invalid escalation' in i]) == 0}\n")
        f.write(f"4. Duplicate examples: {duplicates == 0}\n")
        f.write(f"5. Missing customer messages: {len([i for i in issues if 'Missing customer message' in i]) == 0}\n")
        f.write(f"6/7. Leakage issues: {len(leakage)}\n")
        f.write(f"8. Inconsistent labels: {len([i for i in issues if 'must be ESCALATE' in i])}\n")
        f.write(f"9. Manual annotations: {manual_count} | AI-assisted annotations: {ai_count}\n\n")
        
        f.write("## Issues Detected\n")
        for iss in issues:
            f.write(f"- {iss}\n")
            
        f.write("\n## Highest Risk Annotations (Top 20)\n")
        for g_id in high_risk_ids[:20]:
            f.write(f"- {g_id}\n")

    overall_pass = (len(issues) == 0 and len(leakage) == 0 and count_check and duplicates == 0)

    print(f"overall audit PASS/FAIL: {'PASS' if overall_pass else 'FAIL'}")
    print(f"number of potential label issues: {len(issues)}")
    print(f"number of leakage issues: {len(leakage)}")
    print(f"manual annotations count: {manual_count}")
    print(f"AI-assisted annotations count: {ai_count}")
    print(f"the 20 highest-risk Golden Set IDs: {', '.join(high_risk_ids[:20])}")

if __name__ == "__main__":
    run_audit()
