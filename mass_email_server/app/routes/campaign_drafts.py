from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.database import CampaignDraft
from ..models.email_models import CampaignDraftCreate
from ..security.api_key import verify_api_key

router = APIRouter(
    prefix="/api/campaigns/drafts",
    tags=["campaign_drafts"],
    dependencies=[Depends(verify_api_key)],
)

@router.post("", status_code=201)
async def create_draft(draft: CampaignDraftCreate, request: Request):
    db: AsyncSession = request.state.db
    new_draft = CampaignDraft(
        user_id=draft.user_id,
        wizard_data=str(draft.wizard_data),
        step_completed=draft.step_completed,
    )
    db.add(new_draft)
    await db.commit()
    await db.refresh(new_draft)
    return {"id": new_draft.id}

@router.get("/{draft_id}")
async def get_draft(draft_id: int, request: Request):
    db: AsyncSession = request.state.db
    result = await db.execute(select(CampaignDraft).where(CampaignDraft.id == draft_id))
    draft = result.scalar_one_or_none()
    if draft is None:
        raise HTTPException(status_code=404, detail="Draft not found")
    return {
        "id": draft.id,
        "user_id": draft.user_id,
        "wizard_data": draft.wizard_data,
        "step_completed": draft.step_completed,
    }

@router.put("/{draft_id}")
async def update_draft(draft_id: int, draft: CampaignDraftCreate, request: Request):
    db: AsyncSession = request.state.db
    result = await db.execute(select(CampaignDraft).where(CampaignDraft.id == draft_id))
    db_draft = result.scalar_one_or_none()
    if db_draft is None:
        raise HTTPException(status_code=404, detail="Draft not found")
    db_draft.wizard_data = str(draft.wizard_data)
    db_draft.step_completed = draft.step_completed
    await db.commit()
    return {"ok": True}
