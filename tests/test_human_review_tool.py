import pytest
import os
import pandas as pd
from unittest.mock import patch
import sys

# Add scripts to path to import the review tool
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from human_review_golden_set import review_loop, initialize_dataset, ALLOWED_INTENTS, ALLOWED_ESCALATION

@pytest.fixture
def clean_env():
    final_path = "data/golden_set/golden_set_final.csv"
    backup_path = "data/golden_set/golden_set_final.csv.bak"
    if os.path.exists(final_path):
        os.rename(final_path, backup_path)
    
    yield
    
    if os.path.exists(final_path):
        os.remove(final_path)
    if os.path.exists(backup_path):
        os.rename(backup_path, final_path)

def test_initialization(clean_env):
    output_file, df = initialize_dataset()
    assert os.path.exists(output_file)
    assert len(df) == 200
    assert 'human_verified_status' in df.columns
    assert all(df['human_verified_status'] == 'UNREVIEWED')
    
def test_unmodified_source_files(clean_env):
    source_path = "data/golden_set/golden_set_human_reviewed.csv"
    mtime_before = os.path.getmtime(source_path)
    
    initialize_dataset()
    
    mtime_after = os.path.getmtime(source_path)
    assert mtime_before == mtime_after

def test_save_and_resume_progress(clean_env):
    # Mock inputs: Save first item, then Quit
    with patch('builtins.input', side_effect=['S', 'Q']):
        try:
            review_loop()
        except SystemExit:
            pass
            
    df = pd.read_csv("data/golden_set/golden_set_final.csv")
    assert df.loc[0, 'human_verified_status'] == 'HUMAN_VERIFIED'
    assert df.loc[1, 'human_verified_status'] == 'UNREVIEWED'
    
    # Resume: should skip first item and start at second. We will just quit immediately.
    with patch('builtins.input', side_effect=['Q']):
        try:
            review_loop()
        except SystemExit:
            pass
            
    df2 = pd.read_csv("data/golden_set/golden_set_final.csv")
    assert df2.loc[0, 'human_verified_status'] == 'HUMAN_VERIFIED'
    
def test_data_integrity(clean_env):
    output_file, df = initialize_dataset()
    orig = pd.read_csv("data/golden_set/golden_set_annotation.csv")
    
    assert len(df) == 200
    assert list(df['golden_id']) == list(orig['golden_id'])
    assert list(df['customer_message']) == list(orig['customer_message'])
    
    assert set(df['human_intent'].dropna().unique()).issubset(set(ALLOWED_INTENTS + ['OTHER']))
    assert set(df['human_auto_handle'].dropna().unique()).issubset(set(ALLOWED_ESCALATION))

def test_edit_labels_and_save(clean_env):
    # Change intent to 1 (DeliveryStatus), change escalation to 2 (ESCALATE), edit notes, then Save, then Quit
    inputs = [
        'I', '1',  # Change intent -> DeliveryStatus
        'E', '2',  # Change escalation -> ESCALATE
        'N', 'Test note', # Edit notes
        'S',       # Save and next
        'Q'        # Quit
    ]
    with patch('builtins.input', side_effect=inputs):
        try:
            review_loop()
        except SystemExit:
            pass
            
    df = pd.read_csv("data/golden_set/golden_set_final.csv")
    assert df.loc[0, 'human_intent'] == 'DeliveryStatus'
    assert df.loc[0, 'human_auto_handle'] == 'ESCALATE'
    assert df.loc[0, 'human_review_notes'] == 'Test note'
    assert df.loc[0, 'human_verified_status'] == 'HUMAN_VERIFIED'
