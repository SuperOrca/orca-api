from __future__ import annotations

import random
from typing import Dict, Optional

import orjson
from app.utils import limiter
from fastapi import APIRouter, HTTPException, Request

with open("data/dj.json", "r") as file:
    dj = orjson.loads(file.read())

with open("data/wyr.json", "r") as file:
    wyr = orjson.loads(file.read())

with open("data/8ball.json", "r") as file:
    _8ball_responses = orjson.loads(file.read())

router = APIRouter(tags=["Fun"])


@router.get("/dj", summary="Get dad jokes.", description="Limit: `3/second`")
@limiter.limit("3/second")
async def _dj(request: Request, amount: Optional[int] = 1) -> Dict:
    if amount < 1:  # min amount
        raise HTTPException(status_code=400, detail="The amount is less than 1.")

    if amount > 50:  # max amount
        raise HTTPException(status_code=400, detail="The amount is greater than 50.")

    return {"amount": amount, "jokes": random.sample(dj, amount)}


@router.get(
    "/wyr", summary="Get would you rather questions.", description="Limit: `3/second`"
)
@limiter.limit("3/second")
async def _wyr(request: Request, amount: Optional[int] = 1) -> Dict:
    if amount < 1:  # min amount
        raise HTTPException(status_code=400, detail="The amount is less than 1.")

    if amount > 50:  # max amount
        raise HTTPException(status_code=400, detail="The amount is greater than 50.")

    return {"amount": amount, "questions": random.sample(wyr, amount)}


@router.get("/8ball", summary="Get 8ball responses.", description="Limit: `3/second`")
@limiter.limit("3/second")
async def _8ball(request: Request, all: Optional[bool] = False) -> Dict:
    if all:
        return {"amount": len(_8ball_responses), "responses": _8ball_responses}
    else:
        return {"amount": 1, "responses": [random.choice(_8ball_responses)]}
