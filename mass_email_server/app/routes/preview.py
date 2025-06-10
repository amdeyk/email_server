from fastapi import APIRouter, Depends
from ..security.api_key import verify_api_key

router = APIRouter(
    prefix="/api/preview",
    tags=["preview"],
    dependencies=[Depends(verify_api_key)],
)

@router.post("/email")
async def generate_preview():
    return {"preview": "<html></html>"}
