from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.catschem import CatSchema, CatResponse
from database import get_db
from models.model import Category
from route import category
from sqlalchemy import select
from fastapi import HTTPException
from utils.category_tuls import create_cat, get_cat, del_cat
from typing import List

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/create", response_model=CatResponse)
async def create_category(category: CatSchema, db: AsyncSession = Depends(get_db)):
    new_cat = await create_cat(category, db)
    return new_cat


@router.get("/{category_name}", response_model=CatResponse)
async def get_category(category_name: str, db: AsyncSession = Depends(get_db)):
    result = await get_cat(category_name, db)
    return result


@router.delete("/cat", response_model=CatResponse)
async def delete_category(category_name: str, db: AsyncSession = Depends(get_db)):
    result = await del_cat(category_name, db)
    return result
