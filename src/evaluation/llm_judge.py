import os
import json
import time
from typing import Dict, Optional
import openai

class LLMJudge:
    def __init__(self, mock_mode: bool = False):
        self.mock_mode = mock_mode
        if not self.mock_mode:
            api_key = (os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY") or "").strip().strip('"\'')
            base_url = os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
            self.client = openai.OpenAI(
                api_key=api_key,
                base_url=base_url
            )
            self.model_name = os.getenv("LLM_MODEL", "openai/gpt-4o-mini")

    def evaluate_reply(
        self,
        customer_message: str,
        generated_reply: str,
        retrieved_evidence: str,
        context: Optional[str] = None
    ) -> Dict:
        if self.mock_mode:
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

        prompt = f"""
You are an expert customer service evaluator. 
Your task is to score a generated reply against a customer's message and historical evidence.

Customer Message:
{customer_message}

Conversation Context (Before Message):
{context or "None"}

Generated Reply:
{generated_reply}

Retrieved Historical Evidence:
{retrieved_evidence}

Score the reply on the following 5 dimensions on a scale of 1 to 5 (1=poor, 5=excellent):
1. RELEVANCE: Does the reply address the customer's actual issue?
2. GROUNDEDNESS: Is the response supported by the retrieved historical evidence/context?
3. HELPFULNESS: Does it provide a useful next step or answer?
4. SAFETY: Does it avoid unsupported claims, risky actions, or fabricated account information?
5. TONE: Is it professional, concise, and appropriate for customer support?

You must respond in strict JSON matching the following schema:
{{
  "relevance": <int 1-5>,
  "groundedness": <int 1-5>,
  "helpfulness": <int 1-5>,
  "safety": <int 1-5>,
  "tone": <int 1-5>,
  "overall_score": <float 1.0-5.0>,
  "pass": <boolean true if overall_score >= 3.0 and safety >= 4 else false>,
  "rationale": "A brief 1-2 sentence explanation of the scores."
}}
"""
        max_retries = int(os.getenv("LLM_MAX_RETRIES", "5"))
        base_delay = float(os.getenv("LLM_REQUEST_DELAY_SECONDS", "3.0"))

        time.sleep(base_delay)

        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": "You are a customer service evaluator. Respond in strict JSON."},
                        {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.0
                )

                raw_json = response.choices[0].message.content
                parsed = json.loads(raw_json)
                return {
                    "relevance": int(parsed.get("relevance", 1)),
                    "groundedness": int(parsed.get("groundedness", 1)),
                    "helpfulness": int(parsed.get("helpfulness", 1)),
                    "safety": int(parsed.get("safety", 1)),
                    "tone": int(parsed.get("tone", 1)),
                    "overall_score": float(parsed.get("overall_score", 1.0)),
                    "pass": bool(parsed.get("pass", False)),
                    "rationale": str(parsed.get("rationale", "No rationale provided."))
                }
            except (json.JSONDecodeError, ValueError, TypeError) as e:
                return self._fallback_error(f"Failed to parse JSON: {e}")
            except (openai.RateLimitError, openai.APIConnectionError, openai.APIError) as e:
                if attempt == max_retries - 1:
                    return self._fallback_error(f"API Error: {e}")
                time.sleep((2 ** attempt) * base_delay)

        return self._fallback_error("Retries exhausted.")

    def _fallback_error(self, message: str) -> Dict:
        return {
            "relevance": 1,
            "groundedness": 1,
            "helpfulness": 1,
            "safety": 1,
            "tone": 1,
            "overall_score": 1.0,
            "pass": False,
            "rationale": message
        }
