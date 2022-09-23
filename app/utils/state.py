from __future__ import annotations

from typing import Any, Dict, Optional

from app.utils import Limiter, limiter
from fastapi.datastructures import State as FastState


class State(FastState):
    def __init__(self, state: Optional[Dict[str, Any]] = None):
        super().__init__(state)
        self.limiter: Limiter = limiter
