# Kolably Backend

Local Business × Creator Collaboration Marketplace — **FastAPI Backend**

## Quick Start

```bash
# 1. Create virtual environment
python -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Copy env and configure
cp .env.example .env

# 4. Run development server
uvicorn app.main:app --reload

# 5. Open docs
# → http://127.0.0.1:8000/docs
```

## Project Structure

```
kolably_backend/
├── app/
│   ├── main.py                  # FastAPI entry point
│   ├── api/
│   │   ├── router.py            # Aggregate API router (/api/v1)
│   │   └── routes/
│   │       ├── auth.py           # Signup, login, tokens
│   │       ├── users.py          # Current-user operations
│   │       ├── creators.py       # Creator profiles & portfolio
│   │       ├── businesses.py     # Business profiles
│   │       ├── campaigns.py      # Campaign CRUD & feed
│   │       ├── applications.py   # Apply / accept / reject
│   │       ├── collaborations.py # Collab lifecycle
│   │       └── chat.py           # Messaging
│   ├── core/
│   │   ├── config.py             # Pydantic settings
│   │   ├── security.py           # JWT & password utils
│   │   ├── supabase.py           # Supabase client init
│   │   ├── dependencies.py       # FastAPI DI (auth, DB)
│   │   └── exceptions.py         # Custom HTTP exceptions
│   ├── schemas/                  # Pydantic request/response models
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── creator.py
│   │   ├── business.py
│   │   ├── campaign.py
│   │   ├── application.py
│   │   ├── collaboration.py
│   │   ├── chat.py
│   │   └── common.py
│   └── services/                 # Business logic layer
│       ├── auth_service.py
│       ├── creator_service.py
│       ├── business_service.py
│       ├── campaign_service.py
│       ├── application_service.py
│       ├── collaboration_service.py
│       └── chat_service.py
├── tests/
│   ├── conftest.py               # Shared fixtures
│   └── test_health.py            # Smoke test
├── pyproject.toml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## API Docs

Once running, visit:

| Docs | URL |
|------|-----|
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |
| Health Check | `http://127.0.0.1:8000/health` |

## Running Tests

```bash
pip install -e ".[dev]"
pytest
```
