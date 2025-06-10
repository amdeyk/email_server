import aiosmtplib
from typing import Optional
from ..config import get_settings
from ..utils.logger import logging

settings = get_settings()

class SMTPService:
    def __init__(self):
        self.host = settings.smtp_host
        self.port = settings.smtp_port
        self.username = settings.smtp_username
        self.password = settings.smtp_password
        self.tls = True
        self.client: Optional[aiosmtplib.SMTP] = None

    async def connect(self) -> None:
        self.client = aiosmtplib.SMTP(hostname=self.host, port=self.port, use_tls=False, start_tls=self.tls)
        await self.client.connect()
        if self.username:
            await self.client.login(self.username, self.password)
        logging.getLogger(__name__).info("Connected to SMTP server %s", self.host)

    async def disconnect(self) -> None:
        if self.client:
            await self.client.quit()
            logging.getLogger(__name__).info("Disconnected from SMTP server")

    async def test_connection(self) -> bool:
        try:
            await self.connect()
            await self.disconnect()
            return True
        except Exception as exc:
            logging.getLogger(__name__).exception("SMTP connection failed: %s", exc)
            return False
