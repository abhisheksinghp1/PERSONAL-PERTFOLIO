# 📋 Deployment Checklist

Use this as your step-by-step guide. Check off each item as you complete it!

---

## Pre-Deployment (5 minutes)

- [ ] Review `QUICK_DEPLOY.md` to understand the process
- [ ] Create GitHub account (if you don't have one)
- [ ] Have Gmail credentials ready for SMTP
- [ ] Choose a strong admin password

---

## Step 1: GitHub (5 minutes)

- [ ] Open terminal in Portfolio folder
- [ ] Run: `git init`
- [ ] Run: `git add .`
- [ ] Run: `git commit -m "Portfolio ready for deployment"`
- [ ] Run: `git branch -M main`
- [ ] Go to github.com → "New Repository"
- [ ] Repository name: `portfolio`
- [ ] Visibility: Public
- [ ] Click "Create repository"
- [ ] Copy the remote URL
- [ ] Run: `git remote add origin YOUR_URL`
- [ ] Run: `git push -u origin main`
- [ ] Verify files are on GitHub

✅ **GitHub complete!** Your code is now version controlled.

---

## Step 2: Render Backend (10 minutes)

### 2.1 Create Account
- [ ] Go to https://render.com
- [ ] Click "Get Started"
- [ ] Sign up with GitHub
- [ ] Authorize Render to access your repositories

### 2.2 Deploy from Blueprint
- [ ] Click "New +" button
- [ ] Select "Blueprint"
- [ ] Choose your `portfolio` repository
- [ ] Blueprint name: `portfolio-app`
- [ ] Click "Apply"
- [ ] Wait for services to create (~2 min)
- [ ] Verify 3 resources created:
  - [ ] PostgreSQL database
  - [ ] Web service
  - [ ] Persistent disk (1GB)

### 2.3 Configure Environment
- [ ] Go to web service dashboard
- [ ] Click "Environment" in left sidebar
- [ ] Find these variables (should be auto-set):
  - [ ] `DATABASE_URL` → ✅ (auto from render.yaml)
  - [ ] `DATA_DIR` → Should be `/data`
  - [ ] `PYTHON_VERSION` → Should be `3.11.9`
  - [ ] `CORS_ORIGINS` → Should be `["http://localhost:5173","http://localhost:3000"]`

### 2.4 Add Secret Variables
Click "Add Environment Variable" for each:

**Admin Credentials:**
- [ ] Key: `ADMIN_USERNAME`
- [ ] Value: `admin` (or your choice)
- [ ] Click "Add"

- [ ] Key: `ADMIN_PASSWORD`
- [ ] Value: Your secure password
- [ ] Click "Add"

**SMTP Settings:**
- [ ] Go to https://myaccount.google.com/apppasswords
- [ ] Generate app password for Mail
- [ ] Copy the 16-character password

- [ ] Key: `SMTP_USER`
- [ ] Value: your-email@gmail.com
- [ ] Click "Add"

- [ ] Key: `SMTP_PASSWORD`
- [ ] Value: Your 16-char app password
- [ ] Click "Add"

- [ ] Key: `SMTP_HOST`
- [ ] Value: `smtp.gmail.com`
- [ ] Click "Add"

- [ ] Key: `SMTP_PORT`
- [ ] Value: `587`
- [ ] Click "Add"

### 2.5 Deploy
- [ ] Click "Save Changes" (if needed)
- [ ] Wait for deployment (~5-10 min)
- [ ] Status should show "Live" (green)
- [ ] Copy your backend URL (looks like: `https://portfolio-backend-xxxx.onrender.com`)

### 2.6 Test Backend
- [ ] Open backend URL in browser
- [ ] Should see: `{"status":"ok","message":"Portfolio API v2 running",...}`
- [ ] Visit: `YOUR_BACKEND_URL/health`
- [ ] Should see: `{"status":"healthy","version":"2.0.0"}`
- [ ] Visit: `YOUR_BACKEND_URL/docs`
- [ ] Should see Swagger UI with all endpoints

✅ **Backend deployed!** Your API is live.

---

## Step 3: Vercel Frontend (5 minutes)

### 3.1 Create Account
- [ ] Go to https://vercel.com
- [ ] Click "Sign Up"
- [ ] Sign up with GitHub
- [ ] Authorize Vercel

### 3.2 Import Project
- [ ] Click "Add New..." → "Project"
- [ ] Find and select your `portfolio` repository
- [ ] Click "Import"

### 3.3 Configure Build
**Framework Preset:**
- [ ] Should auto-detect: "Vite"

**Root Directory:**
- [ ] Click "Edit"
- [ ] Enter: `portfolio-frontend`
- [ ] Click "Continue"

**Build Settings:**
- [ ] Build Command: `npm run build` (auto-detected)
- [ ] Output Directory: `dist` (auto-detected)
- [ ] Install Command: `npm install` (auto-detected)

### 3.4 Add Environment Variable
- [ ] Click "Environment Variables"
- [ ] Key: `VITE_API_URL`
- [ ] Value: Your backend URL (from Step 2.5)
  - Example: `https://portfolio-backend-xxxx.onrender.com`
- [ ] Click "Add"

### 3.5 Deploy
- [ ] Click "Deploy"
- [ ] Wait 2-3 minutes
- [ ] Status should show "Ready"
- [ ] Copy your frontend URL (looks like: `https://portfolio-xxxx.vercel.app`)
- [ ] Click "Visit" to open your site

✅ **Frontend deployed!** Your site is live.

---

## Step 4: Connect Frontend & Backend (2 minutes)

### 4.1 Update CORS in Backend
- [ ] Go back to Render dashboard
- [ ] Open your web service
- [ ] Click "Environment"
- [ ] Find `CORS_ORIGINS`
- [ ] Click "Edit"
- [ ] Change to: `["https://your-actual-vercel-url.vercel.app"]`
  - Use your real Vercel URL from Step 3.5
- [ ] Click "Save Changes"
- [ ] Wait for auto-redeploy (~2 min)

✅ **Connection complete!** Frontend can now talk to backend.

---

## Step 5: Final Testing (5 minutes)

### 5.1 Test Backend Directly
- [ ] Visit: `YOUR_BACKEND_URL/health`
- [ ] Status: healthy ✅
- [ ] Visit: `YOUR_BACKEND_URL/docs`
- [ ] Try "GET /api/skills/" → Execute
- [ ] Should return default skills ✅

### 5.2 Test Frontend
- [ ] Visit your Vercel URL
- [ ] Page loads correctly ✅
- [ ] Skills section shows skills ✅
- [ ] Projects section shows projects ✅
- [ ] Contact form displays ✅
- [ ] About section shows cards ✅

### 5.3 Test API Connection
- [ ] Open browser DevTools (F12)
- [ ] Go to Network tab
- [ ] Refresh the page
- [ ] Check for API calls to your backend URL
- [ ] All should be 200 OK ✅
- [ ] No CORS errors ✅

### 5.4 Test Admin Login
- [ ] Visit: `YOUR_VERCEL_URL/admin` (or wherever your admin panel is)
- [ ] Enter your ADMIN_USERNAME and ADMIN_PASSWORD
- [ ] Should log in successfully ✅

### 5.5 Test Contact Form
- [ ] Fill out contact form
- [ ] Submit
- [ ] Check your email (SMTP_USER)
- [ ] Should receive the message ✅

✅ **All tests passed!** Everything works.

---

## Step 6: Optional Enhancements (10 minutes)

### 6.1 Keep Backend Awake (Recommended)
- [ ] Go to https://uptimerobot.com
- [ ] Sign up (free)
- [ ] Add New Monitor
- [ ] Monitor Type: HTTP(s)
- [ ] Friendly Name: Portfolio Backend
- [ ] URL: `YOUR_BACKEND_URL/health`
- [ ] Monitoring Interval: 5 minutes
- [ ] Click "Create Monitor"

✅ **Backend stays awake!** No more cold starts.

### 6.2 Custom Domain (Optional)
**For Vercel (Frontend):**
- [ ] Buy domain on Namecheap (~$10/year)
- [ ] Go to Vercel → Project Settings → Domains
- [ ] Click "Add"
- [ ] Enter your domain
- [ ] Follow DNS setup instructions
- [ ] Wait for DNS propagation (~1-24 hours)
- [ ] Visit your custom domain
- [ ] Automatic HTTPS! ✅

**For Render (Backend):**
- [ ] Go to Render → Web Service → Settings
- [ ] Click "Custom Domain"
- [ ] Add subdomain: `api.yourdomain.com`
- [ ] Update DNS (CNAME record)
- [ ] Update frontend `VITE_API_URL` to new domain

### 6.3 Enable Analytics (Optional)
**Vercel Analytics:**
- [ ] Go to Vercel → Project → Analytics tab
- [ ] Click "Enable"
- [ ] View visitor stats, page views, etc.

---

## Post-Deployment

### Share Your Portfolio! 🎉
- [ ] Copy your Vercel URL
- [ ] Add to resume
- [ ] Add to LinkedIn
- [ ] Add to GitHub profile
- [ ] Share with recruiters
- [ ] Tweet about it!

### Monitor Your App
**Render Dashboard:**
- [ ] Check logs for errors
- [ ] Monitor CPU/memory usage
- [ ] View deployment history

**Vercel Dashboard:**
- [ ] Check analytics
- [ ] View bandwidth usage
- [ ] Monitor build times

### Keep It Updated
```bash
# Make changes locally
git add .
git commit -m "Update portfolio"
git push origin main

# Both Render and Vercel auto-deploy! ✅
```

---

## 🎯 Summary

When everything is checked:

✅ **Backend**: Live on Render with PostgreSQL  
✅ **Frontend**: Live on Vercel with Vite  
✅ **Database**: PostgreSQL (1GB free)  
✅ **Storage**: Persistent disk (1GB free)  
✅ **Cost**: $0/month  
✅ **Auto-deploy**: On git push  
✅ **HTTPS**: Automatic  
✅ **Monitoring**: Optional UptimeRobot  

---

## 📊 Your URLs

Fill these in as you deploy:

**GitHub Repo**: `https://github.com/YOUR_USERNAME/portfolio`

**Backend (Render)**: `https://portfolio-backend-xxxx.onrender.com`

**Frontend (Vercel)**: `https://portfolio-xxxx.vercel.app`

**API Docs**: `https://portfolio-backend-xxxx.onrender.com/docs`

**Custom Domain** (optional): `https://yourdomain.com`

---

## 🆘 Need Help?

### Stuck on a step?
1. Check `DEPLOYMENT_READY.md` for detailed explanations
2. Check `QUICK_DEPLOY.md` for quick reference
3. Check `POSTGRESQL_MIGRATION_COMPLETE.md` for technical details

### Common issues?
See "Troubleshooting" section in `DEPLOYMENT_READY.md`

### Still stuck?
- Render docs: https://render.com/docs
- Vercel docs: https://vercel.com/docs
- FastAPI docs: https://fastapi.tiangolo.com

---

## 🎉 Congratulations!

Once all boxes are checked, you have:
- ✅ A live, professional portfolio
- ✅ Production-grade backend
- ✅ Modern frontend
- ✅ Free hosting
- ✅ Auto-deployment
- ✅ Your own API!

**Time to land that job!** 🚀

---

**Total Time**: ~30 minutes  
**Total Cost**: $0/month  
**Total Awesomeness**: 100% 😎
