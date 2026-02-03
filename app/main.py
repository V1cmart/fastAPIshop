from fastapi import Depends, FastAPI
from sqlalchemy import select, text
from database import engine, get_db, init_db
import uvicorn
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import User
from utils.security import hash_password, verify_password
from contextlib import asynccontextmanager
from routers import auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Код выполняется при запуске
    await init_db()

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
