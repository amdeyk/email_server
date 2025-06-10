import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent.parent / 'logs'
LOG_DIR.mkdir(exist_ok=True)

LOG_FILES = {
    'email': LOG_DIR / 'email_sending.log',
    'error': LOG_DIR / 'errors.log',
    'access': LOG_DIR / 'access.log',
    'debug': LOG_DIR / 'debug.log',
}

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def configure_logging(level: str = 'INFO') -> None:
    for file in LOG_FILES.values():
        handler = RotatingFileHandler(file, maxBytes=1024*1024, backupCount=5)
        logging.basicConfig(
            level=level,
            format=FORMAT,
            handlers=[handler]
        )

    logging.getLogger('uvicorn.access').handlers.clear()
    access_handler = RotatingFileHandler(LOG_FILES['access'], maxBytes=1024*1024, backupCount=5)
    logging.getLogger('uvicorn.access').addHandler(access_handler)
