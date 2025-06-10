# Mass Email Server

This is a FastAPI-based mass email server. It includes SMTP connection management, email templates, and database logging.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and modify values as needed.

3. Run database migrations:
   ```bash
   alembic upgrade head
   ```

4. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Tests

Run tests with:
```bash
pytest
```
