import toml
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
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


@app.get("/", response_class=RedirectResponse, status_code=302)
async def index(request: Request) -> None:
    return "https://github.com/SuperOrca/orca-api"
