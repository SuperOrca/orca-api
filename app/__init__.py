from __future__ import annotations

from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import PlainTextResponse

from .utils import API

from .routers import fun

app = API()


@app.get("/", include_in_schema=False)
async def index():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - Swagger UI",
        swagger_css_url="https://cdn.jsdelivr.net/gh/Itz-fork/Fastapi-Swagger-UI-Dark/assets/swagger_ui_dark.min.css",
    )


@app.get("/ping", response_class=PlainTextResponse, summary="Pong!", tags=["General"])
async def ping():
    return "Pong!"


app.include_router(fun.router)
