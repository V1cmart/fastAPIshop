import hashlib
from http.client import HTTPException
import bcrypt
from passlib.context import CryptContext

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends

from models.model import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.Userschem import UserResponse, UserCreate

from database import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    sha = hashlib.sha256(password.encode()).hexdigest()
    return bcrypt.hashpw(sha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    sha256_hash = hashlib.sha256(plain_password.encode()).hexdigest()
    return bcrypt.checkpw(sha256_hash.encode("utf-8"), hashed_password.encode("utf-8"))


async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().one_or_none()
    return db_user


async def fake_decode_token(token, db: AsyncSession):
    user = await get_user(int(token), db)
    return user


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)
):
    user = await fake_decode_token(token, db)
    if not user:
        raise HTTPException(detail="Invalid authentication credentials")

    return user
