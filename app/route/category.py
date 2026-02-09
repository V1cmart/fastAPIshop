from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.catschem import CatSchema, CatResponse
from database import get_db
from models.model import Category
from route import category

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/", response_model=CatResponse)
async def create_category(category: CatSchema, db: AsyncSession = Depends(get_db)):
    cat_data = category.model_dump()
    cat_db = Category(**cat_data)
    db.add(cat_db)
    await db.commit()
    await db.refresh(cat_db)
    return cat_db
