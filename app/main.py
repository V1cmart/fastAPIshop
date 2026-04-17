from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import init_db, close_db
import uvicorn

from contextlib import asynccontextmanager

from route.auth import router as auth_router
from route.category import router as category_router
from route.product import router as product_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

    yield

    await close_db()


app = FastAPI(lifespan=lifespan, title="ElectronicShop")

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://127.0.0.1:8000",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(category_router)
app.include_router(product_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

#   "name": "vicmart",
#   "email": "user211343@example.com",
#   "password": "555555555"
# }
# {
#   "name": "templar",
#   "email": "use4324325353r@example.com",
#   "created_at": "2026-03-11T10:02:03.786202",
#   "password: 7777777777"
#   "id": 22
# }
