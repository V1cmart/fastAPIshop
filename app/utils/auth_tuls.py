from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.Userschem import UserResponse, UserCreate
from models.model import User
from utils.security import (
    hash_password,
    verify_password,
    authenticate_user,
    create_access_token,
    Token,
)

from database import get_db

from utils.security import get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES

from typing import List

from dotenv import load_dotenv
from os import getenv
from datetime import timedelta


async def f_create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    hashed_password = hash_password(user.password)
    user_data = user.model_dump(exclude={"password"})
    user_data["hashed_password"] = hashed_password
    db_user = User(**user_data)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_all_usrs(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users


async def get_usr(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().one_or_none()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
