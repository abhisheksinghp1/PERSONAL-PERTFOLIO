# Portfolio Project — Professional Refactor Plan

## Current Issues

1. **Backend folder naming inconsistency** — `Backend/` vs `backend/` (Windows case-insensitive but Git/Linux sees both)
2. **Missing professional structure** — no tests, no docs, no proper logging, no .dockerignore
3. **Frontend organization** — all components flat in one folder
4. **No CI/CD config** — no GitHub Actions for automated testing
5. **Missing production configs** — no Docker, no nginx, no health checks
6. **No monitoring/logging** — no structured logging, no error tracking
7. **Security** — hardcoded secrets in code, weak password hashing (SHA256 instead of bcrypt)

---

## New Professional Structure

```
portfolio/
├── .github/
│   └── workflows/
│       ├── backend-ci.yml          # Auto-test backend on PR
│       └── frontend-ci.yml         # Auto-test frontend on PR
│
├── backend/                         # Lowercase, consistent naming
│   ├── .env.example                # Template for environment variables
│   ├── .dockerignore
│   ├── .python-version             # Python 3.11.9
│   ├── Dockerfile                  # Production-ready Docker image
│   ├── requirements.txt            # Pinned dependencies
│   ├── requirements-dev.txt        # Dev dependencies (pytest, black, etc.)
│   │
│   ├── alembic/                    # Database migrations (optional upgrade)
│   │   ├── versions/
│   │   └── env.py
│   │
│   ├── app/                        # Main application package
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI app entry
│   │   ├── config.py               # Settings with pydantic-settings
│   │   ├── dependencies.py         # Dependency injection
│   │   │
│   │   ├── api/                    # API routes (versioned)
│   │   │   ├── __init__.py
│   │   │   └── v1/
│   │   │       ├── __init__.py
│   │   │       ├── router.py       # Main router aggregator
│   │   │       └── endpoints/
│   │   │           ├── __init__.py
│   │   │           ├── auth.py
│   │   │           ├── skills.py
│   │   │           ├── projects.py
│   │   │           ├── contact.py
│   │   │           └── ...
│   │   │
│   │   ├── core/                   # Core utilities
│   │   │   ├── __init__.py
│   │   │   ├── security.py         # JWT, password hashing
│   │   │   ├── logging.py          # Structured logging setup
│   │   │   └── exceptions.py       # Custom exceptions
│   │   │
│   │   ├── db/                     # Database
│   │   │   ├── __init__.py
│   │   │   ├── database.py         # Connection management
│   │   │   ├── models.py           # SQLAlchemy models (optional)
│   │   │   └── init_db.py          # Database initialization
│   │   │
│   │   ├── schemas/                # Pydantic models (request/response)
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── skills.py
│   │   │   ├── projects.py
│   │   │   └── ...
│   │   │
│   │   ├── services/               # Business logic
│   │   │   ├── __init__.py
│   │   │   ├── email_service.py
│   │   │   ├── auth_service.py
│   │   │   └── storage_service.py
│   │   │
│   │   └── middleware/             # Custom middleware
│   │       ├── __init__.py
│   │       ├── cors.py
│   │       ├── rate_limit.py
│   │       └── error_handler.py
│   │
│   ├── tests/                      # Pytest tests
│   │   ├── __init__.py
│   │   ├── conftest.py             # Shared fixtures
│   │   ├── test_auth.py
│   │   ├── test_skills.py
│   │   └── ...
│   │
│   ├── scripts/                    # Utility scripts
│   │   ├── seed_db.py
│   │   └── backup_db.sh
│   │
│   └── uploads/                    # File storage (gitignored)
│       └── .gitkeep
│
├── frontend/                        # Renamed from portfolio-frontend
│   ├── .env.example
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── nginx.conf                  # Production nginx config
│   │
│   ├── public/
│   │   └── ...
│   │
│   ├── src/
│   │   ├── main.jsx
│   │   ├── App.jsx
│   │   ├── index.css
│   │   │
│   │   ├── assets/                 # Static assets
│   │   │   ├── images/
│   │   │   └── fonts/
│   │   │
│   │   ├── components/             # Organized by feature
│   │   │   ├── common/             # Reusable UI components
│   │   │   │   ├── Button/
│   │   │   │   │   ├── Button.jsx
│   │   │   │   │   └── Button.css
│   │   │   │   ├── Card/
│   │   │   │   ├── Modal/
│   │   │   │   └── Loader/
│   │   │   │
│   │   │   ├── layout/             # Layout components
│   │   │   │   ├── Navbar/
│   │   │   │   ├── Footer/
│   │   │   │   └── Cursor/
│   │   │   │
│   │   │   └── features/           # Feature-specific components
│   │   │       ├── hero/
│   │   │       │   ├── Hero.jsx
│   │   │       │   ├── Hero.css
│   │   │       │   └── HeroVideoCard.jsx
│   │   │       ├── skills/
│   │   │       │   ├── Skills.jsx
│   │   │       │   └── Skills.css
│   │   │       ├── projects/
│   │   │       ├── about/
│   │   │       ├── contact/
│   │   │       ├── resume/
│   │   │       ├── certifications/
│   │   │       └── admin/
│   │   │
│   │   ├── pages/                  # Route pages
│   │   │   ├── HomePage/
│   │   │   ├── AboutPage/
│   │   │   ├── SkillsPage/
│   │   │   └── ...
│   │   │
│   │   ├── context/                # React context
│   │   │   ├── AdminContext.jsx
│   │   │   ├── ProjectsContext.jsx
│   │   │   └── ThemeContext.jsx
│   │   │
│   │   ├── hooks/                  # Custom hooks
│   │   │   ├── useApi.js
│   │   │   ├── useAuth.js
│   │   │   └── useLocalStorage.js
│   │   │
│   │   ├── services/               # API clients
│   │   │   ├── api.js              # Axios/fetch wrapper
│   │   │   ├── authService.js
│   │   │   ├── skillsService.js
│   │   │   └── projectsService.js
│   │   │
│   │   ├── utils/                  # Helper functions
│   │   │   ├── validators.js
│   │   │   ├── formatters.js
│   │   │   └── constants.js
│   │   │
│   │   └── config/                 # Configuration
│   │       └── config.js
│   │
│   └── tests/                      # Vitest tests
│       └── ...
│
├── docs/                            # Documentation
│   ├── API.md                      # API documentation
│   ├── DEPLOYMENT.md               # Deployment guide
│   ├── DEVELOPMENT.md              # Local dev setup
│   └── ARCHITECTURE.md             # System architecture
│
├── docker-compose.yml              # Local development with Docker
├── .gitignore
├── .editorconfig                   # Consistent editor settings
├── README.md                       # Project overview
└── LICENSE

```

---

## Implementation Steps

### Step 1 — Clean Up Root Level
- Remove duplicate `backend/` folder (keep only `Backend/` or rename to lowercase)
- Add `.editorconfig`, `.gitattributes` for consistency
- Create proper README with badges, setup instructions, screenshots

### Step 2 — Backend Refactor
- Rename `Backend/` → `backend/` (consistent lowercase)
- Reorganize into `app/` package structure
- Split `models.py` into `schemas/` (Pydantic) and `db/models.py` (SQLAlchemy if needed)
- Move routers into `app/api/v1/endpoints/`
- Add proper logging with structlog or loguru
- Replace SHA256 with bcrypt for passwords
- Add environment variable validation
- Add health check endpoint `/health`
- Add rate limiting middleware
- Add proper error handling with custom exceptions
- Write tests with pytest + coverage

### Step 3 — Frontend Refactor
- Rename `portfolio-frontend/` → `frontend/`
- Organize components by feature, not type
- Create reusable UI components in `components/common/`
- Extract API calls into `services/`
- Create custom hooks for repeated logic
- Add proper error boundaries
- Add loading states and skeleton screens
- Add input validation with react-hook-form or Zod
- Write tests with Vitest + React Testing Library

### Step 4 — Add Professional Tooling
- **Backend:**
  - Black (code formatting)
  - Ruff (linting)
  - mypy (type checking)
  - pytest + pytest-cov (testing)
  - pre-commit hooks

- **Frontend:**
  - ESLint + Prettier
  - Husky + lint-staged (pre-commit hooks)
  - Vitest (testing)
  - TypeScript (optional but recommended)

### Step 5 — Add DevOps
- Dockerfile for backend (multi-stage build)
- Dockerfile for frontend (nginx-based)
- docker-compose.yml for local dev
- GitHub Actions for CI/CD
- Health checks for monitoring

### Step 6 — Documentation
- API docs (auto-generated from FastAPI)
- Architecture diagrams
- Setup guide for developers
- Deployment guide for production

---

## Benefits of This Structure

✅ **Scalability** — Easy to add new features without cluttering
✅ **Maintainability** — Clear separation of concerns
✅ **Testability** — Each module can be tested in isolation
✅ **Collaboration** — Multiple developers can work without conflicts
✅ **Production-ready** — Includes logging, monitoring, security best practices
✅ **Professional** — Follows industry standards (FastAPI best practices, React patterns)

---

## Do You Want Me To:

1. **Quick fix** — Just rename folders and add missing professional files (`.dockerignore`, `.editorconfig`, health checks)
2. **Full refactor** — Implement the entire new structure above (will take multiple steps)
3. **Incremental** — Refactor backend first, then frontend later

Let me know which approach you prefer!
