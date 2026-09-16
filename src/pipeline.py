import os
from typing import Dict, List, Optional
from dotenv import load_dotenv

from src.classification.llm_classifier import LLMClassifier
from src.decision.escalation import EscalationDecisionEngine
from src.retrieval.historical_retriever import HistoricalRetriever
from src.generation.reply_generator import ReplyGenerator, LLMReplyProvider, MockReplyProvider

class SupportPipeline:
    def __init__(self, mock_mode: bool = False):
        load_dotenv(override=True)
        self.mock_mode = mock_mode
        self.classifier = LLMClassifier(mock_mode=mock_mode)
        self.retriever = HistoricalRetriever()
        provider = MockReplyProvider() if mock_mode else LLMReplyProvider()
        self.generator = ReplyGenerator(provider=provider)
        self.escalator = EscalationDecisionEngine()

    def process(self, customer_message: str, context: Optional[str] = None) -> Dict:
        """
        Executes end-to-end customer support pipeline:
        1. LLM Intent Classification
        2. Vector/BM25 Historical Retrieval
        3. Grounded Reply Generation
        4. Escalation Decision Engine
        """
        if not customer_message or not customer_message.strip():
            raise ValueError("Customer message cannot be empty.")

        # 1. Intent Classification
        clf_res = self.classifier.classify(customer_message, context=context)
        intent = clf_res.intent
        confidence = clf_res.confidence
        clf_reason = clf_res.reason

        # 2. Historical Retrieval
        retrieved = self.retriever.retrieve(customer_message, intent, top_k=3)

        # 3. Grounded Reply Generation
        gen_res = self.generator.generate(customer_message, intent, retrieved, context=context)
        reply = gen_res.get("reply", "")

        # 4. Escalation Decision Engine
        esc_res = self.escalator.decide(customer_message, intent, confidence, retrieved, gen_res, context=context)

        return {
            "customer_message": customer_message,
            "context": context,
            "intent": intent,
            "confidence": confidence,
            "intent_reason": clf_reason,
            "retrieved_evidence": retrieved,
            "generated_reply": reply,
            "grounded_in_evidence": gen_res.get("grounded_in_evidence", True),
            "decision": esc_res.get("decision", "ESCALATE"),
            "escalation_reason": esc_res.get("reason", "No reason provided."),
            "risk_flags": esc_res.get("risk_flags", [])
        }
