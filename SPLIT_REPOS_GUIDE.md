# 🔀 Split Into Two GitHub Repositories

## Why Separate Repos?

✅ **Better organization** - Backend and frontend independent  
✅ **Easier deployment** - Direct deployment links  
✅ **Professional** - Industry standard practice  
✅ **Independent versioning** - Update backend/frontend separately  

---

## 🎯 Quick Setup (10 minutes)

### Option 1: Create Two New Repos (Recommended)

#### Step 1: Create Backend Repo
1. Go to https://github.com/new
2. **Repository name**: `portfolio-backend`
3. **Description**: `FastAPI backend with PostgreSQL - Portfolio API`
4. **Visibility**: Public
5. Click **"Create repository"**

#### Step 2: Create Frontend Repo
1. Go to https://github.com/new
2. **Repository name**: `portfolio-frontend`
3. **Description**: `React + Vite frontend - Personal Portfolio`
4. **Visibility**: Public
5. Click **"Create repository"**

---

### Step 3: Push Backend to New Repo

```bash
# Navigate to backend folder
cd "c:\Users\HP\OneDrive\Desktop\Portfolio\backend"

# Initialize new git repo
git init
git add .
git commit -m "Initial commit - FastAPI backend with PostgreSQL"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/portfolio-backend.git
git branch -M main
git push -u origin main
```

**Your backend repo will be:**
`https://github.com/YOUR_USERNAME/portfolio-backend`

---

### Step 4: Push Frontend to New Repo

```bash
# Navigate to frontend folder
cd "c:\Users\HP\OneDrive\Desktop\Portfolio\portfolio-frontend"

# Initialize new git repo
git init
git add .
git commit -m "Initial commit - React Vite frontend"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/portfolio-frontend.git
git branch -M main
git push -u origin main
```

**Your frontend repo will be:**
`https://github.com/YOUR_USERNAME/portfolio-frontend`

---

## 🚀 Direct Deployment Links

### Backend Deployment (Render)
After pushing backend to GitHub:

**Direct Deploy Link:**
```
https://render.com/deploy?repo=https://github.com/YOUR_USERNAME/portfolio-backend
```

Or manually:
1. Go to https://dashboard.render.com/
2. Click "New +" → "Web Service"
3. Connect `portfolio-backend` repo
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Environment**: Add `DATABASE_URL` (from PostgreSQL service)

### Frontend Deployment (Vercel)
After pushing frontend to GitHub:

**Direct Deploy Link:**
```
https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/portfolio-frontend
```

Or manually:
1. Go to https://vercel.com/new
2. Import `portfolio-frontend` repo
3. Framework: Vite (auto-detected)
4. Root Directory: `.` (default)
5. Environment Variable: `VITE_API_URL` = Your Render backend URL

---

## 📁 File Structure Changes Needed

### Backend Repo Structure
```
portfolio-backend/
├── render.yaml          # Move from root
├── .env.example
├── requirements.txt
├── runtime.txt
├── Dockerfile
├── app/
│   ├── main.py
│   ├── config.py
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── repositories/
│   ├── schemas/
│   └── services/
├── uploads/
└── README.md
```

### Frontend Repo Structure
```
portfolio-frontend/
├── vercel.json         # Optional config
├── .env.example
├── package.json
├── vite.config.js
├── index.html
├── src/
│   ├── App.jsx
│   ├── main.jsx
│   ├── components/
│   ├── services/
│   ├── hooks/
│   └── utils/
├── public/
└── README.md
```

---

## 🔧 Automated Script

Run this to split automatically:
