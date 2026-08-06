# 🚀 Two Separate GitHub Repos - Quick Setup

## ⚡ Option 1: Automated (Easiest - 5 minutes)

Run the PowerShell script:

```powershell
cd "C:\Users\HP\OneDrive\Desktop\Portfolio"
.\split-repos.ps1
```

Then follow the on-screen instructions!

---

## 🔧 Option 2: Manual (10 minutes)

### Step 1: Create Backend Repo on GitHub

1. Go to: https://github.com/new
2. **Name**: `portfolio-backend`
3. **Description**: `FastAPI backend with PostgreSQL`
4. **Public**
5. Click **Create repository**

### Step 2: Create Frontend Repo on GitHub

1. Go to: https://github.com/new
2. **Name**: `portfolio-frontend`
3. **Description**: `React Vite personal portfolio`
4. **Public**
5. Click **Create repository**

### Step 3: Push Backend

```powershell
# Navigate to backend
cd "C:\Users\HP\OneDrive\Desktop\Portfolio\backend"

# Initialize git
git init
git add .
git commit -m "Initial commit - FastAPI backend"

# Add remote (replace abhisheksinghp1 with your username)
git remote add origin https://github.com/abhisheksinghp1/portfolio-backend.git
git branch -M main
git push -u origin main
```

### Step 4: Push Frontend

```powershell
# Navigate to frontend
cd "C:\Users\HP\OneDrive\Desktop\Portfolio\portfolio-frontend"

# Initialize git
git init
git add .
git commit -m "Initial commit - React frontend"

# Add remote (replace abhisheksinghp1 with your username)
git remote add origin https://github.com/abhisheksinghp1/portfolio-frontend.git
git branch -M main
git push -u origin main
```

### Step 5: Move render.yaml to Backend

```powershell
# Copy render.yaml to backend folder
Copy-Item "C:\Users\HP\OneDrive\Desktop\Portfolio\render.yaml" "C:\Users\HP\OneDrive\Desktop\Portfolio\backend\render.yaml"

# Commit and push
cd "C:\Users\HP\OneDrive\Desktop\Portfolio\backend"
git add render.yaml
git commit -m "Add Render deployment config"
git push origin main
```

---

## 🔗 Direct Deployment Links

### Backend (Render)

**Quick Deploy Button:**
```
https://render.com/deploy?repo=https://github.com/abhisheksinghp1/portfolio-backend
```

Or manually:
1. https://dashboard.render.com/
2. New + → Blueprint
3. Select `portfolio-backend` repo

### Frontend (Vercel)

**Quick Deploy Button:**
```
https://vercel.com/new/clone?repository-url=https://github.com/abhisheksinghp1/portfolio-frontend
```

Or manually:
1. https://vercel.com/new
2. Import `portfolio-frontend` repo
3. Framework: Vite
4. Add env: `VITE_API_URL`

---

## 📝 Your Repository URLs

After creation, you'll have:

**Backend:**
```
https://github.com/abhisheksinghp1/portfolio-backend
```

**Frontend:**
```
https://github.com/abhisheksinghp1/portfolio-frontend
```

---

## ✅ Benefits of Two Repos

### 1. Cleaner Organization
- Backend code separate from frontend
- Each repo has its own README
- Independent version control

### 2. Easier Deployment
- Direct deployment links
- Render only sees backend files
- Vercel only sees frontend files

### 3. Professional
- Industry standard practice
- Better for team collaboration
- Looks better on GitHub profile

### 4. Independent Updates
- Update backend without touching frontend
- Update frontend without touching backend
- Different deployment frequencies

---

## 🎯 After Pushing

### 1. Add Deployment Badges to README

**Backend README.md:**
```markdown
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/abhisheksinghp1/portfolio-backend)
```

**Frontend README.md:**
```markdown
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/abhisheksinghp1/portfolio-frontend)
```

### 2. Update Links

In frontend `.env.production`:
```env
VITE_API_URL=https://your-backend.onrender.com
```

In backend environment variables (Render):
```env
CORS_ORIGINS=["https://your-frontend.vercel.app"]
```

---

## 🚀 Deployment Order

1. **Deploy Backend First** (Render)
   - Creates PostgreSQL database
   - Provides backend URL
   - Takes ~10 minutes

2. **Deploy Frontend Second** (Vercel)
   - Use backend URL as `VITE_API_URL`
   - Takes ~3 minutes

3. **Update Backend CORS**
   - Add frontend URL to `CORS_ORIGINS`
   - Redeploy backend

---

## 💡 Pro Tips

### Keep Both Repos Synced
When you make changes:

```bash
# Backend changes
cd backend
git add .
git commit -m "Update backend"
git push origin main
# Auto-deploys to Render ✅

# Frontend changes
cd portfolio-frontend
git add .
git commit -m "Update frontend"
git push origin main
# Auto-deploys to Vercel ✅
```

### Add Deploy Previews
- Vercel: Automatic preview for every push
- Render: Preview via pull requests

### Monitor Both
- Backend: Render dashboard
- Frontend: Vercel analytics

---

## 🆘 Troubleshooting

### "Repository already exists"
- Use different names: `portfolio-api` and `portfolio-web`

### "Authentication failed"
- Use GitHub Desktop to push
- Or create Personal Access Token

### "render.yaml not found"
- Make sure it's in backend root
- Not in backend/backend/

---

## ✨ Final Result

**Backend Repo:**
- `https://github.com/abhisheksinghp1/portfolio-backend`
- Deployed at: `https://portfolio-backend-xxx.onrender.com`

**Frontend Repo:**
- `https://github.com/abhisheksinghp1/portfolio-frontend`
- Deployed at: `https://portfolio-xxx.vercel.app`

**Both FREE, both auto-deploying!** 🎉

---

## 🎯 Choose Your Method

**Want it automatic?**
→ Run `.\split-repos.ps1`

**Want it manual?**
→ Follow Step 1-5 above

**Want to keep one repo?**
→ Use current `DYNAMIC-PERSONAL-PERTFOLIO` with monorepo structure

---

**Time**: 5-10 minutes  
**Difficulty**: Easy  
**Result**: Two professional repos ready to deploy! 🚀
