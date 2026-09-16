import pytest
import pandas as pd
import json
import os
from unittest.mock import patch, MagicMock

from src.evaluation.human_judge_agreement import calculate_cohen_kappa, calculate_weighted_kappa, check_human_ratings_available
from src.evaluation.llm_judge import LLMJudge
from src.evaluation.failure_analysis import generate_failure_analysis

def test_kappa_calculations():
    # Perfect agreement
    h = [1, 2, 3, 4, 5]
    j = [1, 2, 3, 4, 5]
    assert calculate_cohen_kappa(h, j) == 1.0
    assert calculate_weighted_kappa(h, j) == 1.0
    
    # Complete disagreement
    h = [1, 1]
    j = [5, 5]
    # In complete disagreement, the score is often negative or 0 depending on chance agreement
    cohen = calculate_cohen_kappa(h, j)
    weighted = calculate_weighted_kappa(h, j)
    assert cohen <= 0.0
    assert weighted <= 0.0

def test_check_human_ratings():
    # Missing column
    df1 = pd.DataFrame({"human_intent": ["DeliveryStatus"]})
    avail1, msg1 = check_human_ratings_available(df1)
    assert not avail1
    
    # Empty column
    df2 = pd.DataFrame({"human_reply_quality": [pd.NA, pd.NA]})
    avail2, msg2 = check_human_ratings_available(df2)
    assert not avail2

def test_llm_judge_offline():
    judge = LLMJudge(mock_mode=True)
    res = judge.evaluate_reply("Where is it", "It is on the way", "Root ID 123")
    
    assert res["relevance"] == 4
    assert res["pass"] is True
    assert "overall_score" in res

def test_failure_analysis_generation(tmp_path):
    results = [
        {
            "golden_id": "G-1",
            "customer_message": "Hello",
            "true_intent": "DeliveryStatus",
            "pred_intent": "AccountAndPayment",
            "true_escalation": "AUTO-HANDLE",
            "pred_escalation": "ESCALATE",
            "generated_reply": "I don't know",
            "judge_scores": {
                "overall_score": 2.0,
                "safety": 3,
                "relevance": 1,
                "rationale": "Poor reply"
            }
        }
    ]
    
    out_path = tmp_path / "failure_analysis.md"
    metrics = generate_failure_analysis(results, str(out_path))
    
    assert metrics["intent_failures"] == 1
    assert metrics["escalation_failures"] == 1
    assert metrics["low_judge_scores"] == 1
    
    assert out_path.exists()
    content = out_path.read_text(encoding="utf-8")
    assert "G-1" in content
    assert "DeliveryStatus" in content
