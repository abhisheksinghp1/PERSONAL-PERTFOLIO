# 🐍 Portfolio Backend API

FastAPI backend with PostgreSQL database for personal portfolio.

## 📁 This is the Backend Folder

**Deploy this folder separately on Render!**

---

## 🚀 Features

- ✅ FastAPI async framework
- ✅ PostgreSQL database (production) / SQLite (development)
- ✅ 13 RESTful API endpoints
- ✅ bcrypt password hashing
- ✅ SMTP email service
- ✅ File upload support
- ✅ Auto-generated Swagger docs
- ✅ Repository pattern
- ✅ CORS support

---

## 📋 API Endpoints

### Public Endpoints
- `GET /` - Health check
- `GET /health` - Service health status
- `GET /api/skills/` - Get all skills
- `GET /api/projects/` - Get all projects
- `GET /api/about/` - Get about cards
- `GET /api/contact-links/` - Get contact links
- `POST /api/contact/` - Send contact message

### Admin Endpoints (Requires Auth)
- `POST /api/auth/login` - Admin login
- `POST /api/skills/` - Create skill
- `PUT /api/skills/{id}` - Update skill
- `DELETE /api/skills/{id}` - Delete skill
- `POST /api/projects/` - Create project
- And more...

---

## 🛠️ Tech Stack

- **Framework:** FastAPI 0.115.5
- **Database:** PostgreSQL (production) / SQLite (local)
- **ORM:** SQLAlchemy 2.0.36 with asyncpg
- **Authentication:** bcrypt password hashing
- **Email:** SMTP (Gmail support)
- **Python:** 3.11.9

---

## 🔧 Local Development

### Prerequisites
- Python 3.11+
- pip

### Setup
```bash
# Navigate to backend folder
cd backend

# Create virtual environment (optional)
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Copy environment file
copy .env.example .env

# Edit .env with your credentials

# Run server
uvicorn app.main:app --reload
```

### Access
- **API:** http://localhost:8000
- **Docs:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## 🌐 Deployment (Render)

### Method 1: Web Interface

1. **Go to:** https://dashboard.render.com/select-repo?type=web

2. **Select Repository:** `DYNAMIC-PERSONAL-PERTFOLIO`

3. **Configure:**
   - **Name:** `portfolio-backend`
   - **Root Directory:** `backend` ⭐ (IMPORTANT!)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Plan:** Free

4. **Environment Variables:**
   ```env
   PYTHON_VERSION=3.11.9
   DATABASE_URL=(from PostgreSQL service)
   ADMIN_USERNAME=admin
   ADMIN_PASSWORD=your-secure-password
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=your-email@gmail.com
   SMTP_PASSWORD=your-gmail-app-password
   CORS_ORIGINS=["https://your-frontend.vercel.app"]
   DATA_DIR=/data
   ```

5. **Create PostgreSQL Database:**
   - Go to: https://dashboard.render.com/new/database
   - Name: `portfolio-db`
   - Plan: Free
   - Copy **Internal Database URL**
   - Add as `DATABASE_URL` in web service

6. **Add Persistent Disk:**
   - Service Settings → Disks → Add Disk
   - Name: `portfolio-uploads`
   - Mount Path: `/data`
   - Size: 1 GB

7. **Deploy!**

### Method 2: Blueprint (Automated)

The `render.yaml` file in root automates everything!

1. Go to: https://dashboard.render.com/blueprints
2. New Blueprint Instance
3. Select `DYNAMIC-PERSONAL-PERTFOLIO` repo
4. Apply

---

## 📝 Environment Variables

### Required

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection | `postgres://user:pass@host/db` |
| `ADMIN_USERNAME` | Admin login username | `admin` |
| `ADMIN_PASSWORD` | Admin login password | `SecurePass123!` |
| `SMTP_USER` | Gmail address | `your-email@gmail.com` |
| `SMTP_PASSWORD` | Gmail app password | `abcd efgh ijkl mnop` |

### Optional

| Variable | Description | Default |
|----------|-------------|---------|
| `CORS_ORIGINS` | Allowed frontend URLs | `["*"]` |
| `DATA_DIR` | Upload storage path | `./uploads` |
| `SMTP_HOST` | SMTP server | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP port | `587` |

---

## 🗄️ Database

### Auto-Detection
The app automatically detects which database to use:

- **No `DATABASE_URL`** → Uses SQLite (`portfolio.db`)
- **`DATABASE_URL` set** → Uses PostgreSQL

### Tables (14 total)
- `admin` - Admin authentication
- `contact_messages` - Contact form submissions
- `skill_categories` - Skill categories
- `skills` - Skills with levels
- `projects` - Project portfolio
- `resume` - Resume files
- `resume_media` - Resume images/videos
- `code_card` - Code display content
- `certifications` - Certificates
- `hero_video` - Hero section media
- `documents` - Private documents
- `gallery_images` - Public gallery
- `about_cards` - About section
- `contact_links` - Contact information

### Seeding
Default data is automatically seeded on first run:
- 1 admin user
- 3 skill categories
- 10 sample skills
- 5 about cards
- 6 contact links
- 5 sample projects

---

## 📊 API Documentation

After deployment, visit:
- **Swagger UI:** `https://your-backend.onrender.com/docs`
- **ReDoc:** `https://your-backend.onrender.com/redoc`

Interactive documentation with:
- All endpoints
- Request/response schemas
- Try it out feature
- Authentication support

---

## 🔐 Security

- ✅ bcrypt password hashing
- ✅ CORS protection
- ✅ Environment-based secrets
- ✅ SQL injection protection (parameterized queries)
- ✅ HTTPS only (Render automatic)

---

## 📦 Dependencies

See `requirements.txt` for complete list.

Key dependencies:
- `fastapi==0.115.5` - Web framework
- `asyncpg==0.30.0` - PostgreSQL driver
- `sqlalchemy==2.0.36` - ORM
- `aiosqlite==0.20.0` - SQLite driver (local)
- `passlib[bcrypt]==1.7.4` - Password hashing
- `uvicorn==0.32.1` - ASGI server

---

## 🧪 Testing

```bash
# Health check
curl https://your-backend.onrender.com/health

# Get skills
curl https://your-backend.onrender.com/api/skills/

# API docs
open https://your-backend.onrender.com/docs
```

---

## 🐛 Troubleshooting

### Server won't start
- Check Render logs for errors
- Verify all environment variables are set
- Ensure `DATABASE_URL` is correct

### Database connection error
- Use **Internal Database URL** (not External)
- Check database service is running
- Verify PostgreSQL is created in same region

### CORS errors
- Check `CORS_ORIGINS` includes frontend URL
- Format: `["https://your-frontend.vercel.app"]`
- No trailing slashes

---

## 📚 Project Structure

```
backend/
├── app/
│   ├── api/v1/
│   │   ├── endpoints/        # 13 API route files
│   │   └── router.py         # Router aggregator
│   ├── core/
│   │   └── security.py       # Auth & hashing
│   ├── db/
│   │   └── database.py       # Database layer
│   ├── repositories/         # Data access layer
│   ├── schemas/
│   │   └── models.py         # Pydantic models
│   ├── services/
│   │   └── email_service.py  # Email service
│   ├── config.py             # App configuration
│   └── main.py               # FastAPI app
├── uploads/                  # File storage
├── requirements.txt          # Python deps
├── render.yaml              # Deployment config
├── Dockerfile               # Container config
├── .env.example             # Env template
└── README.md                # This file
```

---

## 🔗 Related

- **Frontend:** `/portfolio-frontend`
- **Main README:** `/README.md`
- **Deployment Guide:** `/QUICK_DEPLOY.md`

---

## 📞 Support

Issues? Check:
- Render logs: https://dashboard.render.com
- API docs: `https://your-backend.onrender.com/docs`
- Full deployment guide: `/DEPLOYMENT_READY.md`

---

**Backend API ready for deployment!** 🚀
