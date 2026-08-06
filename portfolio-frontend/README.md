# ⚛️ Portfolio Frontend

Modern React + Vite frontend for personal portfolio application.

## 📁 This is the Frontend Folder

**Deploy this folder separately on Vercel!**

---

## 🚀 Features

- ✅ Modern React 18
- ✅ Vite for fast development
- ✅ Responsive design
- ✅ Dynamic content from API
- ✅ Admin panel
- ✅ Contact form
- ✅ Project showcase
- ✅ Skills display
- ✅ About section
- ✅ Gallery
- ✅ Resume upload/download

---

## 🛠️ Tech Stack

- **Framework:** React 18
- **Build Tool:** Vite
- **Language:** JavaScript/JSX
- **Styling:** CSS3
- **HTTP Client:** Fetch API
- **Routing:** React Router (if used)

---

## 🎨 Pages/Sections

### Public Pages
- **Home** - Hero section with intro
- **About** - About cards
- **Skills** - Skills by category
- **Projects** - Project portfolio
- **Contact** - Contact form + links
- **Gallery** - Image gallery
- **Resume** - Downloadable resume

### Admin Panel
- **Login** - Admin authentication
- **Dashboard** - Content management
- **Skills Manager** - Add/edit/delete skills
- **Projects Manager** - Manage projects
- **Upload Manager** - File management

---

## 🔧 Local Development

### Prerequisites
- Node.js 16+ and npm

### Setup
```bash
# Navigate to frontend folder
cd portfolio-frontend

# Install dependencies
npm install

# Copy environment file
copy .env.example .env.local

# Edit .env.local with your backend URL
# VITE_API_URL=http://localhost:8000

# Run development server
npm run dev
```

### Access
- **Frontend:** http://localhost:5173
- **Fast HMR** - Changes reflect instantly

---

## 🌐 Deployment (Vercel)

### Method 1: Web Interface

1. **Go to:** https://vercel.com/new

2. **Import Repository:** `DYNAMIC-PERSONAL-PERTFOLIO`

3. **Configure Project:**
   - **Framework Preset:** Vite (auto-detected)
   - **Root Directory:** `portfolio-frontend` ⭐ (IMPORTANT!)
   - **Build Command:** `npm run build` (auto)
   - **Output Directory:** `dist` (auto)
   - **Install Command:** `npm install` (auto)

4. **Environment Variables:**
   ```env
   VITE_API_URL=https://your-backend.onrender.com
   ```
   
   Get your backend URL from Render after deploying backend.

5. **Deploy!**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your site is live! 🎉

### Method 2: Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Navigate to frontend folder
cd portfolio-frontend

# Deploy
vercel --prod
```

### Method 3: One-Click Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/abhisheksinghp1/DYNAMIC-PERSONAL-PERTFOLIO&root-directory=portfolio-frontend)

---

## 📝 Environment Variables

### Required

| Variable | Description | Example |
|----------|-------------|---------|
| `VITE_API_URL` | Backend API URL | `https://portfolio-backend-xxxx.onrender.com` |

### Development
```env
# .env.development
VITE_API_URL=http://localhost:8000
```

### Production
```env
# Set in Vercel dashboard
VITE_API_URL=https://your-backend.onrender.com
```

**Important:** 
- Vite env vars must start with `VITE_`
- Restart dev server after changing env vars
- Update backend CORS to allow frontend URL

---

## 📦 Scripts

```bash
# Development
npm run dev          # Start dev server (port 5173)

# Build
npm run build        # Build for production

# Preview
npm run preview      # Preview production build locally

# Lint
npm run lint         # Run ESLint (if configured)
```

---

## 📁 Project Structure

```
portfolio-frontend/
├── public/               # Static assets
│   ├── images/
│   └── favicon.ico
├── src/
│   ├── components/       # React components
│   │   ├── About.jsx
│   │   ├── Contact.jsx
│   │   ├── Gallery.jsx
│   │   ├── Hero.jsx
│   │   ├── Projects.jsx
│   │   ├── Skills.jsx
│   │   └── ...
│   ├── services/         # API integration
│   │   ├── api.js        # HTTP client
│   │   ├── authService.js
│   │   ├── projectsService.js
│   │   └── skillsService.js
│   ├── hooks/            # Custom React hooks
│   │   ├── useAuth.js
│   │   ├── useApi.js
│   │   └── useLocalStorage.js
│   ├── utils/            # Utilities
│   │   ├── validators.js
│   │   ├── formatters.js
│   │   └── constants.js
│   ├── App.jsx           # Main app component
│   ├── main.jsx          # Entry point
│   └── index.css         # Global styles
├── .env.example          # Env template
├── .env.development      # Development env
├── .env.production       # Production env
├── index.html            # HTML template
├── package.json          # Dependencies
├── vite.config.js        # Vite config
└── README.md             # This file
```

---

## 🎨 Components

### Layout Components
- `Header` - Navigation bar
- `Footer` - Footer section
- `Layout` - Page layout wrapper

### Content Components
- `Hero` - Landing section
- `About` - About cards grid
- `Skills` - Skills by category
- `Projects` - Project cards
- `Contact` - Contact form + links
- `Gallery` - Image gallery
- `Resume` - Resume section

### Admin Components
- `AdminLogin` - Login form
- `AdminDashboard` - Admin panel
- `SkillsManager` - CRUD skills
- `ProjectsManager` - CRUD projects

---

## 🔌 API Integration

All API calls go through service layers:

```javascript
// services/api.js
const API_URL = import.meta.env.VITE_API_URL;

// Example API call
async function getSkills() {
  const response = await fetch(`${API_URL}/api/skills/`);
  return response.json();
}
```

### Services
- `authService.js` - Authentication
- `skillsService.js` - Skills CRUD
- `projectsService.js` - Projects CRUD
- `contactService.js` - Contact form

---

## 🧪 Testing

```bash
# Test API connection
# Open browser console and check:
console.log(import.meta.env.VITE_API_URL);

# Should show your backend URL
# Check Network tab for API calls
```

---

## 🐛 Troubleshooting

### API calls failing
- Check `VITE_API_URL` is set correctly
- Check backend CORS allows your frontend URL
- Open Network tab in DevTools
- Check backend is running

### Environment variables not loading
- Restart dev server after changing .env
- Ensure variable starts with `VITE_`
- Check file is named correctly (`.env.local` for local)

### Build errors
- Clear node_modules: `rm -rf node_modules && npm install`
- Clear cache: `npm run build -- --force`
- Check for syntax errors

### CORS errors
- Update backend `CORS_ORIGINS` to include your Vercel URL
- Format: `["https://your-app.vercel.app"]`
- Redeploy backend after updating

---

## 🚀 Performance

Vite provides:
- ⚡ Lightning fast HMR
- 📦 Optimized production builds
- 🔄 Code splitting
- 🗜️ Minification
- 🌳 Tree shaking

Production build is optimized and ready for deployment!

---

## 🎯 Post-Deployment

After deploying on Vercel:

1. **Copy your Vercel URL**
   Example: `https://portfolio-xxxx.vercel.app`

2. **Update Backend CORS**
   Go to Render → Backend Service → Environment
   ```env
   CORS_ORIGINS=["https://portfolio-xxxx.vercel.app"]
   ```

3. **Test Everything**
   - Page loads ✅
   - Skills display ✅
   - Projects display ✅
   - Contact form works ✅
   - No CORS errors ✅

---

## 📊 Vercel Features

Free tier includes:
- ✅ Unlimited deployments
- ✅ Automatic HTTPS
- ✅ Global CDN
- ✅ 100GB bandwidth/month
- ✅ Preview deployments
- ✅ Auto-deploy on git push
- ✅ Analytics (optional)

---

## 🔗 Related

- **Backend:** `/backend`
- **Main README:** `/README.md`
- **Deployment Guide:** `/QUICK_DEPLOY.md`

---

## 📞 Support

Issues? Check:
- Browser console for errors
- Network tab for API calls
- Vercel deployment logs
- Backend API docs: `https://backend.onrender.com/docs`

---

## 🎨 Customization

### Update Colors
Edit `src/index.css` or component styles

### Add Pages
1. Create component in `src/components/`
2. Add route (if using router)
3. Update navigation

### Modify Layout
Edit `src/App.jsx` and layout components

---

**Frontend ready for deployment!** 🚀

Deploy now: [Click to Deploy](https://vercel.com/new)
