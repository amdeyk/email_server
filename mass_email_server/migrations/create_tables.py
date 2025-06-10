"""Simple script to create database tables"""
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from app.models import Base
from app.config import get_settings

settings = get_settings()
DATABASE_URL = settings.database_url
engine = create_async_engine(DATABASE_URL, echo=True)

async def run():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == '__main__':
    asyncio.run(run())
