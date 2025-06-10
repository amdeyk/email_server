from fastapi import APIRouter, UploadFile, File, Depends
from ..security.api_key import verify_api_key

router = APIRouter(
    prefix="/api/uploads",
    tags=["uploads"],
    dependencies=[Depends(verify_api_key)],
)

@router.post("/csv")
async def upload_csv(file: UploadFile = File(...)):
    return {"filename": file.filename}

@router.post("/images")
async def upload_image(file: UploadFile = File(...)):
    return {"filename": file.filename}

@router.get("/validate-csv")
async def validate_csv():
    return {"valid": True}
