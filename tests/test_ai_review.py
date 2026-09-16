import os
import pandas as pd
import pytest

ORIGINAL_FILE = "data/golden_set/golden_set_annotation.csv"
REVIEWED_FILE = "data/golden_set/golden_set_ai_reviewed.csv"

def test_original_file_preservation():
    assert os.path.exists(ORIGINAL_FILE), "Original Golden Set file is missing!"
    df = pd.read_csv(ORIGINAL_FILE)
    assert len(df) == 200, "Original Golden Set does not have exactly 200 rows."
    assert 'ai_uncertainty_flags' not in df.columns, "Original file was polluted with AI review fields."
    
def test_ai_reviewed_file_integrity():
    if not os.path.exists(REVIEWED_FILE):
        pytest.skip("AI Reviewed file does not exist yet.")
        
    orig_df = pd.read_csv(ORIGINAL_FILE)
    rev_df = pd.read_csv(REVIEWED_FILE)
    
    # Exactly 200 rows
    assert len(rev_df) == 200, "AI reviewed file does not have exactly 200 rows."
    
    # No duplicate golden_id
    assert len(rev_df['golden_id'].unique()) == 200, "Duplicate golden_ids found in AI reviewed file."
    
    # No missing required fields
    required_fields = ['human_intent', 'human_auto_handle', 'human_intent_notes', 'human_reply_quality', 'human_intent_confidence', 'ai_uncertainty_flags']
    for f in required_fields:
        assert f in rev_df.columns, f"{f} missing from AI reviewed file"
        
    # Schema checks
    valid_intents = {"DeliveryStatus", "RefundsAndReturns", "DamagedOrDefective", "WrongItem", "CourierFeedback", "AccountAndPayment", "DigitalServices", "CustomerServiceEscalation", "OTHER"}
    assert set(rev_df['human_intent'].unique()).issubset(valid_intents), "Invalid AI-generated intent."
    
    assert set(rev_df['human_auto_handle'].unique()).issubset({"AUTO-HANDLE", "ESCALATE"}), "Invalid AI-generated auto_handle."
    
    assert set(rev_df['human_intent_confidence'].unique()).issubset({"LOW", "MEDIUM", "HIGH"}), "Invalid AI-generated confidence."
    
    # Golden IDs match original
    assert set(orig_df['golden_id']) == set(rev_df['golden_id']), "Golden IDs do not match."
    
    # Customer messages and contexts strictly untouched
    for idx, row in rev_df.iterrows():
        orig_row = orig_df[orig_df['golden_id'] == row['golden_id']].iloc[0]
        assert row['customer_message'] == orig_row['customer_message'], "Customer message was modified!"
        assert str(row['conversation_context']) == str(orig_row['conversation_context']), "Conversation context was modified!"
