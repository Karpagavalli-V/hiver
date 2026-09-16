import pandas as pd
import json
import sys

def main():
    print("Validating Golden Set Annotations...")
    df = pd.read_csv("data/golden_set/golden_set_annotation.csv")
    
    # Check 1: exactly 200 rows
    assert len(df) == 200, f"Expected 200 rows, got {len(df)}"
    print("Pass: Exactly 200 rows.")
    
    # Check 2: golden IDs G-1000 through G-1199 are present exactly once
    expected_ids = {f"G-{1000 + i}" for i in range(200)}
    actual_ids = set(df['golden_id'].tolist())
    assert expected_ids == actual_ids, "Missing or duplicate golden_ids."
    print("Pass: golden_ids G-1000 through G-1199 are present exactly once.")
    
    # Check 4: every human_intent is one of the 9 allowed values
    valid_intents = {"DeliveryStatus", "RefundsAndReturns", "DamagedOrDefective", "WrongItem", "CourierFeedback", "AccountAndPayment", "DigitalServices", "CustomerServiceEscalation", "OTHER"}
    invalid_intents = set(df['human_intent'].unique()) - valid_intents
    assert len(invalid_intents) == 0, f"Invalid intents found: {invalid_intents}"
    print("Pass: All intents are valid.")
    
    # Check 5: every confidence value is HIGH/MEDIUM/LOW
    valid_conf = {"HIGH", "MEDIUM", "LOW"}
    invalid_conf = set(df['human_intent_confidence'].unique()) - valid_conf
    assert len(invalid_conf) == 0, f"Invalid confidence found: {invalid_conf}"
    print("Pass: All confidences are valid.")
    
    # Check 6: every resolution value is YES/NO
    valid_res = {"YES", "NO"}
    invalid_res = set(df['human_resolution_supported'].unique()) - valid_res
    assert len(invalid_res) == 0, f"Invalid resolution found: {invalid_res}"
    print("Pass: All resolutions are valid.")
    
    # Check 7: every auto-handle value is AUTO-HANDLE/ESCALATE
    valid_auto = {"AUTO-HANDLE", "ESCALATE"}
    invalid_auto = set(df['human_auto_handle'].unique()) - valid_auto
    assert len(invalid_auto) == 0, f"Invalid auto-handle found: {invalid_auto}"
    print("Pass: All auto-handle values are valid.")
    
    # Check 8: every reply quality is an integer 1–5
    valid_qual = {1, 2, 3, 4, 5, 1.0, 2.0, 3.0, 4.0, 5.0} # handle potential float conversion
    invalid_qual = set(df['human_reply_quality'].unique()) - valid_qual
    assert len(invalid_qual) == 0, f"Invalid reply quality found: {invalid_qual}"
    print("Pass: All reply quality values are valid 1-5.")
    
    # Check 9: every annotation_complete is YES
    assert all(df['annotation_complete'] == "YES"), "Not all rows are marked YES"
    print("Pass: All rows marked complete.")
    
    # Check 10: no required human annotation cell is blank
    for col in df.columns:
        if "human_" in col or "annotation_" in col:
            assert df[col].notna().all(), f"Blank cell found in {col}"
    print("Pass: No blank cells in annotation columns.")
    
    print("\nALL VALIDATION CHECKS PASSED.")

if __name__ == "__main__":
    main()
