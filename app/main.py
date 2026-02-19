from fastapi import Depends, FastAPI

from schemas.Userschem import UserResponse, UserCreate
from database import init_db
import uvicorn


from contextlib import asynccontextmanager

from route.auth import router as auth_router
from route.category import router as category_router
from route.product import router as product_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(category_router)
app.include_router(product_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

{"name": "victortop", "email": "user466463@example.com", "password": "22222222"}

{"name": "masha", "email": "user121334@example.com", "password": "12345678"}
