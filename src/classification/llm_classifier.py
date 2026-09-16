import os
import json
import hashlib
from typing import Dict, List, Optional
import time
import openai
from openai import OpenAI
from pydantic import BaseModel, Field

class IntentResult(BaseModel):
    intent: str = Field(description="The assigned intent ID from the taxonomy.")
    confidence: float = Field(description="Confidence score from 0.0 to 1.0.")
    reason: str = Field(description="Short explanation for the classification.")

class LLMClassifier:
    def __init__(self, taxonomy_path: str = "configs/intents.json", cache_dir: str = "cache", mock_mode: bool = False):
        self.mock_mode = mock_mode
        self.cache_dir = cache_dir
        self.cache_file = os.path.join(cache_dir, "llm_cache.json")
        self.taxonomy = self._load_taxonomy(taxonomy_path)
        self.valid_intents = [intent['id'] for intent in self.taxonomy['intents']]
        
        os.makedirs(self.cache_dir, exist_ok=True)
        self.cache = self._load_cache()
        
        if not self.mock_mode:
            api_key = (os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY") or "").strip().strip('"\'')
            base_url = os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
            self.client = OpenAI(
                api_key=api_key,
                base_url=base_url
            )
            self.model_name = os.getenv("LLM_MODEL", "openai/gpt-4o-mini")
            
        self.system_prompt = self._build_system_prompt()
        
        # Track usage
        self.api_calls_made = 0
        self.cache_hits = 0

    def _load_taxonomy(self, path: str) -> dict:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _load_cache(self) -> dict:
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def _save_cache(self):
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, indent=2)

    def _build_system_prompt(self) -> str:
        prompt = (
            "You are an expert AI customer support agent for AmazonHelp.\n"
            "Your task is to classify incoming customer messages into exactly one of the following intents.\n"
            "Do NOT invent new intents. Do NOT output arbitrary prose. You must respond in strict JSON.\n\n"
            "## TAXONOMY\n"
        )
        for intent in self.taxonomy['intents']:
            prompt += f"- **{intent['id']}**: {intent['description']}\n"
            prompt += f"  - Inclusion: {', '.join(intent['inclusion_criteria'])}\n"
            prompt += f"  - Exclusion: {', '.join(intent['exclusion_criteria'])}\n\n"
            
        prompt += (
            "## INSTRUCTIONS\n"
            "1. Classify the customer's *underlying support problem*, not just isolated keywords.\n"
            "2. If conversation context is provided, use it to understand fragments like 'Done' or 'Thanks', but your classification must represent the goal of the target message.\n"
            "3. If the intent genuinely cannot be determined or is out of scope (like praise, spam, or fragments with no context), classify as 'OTHER'.\n"
            "4. For ambiguous cases, choose the best-supported intent but lower your confidence score.\n"
        )
        return prompt

    def _get_cache_key(self, target_message: str, context: Optional[str]) -> str:
        # Cache key depends on target, context, and the taxonomy version to ensure freshness if taxonomy changes
        raw = f"{target_message}|||{context or ''}|||{self.taxonomy.get('version', '1.0')}"
        return hashlib.sha256(raw.encode('utf-8')).hexdigest()

    def classify(self, target_message: str, context: Optional[str] = None, use_cache: bool = True) -> IntentResult:
        cache_key = self._get_cache_key(target_message, context)
        
        if use_cache and cache_key in self.cache:
            self.cache_hits += 1
            data = self.cache[cache_key]
            return IntentResult(**data)
            
        if self.mock_mode:
            # Fake response for dry runs
            result = IntentResult(intent="OTHER", confidence=1.0, reason="Mock mode response")
            return result
            
        # Format user prompt
        user_content = f"Target Customer Message: {target_message}\n"
        if context:
            user_content = f"Conversation Context:\n{context}\n\n" + user_content
            
        self.api_calls_made += 1
        
        max_retries = int(os.getenv("LLM_MAX_RETRIES", "5"))
        base_delay = float(os.getenv("LLM_REQUEST_DELAY_SECONDS", "3.0"))
        
        # Pace baseline requests to avoid bursting rate limits
        if not self.mock_mode:
            time.sleep(base_delay)
            
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": user_content}
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.0
                )
                
                raw_json = response.choices[0].message.content
                try:
                    parsed = json.loads(raw_json)
                    intent = parsed.get("intent", "OTHER")
                    confidence = float(parsed.get("confidence", 0.0))
                    reason = str(parsed.get("reason", "No reason provided."))
                    
                    if intent not in self.valid_intents:
                        intent = "OTHER"
                        reason = f"Model returned invalid intent '{parsed.get('intent')}'. Fallback to OTHER. Original reason: {reason}"
                        
                    result = IntentResult(intent=intent, confidence=confidence, reason=reason)
                    
                    # Save to cache
                    self.cache[cache_key] = result.model_dump()
                    
                    # Save to disk every 10 calls to prevent massive loss on crash
                    if self.api_calls_made % 10 == 0:
                        self._save_cache()
                        
                    return result
                    
                except (json.JSONDecodeError, ValueError, TypeError) as e:
                    return IntentResult(intent="OTHER", confidence=0.0, reason=f"Failed to parse LLM response: {str(e)}")
                    
            except (openai.RateLimitError, openai.APIConnectionError, openai.APIError) as e:
                if attempt == max_retries - 1:
                    raise  # bubble up if max retries exceeded
                sleep_time = (2 ** attempt) * base_delay
                print(f"API Error encountered ({type(e).__name__}). Retrying in {sleep_time} seconds (Attempt {attempt + 1}/{max_retries})...")
                time.sleep(sleep_time)
            
    def flush_cache(self):
        """Save any remaining items to disk."""
        if not self.mock_mode:
            self._save_cache()
