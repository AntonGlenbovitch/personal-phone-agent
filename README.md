# Personal Phone-Answering AI Agent (FastAPI Skeleton)

Production-friendly project skeleton for a personal phone-answering AI agent using FastAPI.

## Tech stack

- Python 3.11+
- FastAPI
- Uvicorn
- python-dotenv
- websockets
- pydantic-settings
- pytest

## Project structure

```text
app/
  __init__.py
  main.py
  api/
    __init__.py
    health.py
  core/
    __init__.py
    config.py
  services/
    __init__.py
  models/
    __init__.py
  tests/
    __init__.py
    test_health.py
.env.example
requirements.txt
README.md
```

## Quickstart

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy environment template:

```bash
cp .env.example .env
```

4. Run the app:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

5. Verify health:

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

## Running tests

```bash
pytest -q
```

## Notes

- Twilio and OpenAI integrations are intentionally not implemented yet.
- `websockets` dependency is included for future real-time communication features.
