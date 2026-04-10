from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import DB_URL

engine = create_async_engine(url=DB_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with async_session() as session:
        yield session