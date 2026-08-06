# 🚀 Dynamic Personal Portfolio

Full-stack portfolio application with FastAPI backend and React frontend.

## 📁 Project Structure

```
DYNAMIC-PERSONAL-PERTFOLIO/
│
├── backend/                    # 🐍 FastAPI Backend
│   ├── app/                   # Application code
│   │   ├── api/              # API endpoints
│   │   ├── core/             # Security & config
│   │   ├── db/               # Database layer
│   │   ├── repositories/     # Data access
│   │   ├── schemas/          # Pydantic models
│   │   └── services/         # Business logic
│   ├── requirements.txt       # Python dependencies
│   ├── render.yaml           # Render deployment config
│   ├── Dockerfile            # Container config
│   └── .env.example          # Environment template
│
├── portfolio-frontend/         # ⚛️ React Frontend
│   ├── src/                  # Source code
│   │   ├── components/       # React components
│   │   ├── services/         # API integration
│   │   ├── hooks/            # Custom hooks
│   │   └── utils/            # Utilities
│   ├── package.json          # Node dependencies
│   ├── vite.config.js        # Vite configuration
│   └── .env.example          # Environment template
│
├── render.yaml                # Backend deployment (Render)
├── vercel.json                # Frontend deployment (Vercel)
└── README.md                  # This file
```

---

## 🎯 Separate Deployments

### Backend (Render)
- **Path:** `/backend`
- **Deploy:** [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://dashboard.render.com/select-repo?type=web)

### Frontend (Vercel)
- **Path:** `/portfolio-frontend`
- **Deploy:** [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

---

## 🛠️ Backend Setup

### Tech Stack
- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- asyncpg

### Local Development
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: http://localhost:8000/docs

### Deployment
1. Go to: https://dashboard.render.com/select-repo?type=web
2. Select this repo: `DYNAMIC-PERSONAL-PERTFOLIO`
3. **Root Directory:** `backend`
4. See `backend/README.md` for detailed instructions

---

## 🎨 Frontend Setup

### Tech Stack
- React 18
- Vite
- JavaScript/JSX

### Local Development
```bash
cd portfolio-frontend
npm install
npm run dev
```

Visit: http://localhost:5173

### Deployment
1. Go to: https://vercel.com/new
2. Select this repo: `DYNAMIC-PERSONAL-PERTFOLIO`
3. **Root Directory:** `portfolio-frontend`
4. See `portfolio-frontend/README.md` for detailed instructions

---

## 🔗 Environment Variables

### Backend (.env)
```env
DATABASE_URL=postgres://...
ADMIN_USERNAME=admin
ADMIN_PASSWORD=secure-password
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
CORS_ORIGINS=["https://your-frontend.vercel.app"]
DATA_DIR=/data
```

### Frontend (.env)
```env
VITE_API_URL=https://your-backend.onrender.com
```

---

## 📚 Documentation

- **Backend Details:** See `/backend/README.md`
- **Frontend Details:** See `/portfolio-frontend/README.md`
- **Deployment Guide:** See `/QUICK_DEPLOY.md`
- **Full Guide:** See `/DEPLOYMENT_READY.md`

---

## 🚀 Quick Deploy

### 1. Backend (Render)
```bash
# Deploys from /backend folder
Root Directory: backend
Build: pip install -r requirements.txt
Start: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### 2. Frontend (Vercel)
```bash
# Deploys from /portfolio-frontend folder
Root Directory: portfolio-frontend
Framework: Vite
Build: npm run build
Output: dist
```

---

## 🎯 Live URLs

After deployment:

- **Backend API:** `https://portfolio-backend-xxxx.onrender.com`
- **API Docs:** `https://portfolio-backend-xxxx.onrender.com/docs`
- **Frontend:** `https://portfolio-xxxx.vercel.app`

---

## 💰 Cost

**Everything is FREE!**
- Render Backend: Free tier
- PostgreSQL: Free tier (1GB)
- Vercel Frontend: Free tier

---

## 📝 License

MIT License

---

## 👤 Author

**Abhishek Pratap Singh**
- GitHub: [@abhisheksinghp1](https://github.com/abhisheksinghp1)
- Email: aps11102003@gmail.com

---

## 🎉 Features

### Backend
- ✅ 13 RESTful API endpoints
- ✅ PostgreSQL database
- ✅ JWT authentication
- ✅ File upload support
- ✅ Email notifications
- ✅ Auto-generated API docs

### Frontend
- ✅ Modern React UI
- ✅ Responsive design
- ✅ Dynamic content
- ✅ Admin panel
- ✅ Contact form
- ✅ Project showcase

---

**Made with ❤️ by Abhishek Pratap Singh**
