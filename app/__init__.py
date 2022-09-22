from __future__ import annotations

import toml
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from .limiter import limiter
from .routers import wyr, dj

with open("config.toml", "r") as file:
    config = toml.load(file)

app = FastAPI(openapi_url="/swagger.json", **config)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(wyr.router)
app.include_router(dj.router)


@app.get("/", include_in_schema=False)
async def index():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - Swagger UI",
        swagger_css_url="https://cdn.jsdelivr.net/gh/Itz-fork/Fastapi-Swagger-UI-Dark/assets/swagger_ui_dark.min.css",
    )
