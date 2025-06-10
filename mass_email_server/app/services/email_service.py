from email.message import EmailMessage
from jinja2 import Environment, FileSystemLoader
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.database import EmailLog
from ..config import get_settings
from .smtp_service import SMTPService
from ..utils.validators import is_valid_email
from ..utils.logger import logging

settings = get_settings()

env = Environment(loader=FileSystemLoader('templates/email_templates'))

class EmailService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.smtp_service = SMTPService()

    async def send_email(self, to_email: str, subject: str, template_name: str, context: dict) -> bool:
        if not is_valid_email(to_email):
            logging.getLogger(__name__).error("Invalid email: %s", to_email)
            return False

        template = env.get_template(template_name)
        html_content = template.render(**context)

        message = EmailMessage()
        message['From'] = settings.email_from
        message['To'] = to_email
        message['Subject'] = subject
        message.set_content(html_content, subtype='html')

        await self.smtp_service.connect()
        try:
            await self.smtp_service.client.send_message(message)
            logging.getLogger(__name__).info("Email sent to %s", to_email)
            return True
        except Exception as exc:
            logging.getLogger(__name__).exception("Failed to send email to %s: %s", to_email, exc)
            return False
        finally:
            await self.smtp_service.disconnect()
