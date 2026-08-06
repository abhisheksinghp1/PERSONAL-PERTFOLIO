# Backend Migration Guide — From Flat to Professional Structure

This guide will help you reorganize the backend into a production-ready structure.

---

## Current Structure (Flat)
```
Backend/
├── main.py
├── database.py
├── models.py
├── config.py
├── auth.py
├── email_service.py
├── requirements.txt
└── routers/
    ├── auth.py
    ├── skills.py
    ├── projects.py
    └── ...
```

## Target Structure (Professional)
```
backend/                       # Renamed to lowercase
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI app
│   ├── config.py             # Settings
│   │
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── router.py
│   │       └── endpoints/
│   │           ├── auth.py
│   │           ├── skills.py
│   │           └── ...
│   │
│   ├── core/
│   │   ├── security.py      # JWT, bcrypt
│   │   ├── logging_config.py
│   │   └── exceptions.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── init_db.py
│   │
│   ├── schemas/             # Pydantic models
│   │   ├── auth.py
│   │   ├── skills.py
│   │   └── ...
│   │
│   └── services/
│       ├── email_service.py
│       └── storage_service.py
│
├── tests/
├── Dockerfile
├── .dockerignore
├── .env.example
├── requirements.txt
└── requirements-dev.txt
```

---

## Migration Steps

### Step 1 — Backup Current Code
```bash
cd C:\Users\HP\OneDrive\Desktop\Portfolio
cp -r Backend Backend_backup
```

### Step 2 — Create New Structure
```bash
cd Backend
mkdir -p app/api/v1/endpoints
mkdir -p app/core
mkdir -p app/db
mkdir -p app/schemas
mkdir -p app/services
mkdir -p tests
```

### Step 3 — Create `__init__.py` Files
```bash
# Windows PowerShell
New-Item app/__init__.py
New-Item app/api/__init__.py
New-Item app/api/v1/__init__.py
New-Item app/api/v1/endpoints/__init__.py
New-Item app/core/__init__.py
New-Item app/db/__init__.py
New-Item app/schemas/__init__.py
New-Item app/services/__init__.py
New-Item tests/__init__.py
```

### Step 4 — Move Files

#### 4.1 — Move `main.py`
```bash
# Keep the old one for now, we'll update it
cp main.py app/main.py
```

Then update `app/main.py`:
- Change all imports from `from routers import X` → `from app.api.v1.endpoints import X`
- Change `from database import init_db` → `from app.db.database import init_db`
- Change `from config import settings` → `from app.config import settings`

#### 4.2 — Move `database.py`
```bash
mv database.py app/db/database.py
```

Update imports in `app/db/database.py`:
- Change `from config import settings` → `from app.config import settings`

#### 4.3 — Move `config.py`
```bash
mv config.py app/config.py
```

#### 4.4 — Move Routers
```bash
# Move each router file
mv routers/auth.py app/api/v1/endpoints/auth.py
mv routers/skills.py app/api/v1/endpoints/skills.py
mv routers/projects.py app/api/v1/endpoints/projects.py
# ... repeat for all routers
```

Update imports in each endpoint file:
- Change `from database import get_db` → `from app.db.database import get_db`
- Change `from models import X` → `from app.schemas.X import X`
- Change `from routers.auth import require_admin` → `from app.api.v1.endpoints.auth import require_admin`

#### 4.5 — Split `models.py` into Schemas
```bash
mv models.py app/schemas/base.py
```

Then create separate schema files for each domain:
- `app/schemas/auth.py` — LoginRequest, TokenResponse
- `app/schemas/skills.py` — SkillIn, SkillOut, CategoryIn, CategoryOut
- `app/schemas/projects.py` — ProjectIn, ProjectUpdate
- `app/schemas/contact.py` — ContactRequest

#### 4.6 — Move Services
```bash
mv email_service.py app/services/email_service.py
```

Update imports in `app/services/email_service.py`:
- Change `from config import settings` → `from app.config import settings`

#### 4.7 — Move `auth.py` (security utilities)
```bash
mv auth.py app/core/security.py
```

Update imports and add bcrypt support (see Step 5)

### Step 5 — Upgrade Security (SHA256 → Bcrypt)

Replace password hashing in `app/core/security.py`:

**OLD (SHA256):**
```python
import hashlib
pw_hash = hashlib.sha256(password.encode()).hexdigest()
```

**NEW (Bcrypt):**
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)
```

Add `passlib[bcrypt]` to `requirements.txt`:
```
passlib[bcrypt]==1.7.4
```

### Step 6 — Create Router Aggregator

Create `app/api/v1/router.py`:
```python
from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth, skills, projects, contact, resume,
    documents, gallery, about, contact_links,
    resume_media, hero_video, code_card, certifications
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(skills.router, prefix="/skills", tags=["Skills"])
api_router.include_router(projects.router, prefix="/projects", tags=["Projects"])
api_router.include_router(contact.router, prefix="/contact", tags=["Contact"])
api_router.include_router(resume.router, prefix="/resume", tags=["Resume"])
api_router.include_router(documents.router, prefix="/documents", tags=["Documents"])
api_router.include_router(gallery.router, prefix="/gallery", tags=["Gallery"])
api_router.include_router(about.router, prefix="/about", tags=["About"])
api_router.include_router(contact_links.router, prefix="/contact-links", tags=["ContactLinks"])
api_router.include_router(resume_media.router, prefix="/resume-media", tags=["ResumeMedia"])
api_router.include_router(hero_video.router, prefix="/hero-video", tags=["HeroVideo"])
api_router.include_router(code_card.router, prefix="/code-card", tags=["CodeCard"])
api_router.include_router(certifications.router, prefix="/certifications", tags=["Certifications"])
```

### Step 7 — Update `app/main.py`

```python
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from pathlib import Path

from app.api.v1.router import api_router
from app.db.database import init_db, GALLERY_DIR, SKILL_IMAGES_DIR


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title="Abhishek Pratap Singh — Portfolio API",
    version="2.0.0",
    description="Professional portfolio backend with admin panel",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# CORS
frontend_url = os.getenv("FRONTEND_URL", "")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        *([frontend_url] if frontend_url else []),
        "*",  # Remove in production
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/uploads/gallery", StaticFiles(directory=str(GALLERY_DIR)), name="gallery")
app.mount("/uploads/skill_images", StaticFiles(directory=str(SKILL_IMAGES_DIR)), name="skill_images")

# API routes
app.include_router(api_router, prefix="/api")

# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "2.0.0"}

@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "Portfolio API v2 running",
        "docs": "/docs",
        "health": "/health"
    }
```

### Step 8 — Update Start Command

In Render, change the start command from:
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

To:
```
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### Step 9 — Test Locally

```bash
cd Backend
python -m uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` to verify all endpoints work.

### Step 10 — Commit & Deploy

```bash
git add .
git commit -m "refactor: reorganize backend into professional structure"
git push
```

Render will auto-redeploy with the new structure.

---

## Common Issues & Fixes

### Issue: `ModuleNotFoundError: No module named 'app'`
**Fix:** Make sure you're running from the `Backend/` directory and using `python -m uvicorn app.main:app`

### Issue: Import errors after moving files
**Fix:** Update all imports to use `app.` prefix. Search and replace:
- `from database import` → `from app.db.database import`
- `from models import` → `from app.schemas.X import`
- `from routers import` → `from app.api.v1.endpoints import`

### Issue: Static files not found
**Fix:** Verify `GALLERY_DIR` and `SKILL_IMAGES_DIR` paths in `app/db/database.py` are correct

---

## Next Steps After Migration

1. **Add Structured Logging** — Replace print statements with proper logging
2. **Add Tests** — Write pytest tests for each endpoint
3. **Add Rate Limiting** — Protect auth endpoints from brute force
4. **Add Input Sanitization** — Prevent XSS/SQL injection
5. **Switch to PostgreSQL** (optional) — For production scalability

---

**Need help with any step? Let me know!**
