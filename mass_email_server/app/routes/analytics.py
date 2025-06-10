from fastapi import APIRouter, Depends
from ..security.api_key import verify_api_key

router = APIRouter(
    prefix="/api/analytics",
    tags=["analytics"],
    dependencies=[Depends(verify_api_key)],
)

@router.get("/campaign/{id}")
async def campaign_analytics(id: int):
    return {"campaign": id, "analytics": {}}
