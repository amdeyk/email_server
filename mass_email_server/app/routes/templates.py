from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.database import EmailTemplate
from ..models.email_models import EmailTemplateCreate
from ..security.api_key import verify_api_key

router = APIRouter(
    prefix="/api/templates",
    tags=["templates"],
    dependencies=[Depends(verify_api_key)],
)

@router.post("", status_code=201)
async def create_template(template: EmailTemplateCreate, request: Request):
    db: AsyncSession = request.state.db
    new_tmpl = EmailTemplate(
        name=template.name,
        html_content=template.html_content,
        variables=template.variables,
    )
    db.add(new_tmpl)
    await db.commit()
    await db.refresh(new_tmpl)
    return {"id": new_tmpl.id}

@router.get("")
async def list_templates(request: Request):
    db: AsyncSession = request.state.db
    result = await db.execute(select(EmailTemplate))
    templates = result.scalars().all()
    return [
        {"id": t.id, "name": t.name, "variables": t.variables}
        for t in templates
    ]

@router.get("/{template_id}")
async def get_template(template_id: int, request: Request):
    db: AsyncSession = request.state.db
    result = await db.execute(select(EmailTemplate).where(EmailTemplate.id == template_id))
    template = result.scalar_one_or_none()
    if template is None:
        raise HTTPException(status_code=404, detail="Template not found")
    return {
        "id": template.id,
        "name": template.name,
        "html_content": template.html_content,
        "variables": template.variables,
    }
