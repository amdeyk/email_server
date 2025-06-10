from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .config import get_settings
from .utils.logger import configure_logging

settings = get_settings()
configure_logging(settings.log_level)

app = FastAPI(title="Mass Email Server")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = settings.database_url if settings.env == "development" else settings.postgres_url
if settings.env == "development" and DATABASE_URL.startswith("sqlite"):
    DATABASE_URL = DATABASE_URL.replace("sqlite://", "sqlite+aiosqlite://")
engine = create_async_engine(DATABASE_URL, echo=False, future=True)
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

@app.middleware("http")
async def db_session_middleware(request, call_next):
    response = None
    request.state.db = AsyncSessionLocal()
    try:
        response = await call_next(request)
    finally:
        await request.state.db.close()
    return response

@app.get("/")
async def root():
    return {"message": "Mass Email Server running"}
