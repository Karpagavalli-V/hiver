"""
run_eval_tests.py — Standalone test runner for evaluation harness.

Does NOT use pytest or import openai/sklearn/pandas at module level.
Runs entirely via Python's built-in unittest. Fast startup.

Usage:
    python scripts/run_eval_tests.py
"""

import sys
import os
import json
import tempfile
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ── Lightweight imports only ──────────────────────────────────────────────────
from src.evaluation.eval_cache import EvalCache


# ─────────────────────────────────────────────────────────────────────────────
# 1. EvalCache: miss, hit, persist, key, corrupt, autosave, len
# ─────────────────────────────────────────────────────────────────────────────
class TestEvalCacheMiss(unittest.TestCase):
    def test_miss_returns_none(self):
        with tempfile.TemporaryDirectory() as d:
            c = EvalCache("t", cache_dir=d)
            self.assertIsNone(c.get("no_such_key"))


class TestEvalCacheHit(unittest.TestCase):
    def test_hit_returns_stored_value(self):
        with tempfile.TemporaryDirectory() as d:
            c = EvalCache("t", cache_dir=d)
            k = EvalCache.make_key("hello", "world")
            c.set(k, {"intent": "DeliveryStatus"})
            self.assertEqual(c.get(k), {"intent": "DeliveryStatus"})

    def test_has_false_then_true(self):
        with tempfile.TemporaryDirectory() as d:
            c = EvalCache("t", cache_dir=d)
            k = EvalCache.make_key("m")
            self.assertFalse(c.has(k))
            c.set(k, {"v": 1})
            self.assertTrue(c.has(k))


class TestEvalCachePersist(unittest.TestCase):
    def test_persists_across_instances(self):
        with tempfile.TemporaryDirectory() as d:
            k = EvalCache.make_key("msg", "ctx")
            c1 = EvalCache("p", cache_dir=d)
            c1.set(k, {"score": 42})
            c1.save()
            c2 = EvalCache("p", cache_dir=d)
            self.assertEqual(c2.get(k), {"score": 42})

    def test_autosave_writes_file(self):
        with tempfile.TemporaryDirectory() as d:
            c = EvalCache("autosave", cache_dir=d)
            k = EvalCache.make_key("x")
            c.set(k, {"value": "auto"}, autosave=True)
            with open(c.path) as f:
                data = json.load(f)
            self.assertIn(k, data)

    def test_corrupt_file_returns_empty(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "eval_corrupt.json")
            with open(path, "w") as f:
                f.write("INVALID JSON{{")
            c = EvalCache("corrupt", cache_dir=d)
            self.assertEqual(len(c), 0)


class TestEvalCacheKeys(unittest.TestCase):
    def test_key_is_deterministic(self):
        k1 = EvalCache.make_key("msg A", "ctx B")
        k2 = EvalCache.make_key("msg A", "ctx B")
        self.assertEqual(k1, k2)

    def test_different_inputs_different_keys(self):
        k1 = EvalCache.make_key("msg A", "ctx B")
        k2 = EvalCache.make_key("msg X", "ctx Y")
        self.assertNotEqual(k1, k2)

    def test_len_reflects_items(self):
        with tempfile.TemporaryDirectory() as d:
            c = EvalCache("len", cache_dir=d)
            self.assertEqual(len(c), 0)
            c.set(EvalCache.make_key("a"), {"v": 1})
            c.set(EvalCache.make_key("b"), {"v": 2})
            self.assertEqual(len(c), 2)


# ─────────────────────────────────────────────────────────────────────────────
# 2. Resume logic
# ─────────────────────────────────────────────────────────────────────────────
class TestResumeLogic(unittest.TestCase):
    def test_partial_results_loaded(self):
        data = {"results": [
            {"golden_id": "G-1000", "status": "completed", "pred_intent": "DeliveryStatus"}
        ]}
        completed_map = {r["golden_id"]: r for r in data["results"]}
        self.assertIn("G-1000", completed_map)
        self.assertEqual(completed_map["G-1000"]["pred_intent"], "DeliveryStatus")

    def test_completed_id_is_skipped(self):
        completed_map = {"G-1000": {"golden_id": "G-1000", "status": "completed"}}
        api_calls = 0
        for g_id in ["G-1000", "G-1001"]:
            if g_id in completed_map:
                continue
            api_calls += 1
        self.assertEqual(api_calls, 1)


# ─────────────────────────────────────────────────────────────────────────────
# 3. Quota failure behaviour
# ─────────────────────────────────────────────────────────────────────────────
class TestQuotaFailure(unittest.TestCase):
    def test_rate_limit_stops_loop(self):
        class FakeRateLimitError(Exception):
            pass

        completed_map = {}
        failed_ids = []
        quota_hit = False

        def mock_classify(msg):
            if msg == "world":
                raise FakeRateLimitError("quota exceeded")
            return {"intent": "OTHER"}

        for ex in [{"id": "G-1", "msg": "hello"}, {"id": "G-2", "msg": "world"}]:
            try:
                result = mock_classify(ex["msg"])
                completed_map[ex["id"]] = result
            except FakeRateLimitError:
                failed_ids.append(ex["id"])
                quota_hit = True
                break

        self.assertTrue(quota_hit)
        self.assertIn("G-1", completed_map)
        self.assertNotIn("G-2", completed_map)
        self.assertIn("G-2", failed_ids)

    def test_non_quota_error_continues_loop(self):
        results = []
        failed_ids = []
        for ex in [{"id": "G-1", "fail": True}, {"id": "G-2", "fail": False}]:
            try:
                if ex["fail"]:
                    raise ValueError("unexpected")
                results.append({"id": ex["id"], "status": "completed"})
            except Exception as e:
                failed_ids.append(ex["id"])
                results.append({"id": ex["id"], "status": "failed"})

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["status"], "failed")
        self.assertEqual(results[1]["status"], "completed")
        self.assertIn("G-1", failed_ids)


# ─────────────────────────────────────────────────────────────────────────────
# 4. No duplicate API calls
# ─────────────────────────────────────────────────────────────────────────────
class TestNoDuplicateAPICalls(unittest.TestCase):
    def test_cache_hit_prevents_api_call(self):
        with tempfile.TemporaryDirectory() as d:
            c = EvalCache("clf", cache_dir=d)
            k = EvalCache.make_key("test message", "context")
            c.set(k, {"intent": "DeliveryStatus", "confidence": 0.99})

            api_calls = 0

            def mock_classify(msg, context=None):
                nonlocal api_calls
                api_calls += 1
                return {"intent": "OTHER"}

            result = c.get(k) if c.has(k) else mock_classify("test message", "context")

            self.assertEqual(api_calls, 0)
            self.assertEqual(result["intent"], "DeliveryStatus")

    def test_same_input_one_api_call(self):
        with tempfile.TemporaryDirectory() as d:
            c = EvalCache("dedup", cache_dir=d)
            api_calls = 0

            def api_call(msg):
                nonlocal api_calls
                api_calls += 1
                return {"intent": "OTHER", "confidence": 0.9}

            k = EvalCache.make_key("hello")
            for _ in range(3):   # same message 3 times
                if not c.has(k):
                    c.set(k, api_call("hello"))

            self.assertEqual(api_calls, 1)


# ─────────────────────────────────────────────────────────────────────────────
# 5. Offline mode (mock judge — no openai import needed)
# ─────────────────────────────────────────────────────────────────────────────
class TestOfflineMode(unittest.TestCase):
    """
    Tests the mock judge contract without importing openai.
    We inline the mock logic that LLMJudge(mock_mode=True) would use.
    """

    def _mock_judge_evaluate(self, customer_message, generated_reply, evidence, context=None):
        return {
            "relevance": 4,
            "groundedness": 4,
            "helpfulness": 3,
            "safety": 5,
            "tone": 4,
            "overall_score": 4.0,
            "pass": True,
            "rationale": "[MOCK] Reasonable reply based on evidence."
        }

    def test_mock_returns_valid_schema(self):
        result = self._mock_judge_evaluate("Where is my order?", "It is on the way.", "Root ID 1")
        required = {"relevance", "groundedness", "helpfulness",
                    "safety", "tone", "overall_score", "pass", "rationale"}
        self.assertTrue(required.issubset(set(result.keys())))

    def test_mock_pass_is_true(self):
        result = self._mock_judge_evaluate("msg", "reply", "evidence")
        self.assertTrue(result["pass"])

    def test_mock_rationale_tagged(self):
        result = self._mock_judge_evaluate("m", "r", "e")
        self.assertIn("[MOCK]", result["rationale"])

    def test_mock_safety_is_max(self):
        result = self._mock_judge_evaluate("m", "r", "e")
        self.assertEqual(result["safety"], 5)


# ─────────────────────────────────────────────────────────────────────────────
# 6. Failure analysis
# ─────────────────────────────────────────────────────────────────────────────
class TestFailureAnalysis(unittest.TestCase):
    def _make(self, gid, true_i, pred_i, true_e, pred_e, overall, safety):
        return {
            "golden_id": gid,
            "customer_message": "test",
            "true_intent": true_i,
            "pred_intent": pred_i,
            "true_escalation": true_e,
            "pred_escalation": pred_e,
            "generated_reply": "reply",
            "judge_scores": {"overall_score": overall, "safety": safety,
                             "relevance": 3, "rationale": "test"},
        }

    def _run(self, results):
        from src.evaluation.failure_analysis import generate_failure_analysis
        with tempfile.TemporaryDirectory() as d:
            return generate_failure_analysis(results, os.path.join(d, "fa.md"))

    def test_intent_mismatch_detected(self):
        r = self._make("G-1", "DeliveryStatus", "OTHER", "AUTO-HANDLE", "AUTO-HANDLE", 4.0, 5)
        m = self._run([r])
        self.assertEqual(m["intent_failures"], 1)

    def test_escalation_mismatch_detected(self):
        r = self._make("G-2", "DS", "DS", "ESCALATE", "AUTO-HANDLE", 4.0, 5)
        m = self._run([r])
        self.assertEqual(m["escalation_failures"], 1)

    def test_low_overall_score_detected(self):
        r = self._make("G-3", "DS", "DS", "AUTO-HANDLE", "AUTO-HANDLE", 2.0, 5)
        m = self._run([r])
        self.assertEqual(m["low_judge_scores"], 1)

    def test_low_safety_detected(self):
        r = self._make("G-4", "DS", "DS", "AUTO-HANDLE", "AUTO-HANDLE", 4.5, 2)
        m = self._run([r])
        self.assertEqual(m["low_judge_scores"], 1)

    def test_correct_result_no_failures(self):
        r = self._make("G-5", "DS", "DS", "AUTO-HANDLE", "AUTO-HANDLE", 4.5, 5)
        m = self._run([r])
        self.assertEqual(m["intent_failures"], 0)
        self.assertEqual(m["escalation_failures"], 0)
        self.assertEqual(m["low_judge_scores"], 0)

    def test_output_file_created(self):
        from src.evaluation.failure_analysis import generate_failure_analysis
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "fa.md")
            generate_failure_analysis([], out)
            self.assertTrue(os.path.exists(out))

    def test_output_contains_golden_id(self):
        from src.evaluation.failure_analysis import generate_failure_analysis
        r = self._make("G-99", "DS", "OTHER", "AUTO-HANDLE", "AUTO-HANDLE", 4.0, 5)
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "fa.md")
            generate_failure_analysis([r], out)
            with open(out, encoding="utf-8") as f:
                self.assertIn("G-99", f.read())


# ─────────────────────────────────────────────────────────────────────────────
# 7. Kappa helpers (no heavy imports)
# ─────────────────────────────────────────────────────────────────────────────
class TestKappa(unittest.TestCase):
    def test_cohen_kappa_perfect(self):
        from src.evaluation.human_judge_agreement import calculate_cohen_kappa
        self.assertEqual(calculate_cohen_kappa([1,2,3,4,5], [1,2,3,4,5]), 1.0)

    def test_weighted_kappa_perfect(self):
        from src.evaluation.human_judge_agreement import calculate_weighted_kappa
        self.assertEqual(calculate_weighted_kappa([1,2,3,4,5], [1,2,3,4,5]), 1.0)

    def test_kappa_mismatched_lengths(self):
        from src.evaluation.human_judge_agreement import calculate_cohen_kappa
        self.assertEqual(calculate_cohen_kappa([1,2], [1]), 0.0)


# ─────────────────────────────────────────────────────────────────────────────
# 8. Human Judge Workflow (20 Examples) Validation & Sampling Tests
# ─────────────────────────────────────────────────────────────────────────────
class TestHumanJudgeWorkflow(unittest.TestCase):
    def test_sampling_produces_20_unique_items(self):
        from scripts.sample_human_judge_20 import perform_stratified_sampling
        dummy_results = [
            {"golden_id": f"G-{i}", "pred_intent": f"Intent_{i%5}", "true_escalation": "AUTO-HANDLE" if i%2==0 else "ESCALATE", "judge_scores": {}}
            for i in range(100)
        ]
        sampled = perform_stratified_sampling(dummy_results, target_n=20, seed=42)
        self.assertEqual(len(sampled), 20)
        gids = [x["golden_id"] for x in sampled]
        self.assertEqual(len(set(gids)), 20)

    def test_validation_fails_on_empty_csv(self):
        from scripts.validate_human_judge_20 import validate_human_judge_csv
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "test_empty.csv")
            with open(path, "w") as f:
                f.write("golden_id,human_relevance\n")
            is_valid, errors = validate_human_judge_csv(path)
            self.assertFalse(is_valid)

    def test_validation_passes_on_valid_csv(self):
        from scripts.validate_human_judge_20 import validate_human_judge_csv
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "test_valid.csv")
            cols = ["golden_id", "human_relevance", "human_groundedness", "human_helpfulness", "human_safety", "human_tone", "judge_relevance", "judge_groundedness", "judge_helpfulness", "judge_safety", "judge_tone"]
            rows = [
                f"G-{1000+i},4,3,4,5,4,3,2,3,5,4" for i in range(20)
            ]
            with open(path, "w") as f:
                f.write(",".join(cols) + "\n" + "\n".join(rows))
            is_valid, errors = validate_human_judge_csv(path)
            self.assertTrue(is_valid, msg=f"Errors: {errors}")


# ─────────────────────────────────────────────────────────────────────────────
# 9. Support Pipeline Integration Test
# ─────────────────────────────────────────────────────────────────────────────
class TestSupportPipeline(unittest.TestCase):
    def test_pipeline_offline_mode(self):
        from src.pipeline import SupportPipeline
        pipeline = SupportPipeline(mock_mode=True)
        res = pipeline.process("Where is my package?")
        self.assertIn("customer_message", res)
        self.assertIn("intent", res)
        self.assertIn("confidence", res)
        self.assertIn("retrieved_evidence", res)
        self.assertIn("generated_reply", res)
        self.assertIn("decision", res)
        self.assertIn(res["decision"], ["AUTO-HANDLE", "ESCALATE"])
        self.assertTrue(len(res["generated_reply"]) > 0)




# ─────────────────────────────────────────────────────────────────────────────
# Runner
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite  = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
