from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.prodschem import ProductBase
from database import get_db
from models.model import Product
from sqlalchemy import select


async def create_prod(product: ProductBase, db: AsyncSession = Depends(get_db)):
    prod_data = product.model_dump()
    prod_db = Product(**prod_data)
    db.add(prod_db)
    await db.commit()
    await db.refresh(prod_db)
    return prod_db


async def get_prod(product_name: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).filter(product_name == Product.name))
    db_prod = result.scalar_one_or_none()
    if db_prod is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_prod


async def del_prod(product_name: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).filter(product_name == Product.name))
    db_prod = result.scalar_one_or_none()
    if db_prod is None:
        raise HTTPException(status_code=404, detail="Product not found")

    await db.delete(db_prod)
    await db.commit()

    return db_prod
