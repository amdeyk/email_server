import pytest
from app.services.email_service import EmailService
from app.main import AsyncSessionLocal

@pytest.mark.asyncio
async def test_email_service_connection():
    async with AsyncSessionLocal() as session:
        service = EmailService(session)
        result = await service.smtp_service.test_connection()
        assert isinstance(result, bool)
