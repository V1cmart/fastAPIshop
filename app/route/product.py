from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.prodschem import ProductBase
from database import get_db
from models.model import Product

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=ProductBase)
async def create_product(product: ProductBase, db: AsyncSession = Depends(get_db)):
    prod_data = product.model_dump()
    prod_db = Product(**prod_data)
    db.add(prod_db)
    await db.commit()
    await db.refresh(prod_db)
    return prod_db
