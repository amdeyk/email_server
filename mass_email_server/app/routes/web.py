from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.database import EmailCampaign

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()


@router.get("/recipients", response_class=HTMLResponse)
async def recipients_page(request: Request):
    return templates.TemplateResponse("pages/contact_manager.html", {"request": request})


@router.get("/recipients/import", response_class=HTMLResponse)
async def recipients_import_page(request: Request):
    return templates.TemplateResponse("pages/recipient_import.html", {"request": request})


@router.get("/campaigns/monitor", response_class=HTMLResponse)
async def campaign_monitor_page(request: Request):
    return templates.TemplateResponse("pages/campaign_monitor.html", {"request": request})

@router.get("/campaigns", response_class=HTMLResponse)
async def campaigns_page(request: Request):
    db: AsyncSession = request.state.db
    result = await db.execute(select(EmailCampaign))
    campaigns = result.scalars().all()
    return templates.TemplateResponse(
        "pages/campaigns.html",
        {"request": request, "campaigns": campaigns},
    )

@router.get("/campaigns/new", response_class=HTMLResponse)
async def new_campaign_form(request: Request):
    return templates.TemplateResponse("pages/campaign_wizard.html", {"request": request})

@router.post("/campaigns/new")
async def create_campaign_form(request: Request, name: str = Form(...), subject: str = Form(...), html_content: str = Form(...)):
    db: AsyncSession = request.state.db
    campaign = EmailCampaign(name=name, subject=subject, html_content=html_content)
    db.add(campaign)
    await db.commit()
    return RedirectResponse(url="/campaigns", status_code=303)


@router.get("/templates/editor", response_class=HTMLResponse)
async def template_editor(request: Request):
    return templates.TemplateResponse("pages/template_editor.html", {"request": request})
