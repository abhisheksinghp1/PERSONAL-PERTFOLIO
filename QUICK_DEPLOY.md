# ⚡ Quick Deploy Guide - 20 Minutes to LIVE!

## Status: 🎉 READY TO DEPLOY!

Your backend now supports **automatic PostgreSQL detection**!
- ✅ Local dev: Uses SQLite (no setup needed)
- ✅ Production: Uses PostgreSQL (auto-detected from DATABASE_URL)

---

## 🚀 Deploy in 3 Steps (20 minutes total)

### 1️⃣ Push to GitHub (5 min)

```bash
# In Portfolio folder
git init
git add .
git commit -m "Portfolio ready for deployment"
git branch -M main

# Create repo on github.com → "New Repository" → "portfolio"
git remote add origin https://github.com/YOUR_USERNAME/portfolio.git
git push -u origin main
```

### 2️⃣ Deploy Backend - Render (10 min)

1. **Go to** https://render.com → Sign up with GitHub
2. **Click** "New +" → "Blueprint"
3. **Select** your `portfolio` repository
4. **Blueprint creates**:
   - PostgreSQL database (FREE)
   - Web service (FREE)
   - 1GB persistent disk (FREE)
5. **Set environment variables** in dashboard:
   ```
   ADMIN_USERNAME=admin
   ADMIN_PASSWORD=your-secure-password
   SMTP_USER=your-email@gmail.com
   SMTP_PASSWORD=your-gmail-app-password
   ```
6. **Click** "Apply" → Wait 5-10 min → DONE! ✅

Your backend: `https://portfolio-backend-XXXX.onrender.com`

### 3️⃣ Deploy Frontend - Vercel (5 min)

1. **Go to** https://vercel.com → Sign up with GitHub
2. **Click** "Add New..." → "Project"
3. **Select** your `portfolio` repository
4. **Configure**:
   - Root Directory: `portfolio-frontend`
   - Framework: Vite (auto-detected)
5. **Add environment variable**:
   ```
   VITE_API_URL=https://portfolio-backend-XXXX.onrender.com
   ```
6. **Click** "Deploy" → Wait 2-3 min → DONE! ✅

Your frontend: `https://your-app.vercel.app`

### 4️⃣ Update CORS (1 min)

Go back to Render → Your web service → Environment:
```
CORS_ORIGINS=["https://your-app.vercel.app"]
```
Save → Auto-redeploys → DONE! ✅

---

## ✅ Verify It Works

### Backend Health
```bash
curl https://portfolio-backend-XXXX.onrender.com/health
# Should return: {"status":"healthy","version":"2.0.0"}
```

### API Docs
Visit: `https://portfolio-backend-XXXX.onrender.com/docs`

### Frontend
Visit: `https://your-app.vercel.app`
- Skills load ✅
- Projects display ✅
- Contact form works ✅
- Admin login works ✅

---

## 🔑 How to Get Gmail App Password

1. Go to https://myaccount.google.com/apppasswords
2. Sign in
3. Select "Mail" → Generate
4. Copy 16-character password
5. Use as `SMTP_PASSWORD`

---

## 💰 Cost Breakdown

| Service | What | Cost |
|---------|------|------|
| Render Backend | FastAPI app | **$0** |
| Render PostgreSQL | Database | **$0** |
| Render Disk | 1GB storage | **$0** |
| Vercel Frontend | React app | **$0** |
| **TOTAL** | | **$0/month** |

---

## 🎯 Pro Tip: Keep Backend Awake

Free tier sleeps after 15 min. Use **UptimeRobot**:
1. Go to https://uptimerobot.com (free)
2. Add monitor: Your backend health URL
3. Interval: 5 minutes
4. Backend stays awake 24/7! ✨

---

## 📚 Full Documentation

For detailed guide, see: `DEPLOYMENT_READY.md`

---

## 🎉 You're Done!

Your portfolio is now:
- 🌐 Live on the internet
- 🔒 HTTPS secured
- 💾 PostgreSQL powered
- 🚀 Auto-deploying
- 💰 Completely FREE

**Time to deploy**: ~20 minutes  
**Monthly cost**: $0  

**Go deploy! 🚀**
