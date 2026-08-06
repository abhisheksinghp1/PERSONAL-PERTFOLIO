# 🚀 Complete FREE Deployment Guide

## Everything FREE: Backend + PostgreSQL + Frontend

---

## 📋 What You'll Deploy (ALL FREE)

1. ✅ **Backend (FastAPI)** → Render.com (Free tier)
2. ✅ **Database (PostgreSQL)** → Render.com (Free PostgreSQL)
3. ✅ **Frontend (React)** → Vercel (Free tier)
4. ✅ **File Storage** → Render Disk (Free persistent disk)

**Total Cost**: $0/month 💰

---

## Part 1: Convert SQLite → PostgreSQL

### Step 1: Update Dependencies

Already done! Just verify `requirements.txt` has:
```txt
asyncpg==0.30.0        # PostgreSQL async driver
sqlalchemy==2.0.36     # ORM (optional but recommended)
```

### Step 2: Database Configuration

The new `database.py` will auto-detect PostgreSQL from `DATABASE_URL` environment variable!

---

## Part 2: Deploy Backend to Render (FREE)

### Step 1: Create Render Account
1. Go to https://render.com/
2. Sign up with GitHub (FREE)
3. No credit card required! ✅

### Step 2: Create PostgreSQL Database (FREE)
1. Click "New +" → "PostgreSQL"
2. **Name**: `portfolio-db`
3. **Database**: `portfolio`
4. **User**: (auto-generated)
5. **Region**: Choose closest to you
6. **Plan**: Select **FREE** tier
7. Click "Create Database"

**Important**: Copy these values:
- ✅ **Internal Database URL** (starts with `postgres://`)
- ✅ **External Database URL** (for local testing)

### Step 3: Create Web Service (FREE)
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. **Configuration**:
   - **Name**: `portfolio-backend`
   - **Region**: Same as database
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Select **FREE** tier

### Step 4: Add Environment Variables

In Render dashboard → Environment:

```env
# Database (use Internal Database URL from Step 2)
DATABASE_URL=postgres://user:pass@host/portfolio

# Admin Credentials
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your-secure-password-here

# SMTP (Gmail - for contact form)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-gmail-app-password

# CORS (your frontend URL)
CORS_ORIGINS=["https://your-app.vercel.app"]

# Python Environment
PYTHON_VERSION=3.11.9
```

### Step 5: Add Persistent Disk (FREE - 1GB)

1. Go to your web service settings
2. Click "Disks" → "Add Disk"
3. **Name**: `portfolio-uploads`
4. **Mount Path**: `/data`
5. **Size**: 1GB (FREE)
6. Click "Add"

This stores uploaded files (images, PDFs, etc.)

### Step 6: Deploy!

1. Click "Manual Deploy" → "Deploy latest commit"
2. Wait 5-10 minutes for first build
3. Your backend will be at: `https://portfolio-backend.onrender.com`

---

## Part 3: Deploy Frontend to Vercel (FREE)

### Step 1: Create Vercel Account
1. Go to https://vercel.com/
2. Sign up with GitHub (FREE)
3. No credit card required! ✅

### Step 2: Import Project
1. Click "Add New..." → "Project"
2. Import your GitHub repository
3. **Framework Preset**: Vite
4. **Root Directory**: `portfolio-frontend`
5. **Build Command**: `npm run build`
6. **Output Directory**: `dist`

### Step 3: Add Environment Variables

```env
VITE_API_URL=https://portfolio-backend.onrender.com
```

### Step 4: Deploy!

1. Click "Deploy"
2. Wait 2-3 minutes
3. Your frontend will be at: `https://your-app.vercel.app`

### Step 5: Update Backend CORS

Go back to Render → Your backend → Environment:

Update `CORS_ORIGINS`:
```env
CORS_ORIGINS=["https://your-app.vercel.app"]
```

Redeploy backend.

---

## Part 4: Verify Everything Works

### Backend Health Check
```bash
curl https://portfolio-backend.onrender.com/
# Should return: {"message": "Portfolio API"}
```

### API Documentation
Visit: `https://portfolio-backend.onrender.com/docs`

### Test Endpoints
```bash
# Get skills
curl https://portfolio-backend.onrender.com/api/skills/

# Get projects  
curl https://portfolio-backend.onrender.com/api/projects/
```

### Frontend
Visit: `https://your-app.vercel.app`

Test:
- ✅ Skills section loads
- ✅ Projects display
- ✅ Contact form works
- ✅ Admin login works

---

## 🎯 Free Tier Limits

### Render (Backend + Database)
- ✅ **Web Service**: 750 hours/month (enough for 24/7)
- ✅ **PostgreSQL**: Free forever (with limits)
  - 1GB storage
  - Shared CPU
  - 90 days of backups
- ✅ **Persistent Disk**: 1GB free
- ⚠️ **Sleeps after 15 min inactivity** (wakes in ~30 seconds)

### Vercel (Frontend)
- ✅ **Bandwidth**: 100GB/month
- ✅ **Builds**: Unlimited
- ✅ **Deployments**: Unlimited
- ✅ **Custom Domain**: FREE
- ✅ **SSL**: Automatic & FREE

### Total: $0/month 💰

---

## 🔧 Auto-Deploy Setup (FREE)

### Backend (Render)
Render auto-deploys on git push by default! ✅

### Frontend (Vercel)
Vercel auto-deploys on git push by default! ✅

**Workflow**:
```bash
git add .
git commit -m "update"
git push origin main
```
→ **Both backend & frontend auto-deploy!** 🚀

---

## 📊 Monitoring (FREE)

### Render Dashboard
- View logs in real-time
- Check build status
- Monitor CPU/memory usage

### Vercel Dashboard
- View deployment history
- Check build logs
- Monitor bandwidth usage

---

## 🐛 Troubleshooting

### Backend won't start
1. Check Render logs for errors
2. Verify `DATABASE_URL` is set
3. Verify start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Database connection error
1. Use **Internal Database URL** (not External)
2. Format: `postgres://user:pass@host/dbname`
3. Check database is created and running

### Frontend can't connect to backend
1. Check `VITE_API_URL` in Vercel environment
2. Check `CORS_ORIGINS` in Render environment
3. Verify backend is running

### Files not persisting
1. Check persistent disk is mounted at `/data`
2. Verify `DATA_DIR=/data` in environment
3. Check disk size (1GB limit)

---

## 🎉 Success Checklist

- [ ] Render account created (FREE)
- [ ] PostgreSQL database created (FREE)
- [ ] Backend deployed to Render (FREE)
- [ ] Persistent disk attached (FREE 1GB)
- [ ] Vercel account created (FREE)
- [ ] Frontend deployed to Vercel (FREE)
- [ ] Environment variables set
- [ ] CORS configured
- [ ] API docs accessible
- [ ] Frontend loads data
- [ ] Auto-deploy working

---

## 💡 Pro Tips

### 1. Keep Backend Awake
Free tier sleeps after 15 min. Use a service like:
- UptimeRobot (free) - ping every 5 minutes
- Cron-job.org (free) - scheduled pings

### 2. Custom Domain (FREE)
- Vercel: Add custom domain for FREE
- Render: Add custom domain for FREE
- Buy domain on Namecheap (~$10/year)

### 3. Database Backups
- Render: 90 days automatic backups (FREE)
- Export manually if needed

### 4. Logs
- Render: Real-time logs in dashboard
- Vercel: Build & function logs

---

## 📈 Upgrade Path (If Needed Later)

If you outgrow free tier:

**Render**:
- Starter: $7/month (no sleep, more resources)
- Database: $7/month (25GB, no sleep)

**Vercel**:
- Pro: $20/month (more bandwidth, team features)

But FREE tier is enough for most portfolios! ✅

---

## 🚀 Deploy Commands Summary

### Initial Setup
```bash
# 1. Push to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main

# 2. Create Render PostgreSQL (Web UI)
# 3. Create Render Web Service (Web UI)
# 4. Create Vercel Project (Web UI)
```

### Updates
```bash
# Make changes
git add .
git commit -m "Update features"
git push origin main

# Both auto-deploy! ✅
```

---

## 📝 Environment Variables Template

### Render (.env for backend)
```env
DATABASE_URL=postgres://user:pass@host/portfolio
ADMIN_USERNAME=admin
ADMIN_PASSWORD=secure-password
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=app-password
CORS_ORIGINS=["https://your-app.vercel.app"]
DATA_DIR=/data
PYTHON_VERSION=3.11.9
```

### Vercel (.env for frontend)
```env
VITE_API_URL=https://portfolio-backend.onrender.com
```

---

**Status**: Ready to deploy! 🚀  
**Cost**: $0/month 💰  
**Time to deploy**: ~30 minutes ⏱️  
**Difficulty**: Easy 🟢
