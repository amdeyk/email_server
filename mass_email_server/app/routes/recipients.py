import csv
from fastapi import APIRouter, UploadFile, File, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ..models.database import EmailRecipient
from ..models.email_models import EmailRecipientCreate
from ..security.api_key import verify_api_key

router = APIRouter(
    prefix="/api/recipients",
    tags=["recipients"],
    dependencies=[Depends(verify_api_key)],
)

@router.post("/import")
async def import_recipients(file: UploadFile = File(...), request: Request = None):
    db: AsyncSession = request.state.db
    content = await file.read()
    reader = csv.DictReader(content.decode().splitlines())
    count = 0
    for row in reader:
        recipient = EmailRecipient(email=row.get("email"), name=row.get("name"))
        db.add(recipient)
        count += 1
    await db.commit()
    return {"imported": count}

@router.get("")
async def list_recipients(request: Request):
    db: AsyncSession = request.state.db
    result = await db.execute(select(EmailRecipient))
    recipients = result.scalars().all()
    return [{"id": r.id, "email": r.email, "name": r.name} for r in recipients]

@router.post("")
async def add_recipient(recipient: EmailRecipientCreate, request: Request):
    db: AsyncSession = request.state.db
    rec = EmailRecipient(email=recipient.email, name=recipient.name)
    db.add(rec)
    await db.commit()
    await db.refresh(rec)
    return {"id": rec.id}

@router.delete("/{recipient_id}")
async def delete_recipient(recipient_id: int, request: Request):
    db: AsyncSession = request.state.db
    result = await db.execute(select(EmailRecipient).where(EmailRecipient.id == recipient_id))
    rec = result.scalar_one_or_none()
    if rec:
        await db.delete(rec)
        await db.commit()
        return {"deleted": True}
    return {"deleted": False}
