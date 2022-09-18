import random

import orjson
from fastapi import APIRouter, HTTPException, Request

from ..limiter import limiter

with open("data/wyr.json", "r") as file:
    data = orjson.loads(file.read())

router = APIRouter(prefix="/wyr", tags=["wyr"])


@router.get("/")
@limiter.limit("3/second")
async def get_one(request: Request) -> dict:
    return {"question": random.choice(data)}


@router.get("/{amount}")
@limiter.limit("2/second")
async def get_amount(request: Request, amount: int) -> dict:
    if amount < 1:  # min amount
        raise HTTPException(status_code=400, detail="The amount is less than 1.")

    if amount > 50:  # max amount
        raise HTTPException(status_code=400, detail="The amount is greater than 50.")

    return {"amount": amount, "questions": random.sample(data, amount)}
