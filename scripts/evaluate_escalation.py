import pandas as pd
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'classification')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'retrieval')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'generation')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'decision')))

from historical_retriever import HistoricalRetriever
from reply_generator import ReplyGenerator, MockReplyProvider
from escalation import EscalationDecisionEngine

def main():
    print("Loading Validation Split for Escalation Evaluation...")
    val_df = pd.read_csv("data/splits/amazon_val.csv")
    twcs_df = pd.read_csv("data/twcs.csv")
    
    val_df = val_df[val_df['weak_label'].notna() & (val_df['weak_label'] != 'AMBIGUOUS')]
    
    merged = pd.merge(val_df, twcs_df[['tweet_id', 'text']], on='tweet_id', how='inner')
    merged['created_at_dt'] = pd.to_datetime(merged['created_at'], format='%a %b %d %H:%M:%S +0000 %Y', errors='coerce')
    
    sample_df = merged.sample(n=min(500, len(merged)), random_state=42)
    
    retriever = HistoricalRetriever()
    generator = ReplyGenerator(provider=MockReplyProvider())
    engine = EscalationDecisionEngine()
    
    results_list = []
    
    total_cases = 0
    auto_handle_count = 0
    escalate_count = 0
    
    escalation_by_intent = {}
    escalation_by_risk_flag = {}
    
    print(f"Evaluating {len(sample_df)} cases for escalation...")
    
    for idx, row in sample_df.iterrows():
        total_cases += 1
        
        # MOCK Intent and Confidence since LLM Classifier is expensive to run 500 times.
        # We use weak_label for mock intent.
        intent = row['weak_label']
        # Mock confidence: 10% low confidence artificially to test rule distribution
        confidence = 0.9 if idx % 10 != 0 else 0.6
        
        results = retriever.retrieve(
            query_message=row['text'],
            intent=intent,
            top_k=3,
            query_root_id=row['root_id'],
            query_timestamp=row['created_at_dt']
        )
        
        reply_dict = generator.generate(
            customer_message=row['text'],
            intent=intent,
            retrieved_examples=results
        )
        
        decision = engine.decide(
            customer_message=row['text'],
            intent=intent,
            classifier_confidence=confidence,
            retrieved_examples=results,
            generated_reply=reply_dict
        )
        
        is_escalate = (decision["decision"] == "ESCALATE")
        if is_escalate:
            escalate_count += 1
        else:
            auto_handle_count += 1
            
        # Stats by intent
        if intent not in escalation_by_intent:
            escalation_by_intent[intent] = {"total": 0, "escalated": 0}
        escalation_by_intent[intent]["total"] += 1
        if is_escalate:
            escalation_by_intent[intent]["escalated"] += 1
            
        # Stats by flag
        for flag in decision["risk_flags"]:
            escalation_by_risk_flag[flag] = escalation_by_risk_flag.get(flag, 0) + 1
            
        results_list.append({
            "tweet_id": row["tweet_id"],
            "text": row["text"],
            "intent": intent,
            "decision": decision["decision"],
            "reason": decision["reason"],
            "risk_flags": decision["risk_flags"]
        })
        
    print(f"\nTotal cases: {total_cases}")
    print(f"AUTO-HANDLE: {auto_handle_count} ({(auto_handle_count/total_cases*100):.1f}%)")
    print(f"ESCALATE: {escalate_count} ({(escalate_count/total_cases*100):.1f}%)")
    
    print("\nEscalation Rate by Intent:")
    for intent, data in escalation_by_intent.items():
        rate = data["escalated"] / data["total"] * 100
        print(f"  {intent}: {rate:.1f}% ({data['escalated']}/{data['total']})")
        
    print("\nEscalation Rate by Risk Flag:")
    for flag, count in sorted(escalation_by_risk_flag.items(), key=lambda x: -x[1]):
        print(f"  {flag}: {count}")

    # Inspect 30 cases
    auto_cases = [r for r in results_list if r["decision"] == "AUTO-HANDLE"][:15]
    esc_cases = [r for r in results_list if r["decision"] == "ESCALATE"][:15]
    
    print("\n--- REPRESENTATIVE CASES ---")
    print("AUTO-HANDLE EXAMPLES:")
    for c in auto_cases:
        print(f" - [{c['intent']}] {c['text']}")
        print(f"   Reason: {c['reason']}")
    print("\nESCALATE EXAMPLES:")
    for c in esc_cases:
        print(f" - [{c['intent']}] {c['text']}")
        print(f"   Flags: {c['risk_flags']}")
        print(f"   Reason: {c['reason']}")

    os.makedirs("reports", exist_ok=True)
    with open("reports/escalation_evaluation.json", "w") as f:
        json.dump(results_list, f, indent=2)

if __name__ == "__main__":
    main()
