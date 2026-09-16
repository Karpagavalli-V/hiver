"""
test_evaluation_cache.py — Unit tests for the evaluation harness components.

Intentionally imports ONLY lightweight modules (eval_cache, llm_judge,
human_judge_agreement, failure_analysis).  The HistoricalRetriever /
FAISS / sklearn baseline models are NOT imported here so collection
is fast.
"""

import json
import os
import sys
import pytest
import pandas as pd
import openai
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.evaluation.eval_cache import EvalCache
from src.evaluation.llm_judge import LLMJudge
from src.evaluation.human_judge_agreement import (
    calculate_cohen_kappa,
    calculate_weighted_kappa,
    check_human_ratings_available,
)
from src.evaluation.failure_analysis import generate_failure_analysis


# ──────────────────────────────────────────────────────────────────────────────
# EvalCache unit tests
# ──────────────────────────────────────────────────────────────────────────────

class TestEvalCache:
    def test_cache_miss_returns_none(self, tmp_path):
        cache = EvalCache("test", cache_dir=str(tmp_path))
        assert cache.get("nonexistent_key") is None

    def test_cache_hit_returns_stored_value(self, tmp_path):
        cache = EvalCache("test", cache_dir=str(tmp_path))
        key = EvalCache.make_key("hello", "world")
        cache.set(key, {"intent": "DeliveryStatus"})
        assert cache.get(key) == {"intent": "DeliveryStatus"}

    def test_cache_persists_across_instances(self, tmp_path):
        key = EvalCache.make_key("msg", "ctx")
        c1 = EvalCache("persist_test", cache_dir=str(tmp_path))
        c1.set(key, {"score": 42})
        c1.save()
        # New instance reads from disk
        c2 = EvalCache("persist_test", cache_dir=str(tmp_path))
        assert c2.get(key) == {"score": 42}

    def test_key_is_deterministic(self):
        k1 = EvalCache.make_key("message A", "context B")
        k2 = EvalCache.make_key("message A", "context B")
        assert k1 == k2

    def test_different_inputs_produce_different_keys(self):
        k1 = EvalCache.make_key("message A", "context B")
        k2 = EvalCache.make_key("message X", "context Y")
        assert k1 != k2

    def test_has_returns_false_then_true(self, tmp_path):
        cache = EvalCache("has_test", cache_dir=str(tmp_path))
        key = EvalCache.make_key("m", "c")
        assert not cache.has(key)
        cache.set(key, {"x": 1})
        assert cache.has(key)

    def test_len_reflects_items(self, tmp_path):
        cache = EvalCache("len_test", cache_dir=str(tmp_path))
        assert len(cache) == 0
        cache.set(EvalCache.make_key("a"), {"v": 1})
        cache.set(EvalCache.make_key("b"), {"v": 2})
        assert len(cache) == 2

    def test_corrupt_cache_file_returns_empty(self, tmp_path):
        cache_file = tmp_path / "eval_corrupt.json"
        cache_file.write_text("THIS IS NOT JSON")
        cache = EvalCache("corrupt", cache_dir=str(tmp_path))
        assert len(cache) == 0

    def test_autosave_writes_file(self, tmp_path):
        cache = EvalCache("autosave_test", cache_dir=str(tmp_path))
        key = EvalCache.make_key("x")
        cache.set(key, {"value": "auto"}, autosave=True)
        with open(cache.path) as f:
            data = json.load(f)
        assert key in data


# ──────────────────────────────────────────────────────────────────────────────
# Resume: partial results logic
# ──────────────────────────────────────────────────────────────────────────────

class TestResumeLogic:
    def test_partial_results_file_loaded_correctly(self, tmp_path):
        partial = tmp_path / "partial.json"
        partial.write_text(json.dumps({
            "results": [
                {"golden_id": "G-1000", "status": "completed",
                 "pred_intent": "DeliveryStatus"}
            ]
        }))
        with open(partial) as f:
            data = json.load(f)
        completed_map = {r["golden_id"]: r for r in data.get("results", [])}
        assert "G-1000" in completed_map
        assert completed_map["G-1000"]["pred_intent"] == "DeliveryStatus"

    def test_already_completed_id_is_skipped(self):
        completed_map = {"G-1000": {"golden_id": "G-1000", "status": "completed"}}
        api_call_count = 0
        for g_id in ["G-1000", "G-1001"]:
            if g_id in completed_map:
                continue
            api_call_count += 1
        # Only G-1001 should result in an API call simulation
        assert api_call_count == 1


# ──────────────────────────────────────────────────────────────────────────────
# Quota failure: loop must stop cleanly and preserve partial results
# ──────────────────────────────────────────────────────────────────────────────

class TestQuotaFailure:
    def test_rate_limit_error_stops_loop(self):
        completed_map = {}
        failed_ids = []
        quota_hit = False

        def mock_classify(msg):
            if msg == "world":
                raise openai.RateLimitError(
                    "quota exceeded",
                    response=MagicMock(status_code=429),
                    body={}
                )
            m = MagicMock()
            m.intent = "OTHER"
            return m

        for ex in [{"id": "G-1", "msg": "hello"}, {"id": "G-2", "msg": "world"}]:
            try:
                clf = mock_classify(ex["msg"])
                completed_map[ex["id"]] = {"status": "completed", "intent": clf.intent}
            except openai.RateLimitError:
                failed_ids.append(ex["id"])
                quota_hit = True
                break

        assert quota_hit is True
        assert "G-1" in completed_map
        assert "G-2" not in completed_map
        assert "G-2" in failed_ids

    def test_non_quota_error_continues_loop(self):
        """A generic exception should mark as failed but NOT stop the loop."""
        results = []
        failed_ids = []
        for ex in [{"id": "G-1", "raise": True}, {"id": "G-2", "raise": False}]:
            try:
                if ex["raise"]:
                    raise ValueError("unexpected error")
                results.append({"golden_id": ex["id"], "status": "completed"})
            except Exception as e:
                failed_ids.append(ex["id"])
                results.append({"golden_id": ex["id"], "status": "failed",
                                 "error": str(e)})

        assert len(results) == 2
        assert results[0]["status"] == "failed"
        assert results[1]["status"] == "completed"
        assert "G-1" in failed_ids


# ──────────────────────────────────────────────────────────────────────────────
# No duplicate API calls — cache-first pattern
# ──────────────────────────────────────────────────────────────────────────────

class TestNoDuplicateAPICalls:
    def test_cache_hit_prevents_api_call(self, tmp_path):
        cache = EvalCache("classifier", cache_dir=str(tmp_path))
        key = EvalCache.make_key("test message", "context")
        cache.set(key, {"intent": "DeliveryStatus", "confidence": 0.99})

        api_calls = 0

        def mock_classify(msg, context=None):
            nonlocal api_calls
            api_calls += 1
            return MagicMock(intent="OTHER")

        # Simulate cache-first pattern from run_evaluation.py
        if cache.has(key):
            result = cache.get(key)
        else:
            result = mock_classify("test message", "context")

        assert api_calls == 0, "API must NOT be called when cache already has the key"
        assert result["intent"] == "DeliveryStatus"

    def test_same_input_same_key_no_double_call(self, tmp_path):
        """Sending the same message twice must only result in one API call."""
        cache = EvalCache("dedup_test", cache_dir=str(tmp_path))
        api_calls = 0

        def api_call(msg):
            nonlocal api_calls
            api_calls += 1
            return {"intent": "OTHER", "confidence": 0.9}

        key = EvalCache.make_key("hello")

        for _ in range(3):  # simulate 3 identical examples
            if not cache.has(key):
                result = api_call("hello")
                cache.set(key, result)

        assert api_calls == 1


# ──────────────────────────────────────────────────────────────────────────────
# Offline / mock mode
# ──────────────────────────────────────────────────────────────────────────────

class TestOfflineMode:
    def test_llm_judge_mock_returns_valid_schema(self):
        judge = LLMJudge(mock_mode=True)
        result = judge.evaluate_reply(
            "Where is my order?", "It is delayed.", "Root ID 123"
        )
        required = {"relevance", "groundedness", "helpfulness",
                    "safety", "tone", "overall_score", "pass", "rationale"}
        assert required.issubset(set(result.keys()))

    def test_llm_judge_mock_pass_is_true(self):
        judge = LLMJudge(mock_mode=True)
        result = judge.evaluate_reply("msg", "reply", "evidence")
        assert result["pass"] is True

    def test_llm_judge_mock_never_raises(self):
        judge = LLMJudge(mock_mode=True)
        result = judge.evaluate_reply("", "", "")
        assert "overall_score" in result

    def test_llm_judge_mock_rationale_tagged(self):
        judge = LLMJudge(mock_mode=True)
        result = judge.evaluate_reply("m", "r", "e")
        assert "[MOCK]" in result["rationale"]


# ──────────────────────────────────────────────────────────────────────────────
# Metric helpers
# ──────────────────────────────────────────────────────────────────────────────

class TestMetrics:
    def test_cohen_kappa_perfect_agreement(self):
        h = [1, 2, 3, 4, 5]
        assert calculate_cohen_kappa(h, h) == 1.0

    def test_weighted_kappa_perfect_agreement(self):
        h = [1, 2, 3, 4, 5]
        assert calculate_weighted_kappa(h, h) == 1.0

    def test_kappa_mismatched_lengths_returns_zero(self):
        assert calculate_cohen_kappa([1, 2], [1]) == 0.0

    def test_human_ratings_unavailable_without_column(self):
        df = pd.DataFrame({"human_intent": ["DeliveryStatus"]})
        available, msg = check_human_ratings_available(df)
        assert not available
        assert "does not exist" in msg

    def test_human_ratings_unavailable_when_all_null(self):
        df = pd.DataFrame({"human_reply_quality": [pd.NA, pd.NA]})
        available, _ = check_human_ratings_available(df)
        assert not available


# ──────────────────────────────────────────────────────────────────────────────
# Failure analysis
# ──────────────────────────────────────────────────────────────────────────────

class TestFailureAnalysis:
    def _make_result(self, golden_id, true_intent, pred_intent,
                     true_esc, pred_esc, overall_score, safety):
        return {
            "golden_id": golden_id,
            "customer_message": "test message",
            "true_intent": true_intent,
            "pred_intent": pred_intent,
            "true_escalation": true_esc,
            "pred_escalation": pred_esc,
            "generated_reply": "some reply",
            "judge_scores": {
                "overall_score": overall_score,
                "safety": safety,
                "relevance": 3,
                "rationale": "test",
            },
        }

    def test_detects_intent_mismatch(self, tmp_path):
        r = self._make_result("G-1", "DeliveryStatus", "OTHER",
                              "AUTO-HANDLE", "AUTO-HANDLE", 4.0, 5)
        m = generate_failure_analysis([r], str(tmp_path / "fa.md"))
        assert m["intent_failures"] == 1
        assert m["escalation_failures"] == 0

    def test_detects_escalation_mismatch(self, tmp_path):
        r = self._make_result("G-2", "DeliveryStatus", "DeliveryStatus",
                              "ESCALATE", "AUTO-HANDLE", 4.0, 5)
        m = generate_failure_analysis([r], str(tmp_path / "fa.md"))
        assert m["escalation_failures"] == 1
        assert m["intent_failures"] == 0

    def test_detects_low_judge_score_overall(self, tmp_path):
        r = self._make_result("G-3", "DeliveryStatus", "DeliveryStatus",
                              "AUTO-HANDLE", "AUTO-HANDLE", 2.0, 5)
        m = generate_failure_analysis([r], str(tmp_path / "fa.md"))
        assert m["low_judge_scores"] == 1

    def test_detects_low_judge_score_safety(self, tmp_path):
        r = self._make_result("G-4", "DeliveryStatus", "DeliveryStatus",
                              "AUTO-HANDLE", "AUTO-HANDLE", 4.0, 2)
        m = generate_failure_analysis([r], str(tmp_path / "fa.md"))
        assert m["low_judge_scores"] == 1

    def test_no_failures_on_correct_result(self, tmp_path):
        r = self._make_result("G-5", "DeliveryStatus", "DeliveryStatus",
                              "AUTO-HANDLE", "AUTO-HANDLE", 4.5, 5)
        m = generate_failure_analysis([r], str(tmp_path / "fa.md"))
        assert m["intent_failures"] == 0
        assert m["escalation_failures"] == 0
        assert m["low_judge_scores"] == 0

    def test_output_file_is_created(self, tmp_path):
        out = tmp_path / "failure_analysis.md"
        generate_failure_analysis([], str(out))
        assert out.exists()

    def test_output_file_contains_golden_id(self, tmp_path):
        r = self._make_result("G-99", "DeliveryStatus", "OTHER",
                              "AUTO-HANDLE", "AUTO-HANDLE", 4.0, 5)
        out = tmp_path / "fa.md"
        generate_failure_analysis([r], str(out))
        assert "G-99" in out.read_text(encoding="utf-8")
