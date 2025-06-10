from fastapi import APIRouter, Depends
from ..security.api_key import verify_api_key

router = APIRouter(
    prefix="/api/settings",
    tags=["settings"],
    dependencies=[Depends(verify_api_key)],
)

@router.get("")
async def get_settings():
    return {"settings": {}}

@router.post("")
async def update_settings(payload: dict):
    return {"updated": payload}
