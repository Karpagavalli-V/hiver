import os
import pandas as pd
import pytest
from unittest.mock import patch
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../scripts'))
from human_review_tool import prompt_quality

ORIGINAL_FILE = "data/golden_set/golden_set_annotation.csv"
REVIEWED_FILE = "data/golden_set/golden_set_human_reviewed.csv"

def test_original_file_preservation():
    assert os.path.exists(ORIGINAL_FILE), "Original Golden Set file is missing!"
    df = pd.read_csv(ORIGINAL_FILE)
    assert len(df) == 200, "Original Golden Set does not have exactly 200 rows."
    assert 'review_status' not in df.columns, "Original file was polluted with review fields."

def test_prompt_quality_logic():
    # 1. Enter valid reply-quality value
    with patch('builtins.input', return_value='3'):
        assert prompt_quality('N/A') == 3
        
    with patch('builtins.input', return_value='5'):
        assert prompt_quality(3) == 5

    # 2. Press Enter to preserve existing integer value
    with patch('builtins.input', return_value=''):
        assert prompt_quality(4) == 4
        
    # 3. Handle float string format (just in case)
    with patch('builtins.input', return_value=''):
        assert prompt_quality('4.0') == 4

def test_reviewed_file_integrity():
    if not os.path.exists(REVIEWED_FILE):
        pytest.skip("Reviewed file does not exist yet.")
        
    orig_df = pd.read_csv(ORIGINAL_FILE)
    rev_df = pd.read_csv(REVIEWED_FILE)
    
    # 1. No rows lost
    assert len(rev_df) == 200, "Reviewed file lost rows!"
    
    # 2. No duplicate golden_id
    assert len(rev_df['golden_id'].unique()) == 200, "Duplicate golden_ids found in reviewed file."
    
    # 3. Required fields present
    assert 'review_status' in rev_df.columns, "review_status column missing."
    assert 'human_review_notes' in rev_df.columns, "human_review_notes column missing."
    
    # 4. Golden IDs strictly match original
    assert set(orig_df['golden_id']) == set(rev_df['golden_id']), "Golden IDs do not match between original and reviewed."
    
    # 5. Customer messages and contexts strictly untouched
    for idx, row in rev_df.iterrows():
        orig_row = orig_df[orig_df['golden_id'] == row['golden_id']].iloc[0]
        assert row['customer_message'] == orig_row['customer_message'], "Customer message was modified!"
        assert str(row['conversation_context']) == str(orig_row['conversation_context']), "Conversation context was modified!"
