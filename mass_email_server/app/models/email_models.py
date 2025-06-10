from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class EmailRecipientCreate(BaseModel):
    email: EmailStr
    name: Optional[str]

class EmailCampaignCreate(BaseModel):
    name: str
    subject: str
    html_content: str

class EmailTemplateCreate(BaseModel):
    name: str
    html_content: str
    variables: Optional[str]

class EmailLog(BaseModel):
    campaign_id: int
    recipient_email: EmailStr
    status: str
    error_message: Optional[str]
    timestamp: datetime

class CampaignDraftCreate(BaseModel):
    user_id: Optional[int] = None
    wizard_data: dict
    step_completed: int = 0

class CampaignAnalyticsCreate(BaseModel):
    campaign_id: int
    metric_name: str
    metric_value: float
    recorded_at: Optional[datetime] = None
