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

## Template Editor

The web interface now includes a template editor powered by [GrapesJS](https://github.com/GrapesJS/grapesjs).
Visit `/templates/editor` to design HTML emails with drag-and-drop blocks. Templates can also be rendered with MJML and have their CSS inlined using `premailer`.

## Tests

Run tests with:
```bash
pytest
```
