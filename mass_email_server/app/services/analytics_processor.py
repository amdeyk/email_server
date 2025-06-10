"""Simple analytics processing utilities."""

from collections import defaultdict
from datetime import date
from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from ..models.database import EmailLog, CampaignAnalytics


class AnalyticsProcessor:
    """Process email events and update summary analytics."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def aggregate_daily(self, campaign_id: int):
        """Aggregate email logs for a campaign by day."""
        result = await self.db.execute(
            select(
                func.date(EmailLog.timestamp).label("day"),
                func.count().label("total_sent"),
            ).where(EmailLog.campaign_id == campaign_id)
            .group_by(func.date(EmailLog.timestamp))
        )
        records = result.all()
        for day, total in records:
            await self.db.merge(
                CampaignAnalytics(
                    campaign_id=campaign_id,
                    metric_name="sent",
                    metric_value=total,
                    recorded_at=day,
                )
            )
        await self.db.commit()

    async def summarize(self, campaign_id: int):
        """Return aggregated metrics for dashboard use."""
        result = await self.db.execute(
            select(
                func.count().label("sent"),
                func.sum(func.case((EmailLog.status == "delivered", 1), else_=0)).label("delivered"),
                func.sum(func.case((EmailLog.status == "opened", 1), else_=0)).label("opened"),
                func.sum(func.case((EmailLog.status == "clicked", 1), else_=0)).label("clicked"),
                func.sum(func.case((EmailLog.status == "bounced", 1), else_=0)).label("bounced"),
            ).where(EmailLog.campaign_id == campaign_id)
        )
        return result.first()
