from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.prodschem import ProductBase, ProductResponce
from database import get_db
from models.model import Product
from utils.product_tuls import create_prod, get_prod, del_prod

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=ProductResponce)
async def create_product(product: ProductBase, db: AsyncSession = Depends(get_db)):
    prod_db = await create_prod(product, db)
    return prod_db


@router.get("/get_product", response_model=ProductResponce)
async def get_product(product_name: str, db: AsyncSession = Depends(get_db)):
    prod_db = await get_prod(product_name, db)
    return prod_db


@router.delete("/del product", response_model=ProductResponce)
async def delete_product(product: str, db: AsyncSession = Depends(get_db)):
    result = await del_prod(product, db)
    return result
