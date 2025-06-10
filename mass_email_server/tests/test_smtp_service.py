import pytest
from app.services.smtp_service import SMTPService

@pytest.mark.asyncio
async def test_smtp_connection():
    service = SMTPService()
    result = await service.test_connection()
    assert isinstance(result, bool)
