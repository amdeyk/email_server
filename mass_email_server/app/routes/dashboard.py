from fastapi import APIRouter, Depends
from ..security.api_key import verify_api_key

router = APIRouter(
    prefix="/api/dashboard",
    tags=["dashboard"],
    dependencies=[Depends(verify_api_key)],
)

@router.get("/metrics")
async def get_metrics():
    return {"metrics": []}

@router.get("/recent-activity")
async def get_recent_activity():
    return {"recent": []}

@router.get("/system-status")
async def get_system_status():
    return {"status": "ok"}
