from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class EmailCampaign(Base):
    __tablename__ = 'email_campaigns'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    html_content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default='pending')
    total_recipients = Column(Integer, default=0)

    recipients = relationship('EmailRecipient', back_populates='campaign')

class EmailRecipient(Base):
    __tablename__ = 'email_recipients'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    name = Column(String)
    campaign_id = Column(Integer, ForeignKey('email_campaigns.id'))
    status = Column(String, default='pending')
    sent_at = Column(DateTime)
    opened_at = Column(DateTime)
    clicked_at = Column(DateTime)

    campaign = relationship('EmailCampaign', back_populates='recipients')

class EmailTemplate(Base):
    __tablename__ = 'email_templates'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    html_content = Column(Text, nullable=False)
    variables = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class EmailLog(Base):
    __tablename__ = 'email_logs'

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey('email_campaigns.id'))
    recipient_email = Column(String, nullable=False)
    status = Column(String)
    error_message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
