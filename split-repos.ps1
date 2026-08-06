# Split Portfolio into Two GitHub Repositories
# Run this script to automatically create separate backend and frontend repos

Write-Host "🔀 Splitting Portfolio into Backend + Frontend Repos..." -ForegroundColor Cyan
Write-Host ""

# Get GitHub username
$username = Read-Host "Enter your GitHub username (e.g., abhisheksinghp1)"

# Confirm
Write-Host ""
Write-Host "This will create:" -ForegroundColor Yellow
Write-Host "  Backend:  https://github.com/$username/portfolio-backend" -ForegroundColor Green
Write-Host "  Frontend: https://github.com/$username/portfolio-frontend" -ForegroundColor Green
Write-Host ""
$confirm = Read-Host "Continue? (y/n)"

if ($confirm -ne "y") {
    Write-Host "Cancelled." -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "📦 Step 1: Creating backend repository..." -ForegroundColor Cyan

# Create backend temp directory
$backendTemp = "C:\Users\HP\OneDrive\Desktop\portfolio-backend-temp"
if (Test-Path $backendTemp) {
    Remove-Item $backendTemp -Recurse -Force
}
New-Item -ItemType Directory -Path $backendTemp | Out-Null

# Copy backend files
Copy-Item -Path "C:\Users\HP\OneDrive\Desktop\Portfolio\backend\*" -Destination $backendTemp -Recurse -Force
Copy-Item -Path "C:\Users\HP\OneDrive\Desktop\Portfolio\render.yaml" -Destination $backendTemp -Force

# Create backend .gitignore
@"
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Environment
.env
.env.local

# Database
*.db
*.db-journal
portfolio.db

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Uploads (keep structure, ignore files)
uploads/*
!uploads/.gitkeep
"@ | Out-File -FilePath "$backendTemp\.gitignore" -Encoding utf8

# Create backend README
@"
# Portfolio Backend

FastAPI backend with PostgreSQL for personal portfolio.

## Features
- 🚀 FastAPI async framework
- 🗄️ PostgreSQL database
- 📝 13 API endpoints
- 🔐 bcrypt authentication
- 📧 SMTP email service
- 📚 Auto-generated API docs

## Tech Stack
- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- asyncpg

## Local Development

\`\`\`bash
# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
\`\`\`

Visit: http://localhost:8000/docs

## Deployment

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/$username/portfolio-backend)

See \`render.yaml\` for configuration.

## Environment Variables

See \`.env.example\` for required variables.
"@ | Out-File -FilePath "$backendTemp\README.md" -Encoding utf8

# Initialize backend git
Set-Location $backendTemp
git init
git add .
git commit -m "Initial commit - FastAPI backend with PostgreSQL"
git branch -M main
git remote add origin "https://github.com/$username/portfolio-backend.git"

Write-Host "✅ Backend repository prepared!" -ForegroundColor Green
Write-Host "   Location: $backendTemp" -ForegroundColor Gray
Write-Host ""

Write-Host "📦 Step 2: Creating frontend repository..." -ForegroundColor Cyan

# Create frontend temp directory
$frontendTemp = "C:\Users\HP\OneDrive\Desktop\portfolio-frontend-temp"
if (Test-Path $frontendTemp) {
    Remove-Item $frontendTemp -Recurse -Force
}
New-Item -ItemType Directory -Path $frontendTemp | Out-Null

# Copy frontend files
Copy-Item -Path "C:\Users\HP\OneDrive\Desktop\Portfolio\portfolio-frontend\*" -Destination $frontendTemp -Recurse -Force

# Create frontend README
@"
# Portfolio Frontend

Modern React + Vite frontend for personal portfolio.

## Features
- ⚡ Vite for fast development
- ⚛️ React 18
- 🎨 Modern UI/UX
- 📱 Fully responsive
- 🔌 API integration
- 🎯 Custom hooks

## Tech Stack
- React 18
- Vite
- JavaScript/JSX
- CSS3

## Local Development

\`\`\`bash
# Install dependencies
npm install

# Run dev server
npm run dev
\`\`\`

Visit: http://localhost:5173

## Deployment

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/$username/portfolio-frontend)

## Environment Variables

\`\`\`env
VITE_API_URL=your-backend-url
\`\`\`

See \`.env.example\` for details.
"@ | Out-File -FilePath "$frontendTemp\README.md" -Encoding utf8

# Initialize frontend git
Set-Location $frontendTemp
git init
git add .
git commit -m "Initial commit - React Vite frontend"
git branch -M main
git remote add origin "https://github.com/$username/portfolio-frontend.git"

Write-Host "✅ Frontend repository prepared!" -ForegroundColor Green
Write-Host "   Location: $frontendTemp" -ForegroundColor Gray
Write-Host ""

Write-Host "🎯 Next Steps:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Create GitHub repositories:" -ForegroundColor Yellow
Write-Host "   Backend:  https://github.com/new → Name: portfolio-backend" -ForegroundColor White
Write-Host "   Frontend: https://github.com/new → Name: portfolio-frontend" -ForegroundColor White
Write-Host ""
Write-Host "2. Push backend:" -ForegroundColor Yellow
Write-Host "   cd $backendTemp" -ForegroundColor White
Write-Host "   git push -u origin main" -ForegroundColor White
Write-Host ""
Write-Host "3. Push frontend:" -ForegroundColor Yellow
Write-Host "   cd $frontendTemp" -ForegroundColor White
Write-Host "   git push -u origin main" -ForegroundColor White
Write-Host ""
Write-Host "4. Deploy:" -ForegroundColor Yellow
Write-Host "   Backend:  https://render.com/deploy?repo=https://github.com/$username/portfolio-backend" -ForegroundColor Green
Write-Host "   Frontend: https://vercel.com/new/clone?repository-url=https://github.com/$username/portfolio-frontend" -ForegroundColor Green
Write-Host ""

Write-Host "✨ Done! Repositories are ready to push." -ForegroundColor Cyan
