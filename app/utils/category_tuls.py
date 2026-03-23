from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.catschem import CatSchema, CatResponse
from database import get_db
from models.model import Category
from sqlalchemy import select
from fastapi import HTTPException


async def create_cat(category: CatSchema, db: AsyncSession = Depends(get_db)):
    cat_data = category.model_dump()
    cat_db = Category(**cat_data)
    db.add(cat_db)
    await db.commit()
    await db.refresh(cat_db)
    return cat_db


async def get_cat(category_name: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Category).filter(Category.name == category_name))
    db_cat = result.scalar_one_or_none()
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return db_cat


async def get_all_cat(db: AsyncSession):  # на доработку
    result = await db.execute(select(Category))
    all_cat = result.scalars().all()
    return all_cat


async def del_cat(category_name: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Category).filter(Category.name == category_name))
    db_cat = result.scalar_one_or_none()
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Category not found")

    await db.delete(db_cat)
    await db.commit()

    return db_cat
