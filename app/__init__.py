import toml
from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from .limiter import limiter
from .routers import wyr

with open("config.toml", "r") as file:
    config = toml.load(file)

app = FastAPI(**config)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(wyr.router)
