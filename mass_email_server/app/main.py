from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .config import get_settings
from .utils.logger import configure_logging
from .routes.campaigns import router as campaigns_router
from .routes.templates import router as templates_router
from .routes.recipients import router as recipients_router
from .routes.web import router as web_router
from .routes.dashboard import router as dashboard_router
from .routes.uploads import router as uploads_router
from .routes.preview import router as preview_router
from .routes.analytics import router as analytics_router
from .routes.settings import router as settings_router
from .routes.realtime import router as realtime_router
from .routes.campaign_drafts import router as campaign_drafts_router

settings = get_settings()
configure_logging(settings.log_level)
templates = Jinja2Templates(directory="app/templates")

app = FastAPI(title="Mass Email Server")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(campaigns_router)
app.include_router(templates_router)
app.include_router(recipients_router)
app.include_router(web_router)
app.include_router(dashboard_router)
app.include_router(uploads_router)
app.include_router(preview_router)
app.include_router(campaign_drafts_router)
app.include_router(analytics_router)
app.include_router(settings_router)
app.include_router(realtime_router)

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

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    return templates.TemplateResponse("pages/dashboard.html", {"request": request})
