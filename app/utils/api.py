from __future__ import annotations

import toml
from app.utils.state import State
from fastapi import FastAPI as Fast
from fastapi.responses import ORJSONResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

with open("config.toml", "r") as file:
    config = toml.load(file)


class API(Fast):
    def __init__(self) -> None:
        super().__init__(**config, default_response_class=ORJSONResponse)
        self.state: State = State()
        self.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
