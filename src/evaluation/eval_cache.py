"""
eval_cache.py — Persistent, hash-keyed cache for evaluation results.

Each component (classifier, generator, judge) has its own cache namespace
so they can be invalidated independently.  Cache files live in:
  cache/eval_classifier.json
  cache/eval_generator.json
  cache/eval_judge.json
"""

import hashlib
import json
import os
from typing import Any, Dict, Optional


class EvalCache:
    def __init__(self, namespace: str, cache_dir: str = "cache"):
        self.path = os.path.join(cache_dir, f"eval_{namespace}.json")
        os.makedirs(cache_dir, exist_ok=True)
        self._data: Dict[str, Any] = self._load()

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    def _load(self) -> Dict[str, Any]:
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                return {}
        return {}

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=2)

    # ------------------------------------------------------------------
    # Key generation
    # ------------------------------------------------------------------
    @staticmethod
    def make_key(*parts: str) -> str:
        raw = "|||".join(p or "" for p in parts)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    # ------------------------------------------------------------------
    # Cache operations
    # ------------------------------------------------------------------
    def get(self, key: str) -> Optional[Any]:
        return self._data.get(key)

    def set(self, key: str, value: Any, autosave: bool = False):
        self._data[key] = value
        if autosave:
            self.save()

    def has(self, key: str) -> bool:
        return key in self._data

    def __len__(self) -> int:
        return len(self._data)
