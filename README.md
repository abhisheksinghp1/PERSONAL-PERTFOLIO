# 🚀 Abhishek Pratap Singh — Portfolio

[![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Frontend](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react)](https://react.dev/)
[![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)](https://www.sqlite.org/)
[![Deploy](https://img.shields.io/badge/Deploy-Render%20%2B%20Vercel-blueviolet)](https://render.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A modern, full-stack personal portfolio with an admin panel for dynamic content management. Built with FastAPI (Python) and React (Vite).

🔗 **Live Demo:** [your-portfolio.vercel.app](https://your-portfolio.vercel.app)  
📚 **API Docs:** [backend.onrender.com/docs](https://dynamic-personal-pertfolio.onrender.com/docs)

---

## ✨ Features

### Public Features
- 🎨 Animated hero section with typewriter effect
- 💼 Dynamic skills showcase with progress bars
- 🚀 Project portfolio with modal details
- 📜 Certifications with PDF/image downloads
- 📧 Contact form with email notifications
- 📄 Resume viewer and download
- 🌙 Dark/light theme toggle
- 🖱️ Custom animated cursor

### Admin Panel
- 🔐 Secure JWT authentication with OTP password recovery
- ✏️ Full CRUD for skills, projects, certifications
- 📤 File uploads (resume, gallery, certifications)
- 🗂️ Private document vault
- 🎨 Drag-to-reorder content
- 📊 Real-time content preview

---

## 🛠️ Tech Stack

### Backend
- **Framework:** FastAPI 0.115
- **Database:** SQLite (aiosqlite)
- **Auth:** Custom JWT (HS256)
- **Email:** SMTP (Gmail)
- **Validation:** Pydantic v2
- **Server:** Uvicorn (ASGI)

### Frontend
- **Framework:** React 18.3
- **Build Tool:** Vite 5.3
- **Routing:** React Router v6
- **Animations:** Framer Motion
- **Icons:** React Icons
- **Notifications:** React Hot Toast
- **Styling:** Custom CSS with CSS Variables

### DevOps
- **Hosting:** Render (backend) + Vercel (frontend)
- **CI/CD:** Auto-deploy on git push
- **Containerization:** Docker + docker-compose

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- npm or yarn

### 1. Clone the Repository
```bash
git clone https://github.com/abhisheksinghp1/DYNAMIC-PERSONAL-PERTFOLIO.git
cd DYNAMIC-PERSONAL-PERTFOLIO
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Copy .env.example and fill in your credentials
cp .env.example .env

# Run the server
uvicorn app.main:app --reload
```

Backend runs at: `http://localhost:8000`  
API Docs: `http://localhost:8000/docs`

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://localhost:3000`

### 4. Docker (Alternative)
```bash
# Run both backend and frontend
docker-compose up
```

---

## 📁 Project Structure

```
portfolio/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── core/           # Security, logging, config
│   │   ├── db/             # Database models
│   │   ├── schemas/        # Pydantic models
│   │   └── services/       # Business logic
│   └── tests/              # Pytest tests
│
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Route pages
│   │   ├── context/       # React context
│   │   └── services/      # API clients
│   └── tests/             # Vitest tests
│
└── docs/                  # Documentation
```

---

## 🔧 Configuration

### Backend Environment Variables
```env
# SMTP (Gmail App Password required)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_gmail_app_password

# Admin
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your_secure_password
OWNER_EMAIL=your_email@gmail.com

# Security
SECRET_KEY=your-long-random-secret-key
```

### Frontend Environment Variables
```env
# Development
VITE_API_URL=http://localhost:8000

# Production
VITE_API_URL=https://your-backend.onrender.com
```

---

## 📚 API Documentation

Full API documentation is auto-generated and available at `/docs` (Swagger UI) and `/redoc` (ReDoc).

### Key Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/auth/login` | Admin login |
| `GET` | `/api/skills/` | List all skills |
| `GET` | `/api/projects/` | List all projects |
| `POST` | `/api/contact/send` | Send contact message |
| `GET` | `/api/resume/download` | Download resume PDF |

---

## 🚢 Deployment

### Backend (Render)
1. Push code to GitHub
2. Create new Web Service on Render
3. Set Root Directory to `backend`
4. Set Build Command: `pip install -r requirements.txt`
5. Set Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Add environment variables

### Frontend (Vercel)
1. Import GitHub repo on Vercel
2. Set Root Directory to `frontend`
3. Set Build Command: `npm run build`
4. Set Output Directory: `dist`
5. Add `VITE_API_URL` environment variable

---

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
pytest --cov=app tests/  # With coverage
```

### Frontend Tests
```bash
cd frontend
npm test
npm run test:coverage
```

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Abhishek Pratap Singh**
- Email: aps11102003@gmail.com
- GitHub: [@abhisheksinghp1](https://github.com/abhisheksinghp1)
- LinkedIn: [abhisheksinghp1](https://www.linkedin.com/in/abhisheksinghp1/)

---

## 🙏 Acknowledgments

- FastAPI for the amazing web framework
- React and Vite for the frontend tooling
- Render and Vercel for free hosting
- All open-source contributors

---

**⭐ Star this repo if you find it helpful!**
