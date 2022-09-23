from __future__ import annotations

from slowapi import Limiter as SlowLimiter
from slowapi.util import get_remote_address


class Limiter(SlowLimiter):
    def __init__(self) -> None:
        super().__init__(key_func=get_remote_address)


limiter = Limiter()
