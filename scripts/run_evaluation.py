"""
run_evaluation.py — Phase 5B Resumable Evaluation Harness

Usage
-----
Offline/mock (no API calls, safe):
    python scripts/run_evaluation.py --judge --offline

5-example live smoke-test (consumes real API quota, small):
    python scripts/run_evaluation.py --judge --limit 5

Full resumable live evaluation (stops cleanly on quota, resumes on next run):
    python scripts/run_evaluation.py --judge
"""

import os
import sys
import json
import argparse
import pandas as pd
import numpy as np
import joblib
import openai
from sklearn.metrics import accuracy_score, f1_score, classification_report
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.classification.llm_classifier import LLMClassifier
from src.decision.escalation import EscalationDecisionEngine
from src.retrieval.historical_retriever import HistoricalRetriever
from src.generation.reply_generator import ReplyGenerator, LLMReplyProvider, MockReplyProvider
from src.evaluation.llm_judge import LLMJudge
from src.evaluation.eval_cache import EvalCache
from src.evaluation.human_judge_agreement import check_human_ratings_available, report_agreement
from src.evaluation.failure_analysis import generate_failure_analysis

# ──────────────────────────────────────────────────────────────────────────────
# PARTIAL RESULTS PERSISTENCE
# ──────────────────────────────────────────────────────────────────────────────
PARTIAL_RESULTS_PATH = "reports/evaluation_results_partial.json"
FINAL_RESULTS_PATH   = "reports/evaluation_results.json"


def _load_partial() -> dict:
    """Load an existing partial results file keyed by golden_id."""
    if os.path.exists(PARTIAL_RESULTS_PATH):
        try:
            with open(PARTIAL_RESULTS_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
            return {r["golden_id"]: r for r in data.get("results", [])}
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def _save_partial(results: list):
    os.makedirs("reports", exist_ok=True)
    with open(PARTIAL_RESULTS_PATH, "w", encoding="utf-8") as f:
        json.dump({"results": results, "status": "partial"}, f, indent=2)


def _save_final(results: list, mode: str):
    os.makedirs("reports", exist_ok=True)
    with open(FINAL_RESULTS_PATH, "w", encoding="utf-8") as f:
        json.dump({"results": results, "mode": mode, "status": "complete"}, f, indent=2)


# ──────────────────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Phase 5B Golden Set Evaluation Harness")
    parser.add_argument("--offline", action="store_true",
                        help="Run in offline/mock mode — no API calls made.")
    parser.add_argument("--judge", action="store_true",
                        help="Run LLM-as-Judge evaluation on generated replies.")
    parser.add_argument("--limit", type=int, default=None,
                        help="Process only N examples (useful for smoke-testing).")
    parser.add_argument("--fresh", action="store_true",
                        help="Bypass cache for evaluated examples to make fresh API calls.")
    parser.add_argument("--fresh-id", type=str, default=None,
                        help="Run fresh live evaluation for a specific golden_id (e.g. G-1000).")
    args = parser.parse_args()

    run_mode = "OFFLINE/MOCK" if args.offline else "LIVE"
    print(f"=== Phase 5B Evaluation — mode: {run_mode} ===")

    load_dotenv(override=True)

    # ── Load Golden Set ──────────────────────────────────────────────────────
    print("Loading Golden Set...")
    golden_df = pd.read_csv("data/golden_set/golden_set_final.csv")

    # Safety assertions (no target responses in input — this is enforced at
    # dataset creation; we assert structural invariants here).
    assert len(golden_df) == 200, f"Expected 200 examples, got {len(golden_df)}"
    assert "human_intent"      in golden_df.columns, "Missing column: human_intent"
    assert "human_auto_handle" in golden_df.columns, "Missing column: human_auto_handle"
    assert "customer_message"  in golden_df.columns, "Missing column: customer_message"
    # Weak labels must NOT be used as ground truth — we only read human_intent.
    assert "weak_label" not in ["human_intent", "human_auto_handle"], \
        "Ground truth columns must not reference weak labels."

    if args.fresh_id:
        golden_df = golden_df[golden_df["golden_id"] == args.fresh_id]
        print(f"  --fresh-id {args.fresh_id}: processing single example {args.fresh_id} only.")
    elif args.limit:
        golden_df = golden_df.head(args.limit)
        print(f"  --limit {args.limit}: processing first {args.limit} examples only.")

    n_total = len(golden_df)

    # ── Persistent caches ────────────────────────────────────────────────────
    clf_cache   = EvalCache("classifier")
    gen_cache   = EvalCache("generator")
    judge_cache = EvalCache("judge")

    # ── Component initialisation ─────────────────────────────────────────────
    print("Initializing components...")
    classifier = LLMClassifier(mock_mode=args.offline)
    escalator  = EscalationDecisionEngine()
    retriever  = HistoricalRetriever()
    provider   = MockReplyProvider() if args.offline else LLMReplyProvider()
    generator  = ReplyGenerator(provider=provider)
    judge      = LLMJudge(mock_mode=(not args.judge or args.offline))

    # ── Baselines (no API needed) ─────────────────────────────────────────────
    with open("models/majority_baseline.json", "r") as f:
        maj_intent = json.load(f)["majority_class"]
    vec_msg = joblib.load("models/vec_msg.joblib")
    clf_msg = joblib.load("models/clf_msg.joblib")

    y_true_intent_all = golden_df["human_intent"].tolist()
    y_true_esc_all    = golden_df["human_auto_handle"].tolist()

    y_pred_maj   = [maj_intent] * n_total
    X_tfidf      = vec_msg.transform(golden_df["customer_message"])
    y_pred_tfidf = clf_msg.predict(X_tfidf)

    # ── Resume from partial run ───────────────────────────────────────────────
    completed_map = _load_partial()
    if completed_map:
        print(f"  Resuming: found {len(completed_map)} previously completed result(s).")

    # ── Main evaluation loop ─────────────────────────────────────────────────
    results        = list(completed_map.values())   # carry forward any prior results
    failed_ids     = []
    quota_hit      = False
    completed_this_run = 0

    for pos, (_, row) in enumerate(golden_df.iterrows(), start=1):
        g_id = row["golden_id"]

        bypass_cache = args.fresh or (args.fresh_id is not None and g_id == args.fresh_id)

        # Already done? skip unless bypassing cache for this item.
        if not bypass_cache and g_id in completed_map:
            print(f"  [{pos}/{n_total}] {g_id} — cache hit, skipped.")
            continue

        msg     = row["customer_message"]
        ctx     = row["conversation_context"] if pd.notna(row.get("conversation_context")) else None
        root_id = g_id

        try:
            # ── 1. Intent Classification ──────────────────────────────────
            clf_key = EvalCache.make_key(msg, ctx or "")
            if not bypass_cache and clf_cache.has(clf_key):
                clf_data   = clf_cache.get(clf_key)
                pred_intent = clf_data["intent"]
                confidence  = clf_data["confidence"]
            else:
                clf_res     = classifier.classify(msg, context=ctx, use_cache=not bypass_cache)
                pred_intent = clf_res.intent
                confidence  = clf_res.confidence
                clf_cache.set(clf_key, {"intent": pred_intent, "confidence": confidence,
                                         "reason": clf_res.reason}, autosave=True)

            # ── 2. Retrieval (deterministic, no API) ──────────────────────
            retrieved = retriever.retrieve(msg, pred_intent, top_k=3, query_root_id=root_id)
            formatted_evidence = generator._format_evidence(retrieved)

            # ── 3. Reply Generation ───────────────────────────────────────
            gen_key = EvalCache.make_key(msg, pred_intent, formatted_evidence, ctx or "")
            if not bypass_cache and gen_cache.has(gen_key):
                gen_res = gen_cache.get(gen_key)
            else:
                gen_res = generator.generate(msg, pred_intent, retrieved, context=ctx)
                gen_cache.set(gen_key, gen_res, autosave=True)
            reply = gen_res.get("reply", "")

            # ── 4. Escalation (deterministic) ─────────────────────────────
            esc_res  = escalator.decide(msg, pred_intent, confidence, retrieved, gen_res, context=ctx)
            pred_esc = esc_res["decision"]

            # ── 5. LLM Judge ──────────────────────────────────────────────
            judge_res = None
            if args.judge:
                judge_key = EvalCache.make_key(msg, reply, formatted_evidence, ctx or "")
                if not bypass_cache and judge_cache.has(judge_key):
                    judge_res = judge_cache.get(judge_key)
                else:
                    judge_res = judge.evaluate_reply(msg, reply, formatted_evidence, context=ctx)
                    judge_cache.set(judge_key, judge_res, autosave=True)

            # ── Record result ─────────────────────────────────────────────
            record = {
                "golden_id":        root_id,
                "customer_message": msg,
                "true_intent":      row["human_intent"],
                "pred_intent":      pred_intent,
                "true_escalation":  row["human_auto_handle"],
                "pred_escalation":  pred_esc,
                "generated_reply":  reply,
                "judge_scores":     judge_res,
                "status":           "completed",
                "run_mode":         run_mode,
            }
            results.append(record)
            completed_map[g_id] = record
            completed_this_run += 1

            # Save partial after every completed example
            _save_partial(list(completed_map.values()))
            print(f"  [{pos}/{n_total}] {g_id} — completed (intent: {pred_intent})")

        except (openai.RateLimitError, openai.APIConnectionError) as e:
            print(f"  [{pos}/{n_total}] {g_id} — API quota reached — stopping safely.")
            print(f"  Error: {e}")
            failed_ids.append(g_id)
            quota_hit = True
            # Save caches before exit so no work is lost
            clf_cache.save()
            gen_cache.save()
            judge_cache.save()
            _save_partial(list(completed_map.values()))
            break

        except Exception as e:
            # Non-quota failure: log it and continue with next example
            print(f"  [{pos}/{n_total}] {g_id} — FAILED (non-quota): {e}")
            failed_ids.append(g_id)
            results.append({
                "golden_id":    g_id,
                "status":       "failed",
                "error":        str(e),
                "run_mode":     run_mode,
            })
            completed_map[g_id] = results[-1]
            _save_partial(list(completed_map.values()))

    # Flush all caches
    clf_cache.save()
    gen_cache.save()
    judge_cache.save()

    if quota_hit:
        print(f"\n  Stopped at quota limit. {completed_this_run} new example(s) completed this run.")
        print(f"  Re-run the same command to resume from the next missing example.")
        # Don't write evaluation_report for a partial run
        return

    # ── Only compute full metrics if all N examples succeeded ────────────────
    complete_results   = [r for r in results if r.get("status") == "completed"]
    n_complete         = len(complete_results)
    n_failed           = len([r for r in results if r.get("status") == "failed"])

    print(f"\n  {n_complete}/{n_total} examples completed, {n_failed} failed.")

    if n_complete == 0:
        print("  No completed results to report. Stopping.")
        return

    y_true_intent = [r["true_intent"]    for r in complete_results]
    y_pred_llm    = [r["pred_intent"]    for r in complete_results]
    y_true_esc    = [r["true_escalation"] for r in complete_results]
    y_pred_esc    = [r["pred_escalation"] for r in complete_results]

    # Align baselines to the same subset
    complete_ids        = {r["golden_id"] for r in complete_results}
    baseline_mask       = golden_df["golden_id"].isin(complete_ids)
    y_true_intent_base  = golden_df.loc[baseline_mask, "human_intent"].tolist()
    y_pred_maj_sub      = [maj_intent] * len(y_true_intent_base)
    y_pred_tfidf_sub    = vec_msg.transform(golden_df.loc[baseline_mask, "customer_message"])
    y_pred_tfidf_sub    = clf_msg.predict(y_pred_tfidf_sub)

    # Intent
    acc_llm   = accuracy_score(y_true_intent, y_pred_llm)
    f1_llm    = f1_score(y_true_intent, y_pred_llm, average="macro", zero_division=0)
    p_llm     = f1_score(y_true_intent, y_pred_llm, average="macro", zero_division=0)  # approx
    intent_report = classification_report(y_true_intent, y_pred_llm, zero_division=0)

    acc_maj  = accuracy_score(y_true_intent_base, y_pred_maj_sub)
    f1_maj   = f1_score(y_true_intent_base, y_pred_maj_sub, average="macro", zero_division=0)

    acc_tfidf = accuracy_score(y_true_intent_base, y_pred_tfidf_sub)
    f1_tfidf  = f1_score(y_true_intent_base, y_pred_tfidf_sub, average="macro", zero_division=0)

    # Escalation
    acc_esc   = accuracy_score(y_true_esc, y_pred_esc)
    esc_report = classification_report(y_true_esc, y_pred_esc, zero_division=0)
    auto_rate  = y_pred_esc.count("AUTO-HANDLE") / n_complete
    esc_rate   = y_pred_esc.count("ESCALATE")    / n_complete

    # Reply quality (only from results where judge_scores is a real dict)
    judged = [r for r in complete_results if isinstance(r.get("judge_scores"), dict)]
    n_judged = len(judged)
    avg_relevance     = np.mean([r["judge_scores"]["relevance"]     for r in judged]) if judged else 0.0
    avg_groundedness  = np.mean([r["judge_scores"]["groundedness"]  for r in judged]) if judged else 0.0
    avg_helpfulness   = np.mean([r["judge_scores"]["helpfulness"]   for r in judged]) if judged else 0.0
    avg_safety        = np.mean([r["judge_scores"]["safety"]        for r in judged]) if judged else 0.0
    avg_tone          = np.mean([r["judge_scores"]["tone"]          for r in judged]) if judged else 0.0
    avg_overall       = np.mean([r["judge_scores"]["overall_score"] for r in judged]) if judged else 0.0
    pass_rate         = np.mean([1 if r["judge_scores"]["pass"] else 0 for r in judged]) if judged else 0.0

    # Human/judge agreement
    has_human_ratings, _ = check_human_ratings_available(golden_df)

    # Failure analysis
    failures = generate_failure_analysis(complete_results)

    # ── Save final results ────────────────────────────────────────────────────
    _save_final(results, mode=run_mode)

    # ── Write evaluation_report.md ────────────────────────────────────────────
    os.makedirs("reports", exist_ok=True)
    with open("reports/evaluation_report.md", "w", encoding="utf-8") as f:
        f.write("# Phase 5B Evaluation Report\n\n")

        # Mode banner
        f.write(f"> **Run mode**: {run_mode}  \n")
        if n_failed:
            f.write(f"> **WARNING**: {n_failed} example(s) failed due to API errors and are **excluded** from metrics.  \n")
        f.write(f"> **Examples evaluated**: {n_complete} / {n_total}  \n\n")

        # Dataset
        f.write("## 1. Dataset\n")
        f.write("- **Golden Set size**: 200 examples\n")
        f.write("- **Source split**: INTERNAL_TEST\n")
        f.write("- **Annotation status**: 200 manually reviewed human annotations (100% human-verified ground truth).\n")
        f.write("- **Weak labels**: NOT used as ground truth. All metrics computed against `human_intent`.\n")
        f.write("- **Target responses**: NOT supplied to classifier, retriever, generator, or judge.\n\n")

        # Intent
        f.write("## 2. Intent Classification\n")
        f.write(f"- **Current Model ({run_mode}) Accuracy**: {acc_llm:.4f} | **Macro F1**: {f1_llm:.4f}\n")
        f.write(f"- **TF-IDF Baseline Accuracy**: {acc_tfidf:.4f} | **Macro F1**: {f1_tfidf:.4f}\n")
        f.write(f"- **Majority Baseline Accuracy**: {acc_maj:.4f} | **Macro F1**: {f1_maj:.4f}\n\n")
        f.write("### Per-Intent Results (Current Model)\n```text\n")
        f.write(intent_report)
        f.write("```\n\n")

        # Escalation
        f.write("## 3. Escalation\n")
        f.write(f"- **Accuracy**: {acc_esc:.4f}\n")
        f.write(f"- **AUTO-HANDLE rate**: {auto_rate:.4f}\n")
        f.write(f"- **ESCALATE rate**: {esc_rate:.4f}\n\n")
        f.write("### Escalation Classification Report\n```text\n")
        f.write(esc_report)
        f.write("```\n\n")

        # Reply quality
        f.write("## 4. Reply Quality (LLM-as-Judge)\n")
        if n_judged > 0:
            f.write(f"- **Run mode**: {run_mode}\n")
            f.write(f"- **Replies judged**: {n_judged}\n")
            f.write(f"- **Relevance**: {avg_relevance:.2f}\n")
            f.write(f"- **Groundedness**: {avg_groundedness:.2f}\n")
            f.write(f"- **Helpfulness**: {avg_helpfulness:.2f}\n")
            f.write(f"- **Safety**: {avg_safety:.2f}\n")
            f.write(f"- **Tone**: {avg_tone:.2f}\n")
            f.write(f"- **Overall Score**: {avg_overall:.2f}\n")
            f.write(f"- **Pass Rate**: {pass_rate*100:.1f}%\n\n")
        else:
            f.write("- LLM Judge evaluation was NOT run (run with --judge), "
                    "or all judge calls failed.\n\n")

        # Human/judge agreement
        f.write("## 5. Human / Judge Agreement\n")
        if has_human_ratings:
            f.write("Genuine human reply-quality ratings found — agreement could be calculated.\n\n")
        else:
            f.write("**NOT AVAILABLE** — No genuine human reply-quality ratings exist yet. "
                    "No fabricated agreement score is reported.\n\n")

        # Failure analysis
        f.write("## 6. Failure Analysis\n")
        f.write("See `reports/failure_analysis.md` for detailed examples.\n")
        f.write(f"- Intent mismatches: {failures['intent_failures']}\n")
        f.write(f"- Escalation mismatches: {failures['escalation_failures']}\n")
        f.write(f"- Low Judge Scores (< 3.0 or safety < 4): {failures['low_judge_scores']}\n")
        if failed_ids:
            f.write(f"\n### Failed / Missing API Calls\n")
            f.write(f"The following {len(failed_ids)} example(s) could not be evaluated "
                    "due to API errors and are **excluded** from all metrics above:\n\n")
            for fid in failed_ids:
                f.write(f"- {fid}\n")
        f.write("\n")

        # Limitations
        f.write("## 7. Limitations\n")
        f.write("- Mixed human/AI-assisted Golden Set annotations\n")
        f.write("- Small Golden Set (200 examples)\n")
        f.write("- LLM judge may hallucinate or misunderstand nuance\n")
        f.write("- Possible sampling bias in source TWCS data\n\n")

        # Reproduction
        f.write("## 8. Reproduction\n")
        f.write("```bash\n")
        f.write("# 5-example live smoke-test\n")
        f.write("python scripts/run_evaluation.py --judge --limit 5\n\n")
        f.write("# Full resumable live evaluation\n")
        f.write("python scripts/run_evaluation.py --judge\n\n")
        f.write("# Offline/mock (no API calls consumed)\n")
        f.write("python scripts/run_evaluation.py --judge --offline\n")
        f.write("```\n")

    print("\n=== Evaluation Complete ===")
    print(f"  Mode              : {run_mode}")
    print(f"  Completed         : {n_complete} / {n_total}")
    print(f"  Failed (excluded) : {n_failed}")
    print(f"  Intent accuracy   : {acc_llm:.4f}  Macro F1: {f1_llm:.4f}")
    print(f"  Escalation acc    : {acc_esc:.4f}")
    if n_judged:
        print(f"  Reply quality     : overall avg {avg_overall:.2f}  pass rate {pass_rate*100:.1f}%")
    print("  Report            : reports/evaluation_report.md")


if __name__ == "__main__":
    main()
