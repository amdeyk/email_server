from fastapi import APIRouter, Depends, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..security.api_key import verify_api_key
from ..models.database import CampaignAnalytics

router = APIRouter(
    prefix="/api/analytics",
    tags=["analytics"],
    dependencies=[Depends(verify_api_key)],
)

@router.get("/campaign/{id}")
async def campaign_analytics(id: int, request: Request):
    db: AsyncSession = request.state.db
    result = await db.execute(select(CampaignAnalytics).where(CampaignAnalytics.campaign_id == id))
    records = result.scalars().all()
    analytics = [
        {
            "metric_name": r.metric_name,
            "metric_value": r.metric_value,
            "recorded_at": r.recorded_at,
        }
        for r in records
    ]
    return {"campaign": id, "analytics": analytics}
