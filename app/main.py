from fastapi import Depends, FastAPI
from sqlalchemy import select, text
from schemas.Userschem import UserResponse, UserCreate
from database import engine, get_db, init_db
import uvicorn
from sqlalchemy.ext.asyncio import AsyncSession
from models.model import User
from utils.security import hash_password, verify_password
from contextlib import asynccontextmanager
from route.auth import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
