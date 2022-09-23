from __future__ import annotations

import random
from typing import Dict

import orjson
from fastapi import APIRouter, Request

from ..utils.limiter import limiter

with open("data/8ball.json", "r") as file:
    data = orjson.loads(file.read())

router = APIRouter(prefix="/8ball", tags=["8ball"])


@router.get("/", summary="Get one 8ball response.", description="Limit: `3/second`")
@limiter.limit("3/second")
async def get_one(request: Request) -> Dict:
    return {"response": random.choice(data)}


@router.get("/all", summary="Get all 8ball responses.", description="Limit: `2/second`")
@limiter.limit("2/second")
async def get_amount(request: Request) -> Dict:
    return {"amount": len(data), "responses": data}
