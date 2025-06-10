from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.database import EmailCampaign
from ..models.email_models import EmailCampaignCreate
from ..security.api_key import verify_api_key

router = APIRouter(
    prefix="/api/campaigns",
    tags=["campaigns"],
    dependencies=[Depends(verify_api_key)],
)

@router.post("", status_code=201)
async def create_campaign(campaign: EmailCampaignCreate, request: Request):
    db: AsyncSession = request.state.db
    new_campaign = EmailCampaign(
        name=campaign.name,
        subject=campaign.subject,
        html_content=campaign.html_content,
    )
    db.add(new_campaign)
    await db.commit()
    await db.refresh(new_campaign)
    return {"id": new_campaign.id}

@router.get("")
async def list_campaigns(request: Request):
    db: AsyncSession = request.state.db
    result = await db.execute(select(EmailCampaign))
    campaigns = result.scalars().all()
    return [
        {
            "id": c.id,
            "name": c.name,
            "subject": c.subject,
            "status": c.status,
            "total_recipients": c.total_recipients,
        }
        for c in campaigns
    ]

@router.get("/{campaign_id}")
async def get_campaign(campaign_id: int, request: Request):
    db: AsyncSession = request.state.db
    result = await db.execute(select(EmailCampaign).where(EmailCampaign.id == campaign_id))
    campaign = result.scalar_one_or_none()
    if campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return {
        "id": campaign.id,
        "name": campaign.name,
        "subject": campaign.subject,
        "html_content": campaign.html_content,
        "status": campaign.status,
        "total_recipients": campaign.total_recipients,
    }
