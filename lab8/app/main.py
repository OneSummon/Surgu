import uvicorn
from contextlib import asynccontextmanager
from database.database import engine
from database.models import Base
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.nodes import router as nodes_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("База данных инициализирована")

    yield

    await engine.dispose()
    print("База данных закрыта")

app = FastAPI(lifespan=lifespan)

# middleware cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://127.0.0.1",
        "http://127.0.0.1:5500",
        "http://localhost:5000",
        "null"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# include routers
app.include_router(nodes_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)