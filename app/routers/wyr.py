from __future__ import annotations

import random
from typing import Dict

import orjson
from fastapi import APIRouter, HTTPException, Request

from ..utils.limiter import limiter

with open("data/wyr.json", "r") as file:
    data = orjson.loads(file.read())

router = APIRouter(prefix="/wyr", tags=["Would You Rather?"])


@router.get(
    "/", summary="Get one would you rather question.", description="Limit: `3/second`"
)
@limiter.limit("3/second")
async def get_one(request: Request) -> Dict:
    return {"question": random.choice(data)}


@router.get(
    "/{amount}",
    summary="Get multiple would you rather questions.",
    description="Limit: `2/second`",
)
@limiter.limit("2/second")
async def get_amount(request: Request, amount: int) -> Dict:
    if amount < 1:  # min amount
        raise HTTPException(status_code=400, detail="The amount is less than 1.")

    if amount > 50:  # max amount
        raise HTTPException(status_code=400, detail="The amount is greater than 50.")

    return {"amount": amount, "questions": random.sample(data, amount)}
