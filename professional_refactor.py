#!/usr/bin/env python3
"""
Professional Portfolio Refactor Script
Automatically reorganizes the entire codebase into production-ready structure
"""

import shutil
import os
import re
from pathlib import Path

# Color codes for terminal output
class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Color.BOLD}{Color.HEADER}{'='*60}{Color.END}")
    print(f"{Color.BOLD}{Color.HEADER}{text:^60}{Color.END}")
    print(f"{Color.BOLD}{Color.HEADER}{'='*60}{Color.END}\n")

def print_success(text):
    print(f"{Color.GREEN}✓ {text}{Color.END}")

def print_info(text):
    print(f"{Color.CYAN}ℹ {text}{Color.END}")

def print_warning(text):
    print(f"{Color.YELLOW}⚠ {text}{Color.END}")

def print_error(text):
    print(f"{Color.RED}✗ {text}{Color.END}")

def backup_existing():
    """Backup existing Backend and portfolio-frontend folders"""
    print_header("STEP 1: Backup Existing Code")
    
    if Path("Backend").exists():
        if Path("Backend_backup").exists():
            shutil.rmtree("Backend_backup")
        shutil.copytree("Backend", "Backend_backup")
        print_success("Backed up Backend/ → Backend_backup/")
    
    if Path("portfolio-frontend").exists():
        if Path("portfolio-frontend_backup").exists():
            shutil.rmtree("portfolio-frontend_backup")
        shutil.copytree("portfolio-frontend", "portfolio-frontend_backup")
        print_success("Backed up portfolio-frontend/ → portfolio-frontend_backup/")

def create_backend_structure():
    """Create new backend folder structure"""
    print_header("STEP 2: Create Backend Structure")
    
    backend_dirs = [
        "backend/app",
        "backend/app/api/v1/endpoints",
        "backend/app/core",
        "backend/app/db",
        "backend/app/schemas",
        "backend/app/services",
        "backend/app/middleware",
        "backend/tests",
        "backend/scripts",
        "backend/uploads",
    ]
    
    for dir_path in backend_dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        # Create __init__.py files
        if "/app/" in dir_path or dir_path.endswith("/tests"):
            (Path(dir_path) / "__init__.py").touch()
    
    print_success(f"Created {len(backend_dirs)} directories")

def copy_backend_files():
    """Copy and reorganize backend files"""
    print_header("STEP 3: Copy Backend Files")
    
    # Root-level files
    root_files = [
        ("requirements.txt", "requirements.txt"),
        (".python-version", ".python-version"),
        (".env", ".env"),
    ]
    
    for src, dst in root_files:
        src_path = Path("Backend") / src
        dst_path = Path("backend") / dst
        if src_path.exists():
            shutil.copy2(src_path, dst_path)
            print_success(f"{src} → backend/{dst}")
    
    # Core application files
    app_files = [
        ("config.py", "app/config.py"),
        ("database.py", "app/db/database.py"),
        ("models.py", "app/schemas/models.py"),
        ("auth.py", "app/core/security.py"),
        ("email_service.py", "app/services/email_service.py"),
    ]
    
    for src, dst in app_files:
        src_path = Path("Backend") / src
        dst_path = Path("backend") / dst
        if src_path.exists():
            shutil.copy2(src_path, dst_path)
            print_success(f"{src} → backend/{dst}")
    
    # Copy all routers
    routers_dir = Path("Backend/routers")
    if routers_dir.exists():
        for router_file in routers_dir.glob("*.py"):
            if router_file.name != "__init__.py":
                dst = Path("backend/app/api/v1/endpoints") / router_file.name
                shutil.copy2(router_file, dst)
                print_success(f"routers/{router_file.name} → app/api/v1/endpoints/{router_file.name}")
    
    # Copy uploads if exists
    uploads_src = Path("Backend/uploads")
    uploads_dst = Path("backend/uploads")
    if uploads_src.exists():
        if uploads_dst.exists():
            shutil.rmtree(uploads_dst)
        shutil.copytree(uploads_src, uploads_dst)
        print_success("Copied uploads/ directory")

def update_backend_imports():
    """Update import statements in backend files"""
    print_header("STEP 4: Update Backend Imports")
    
    replacements = [
        (r'from database import', 'from app.db.database import'),
        (r'from config import', 'from app.config import'),
        (r'from models import', 'from app.schemas.models import'),
        (r'from email_service import', 'from app.services.email_service import'),
        (r'from auth import', 'from app.core.security import'),
        (r'from routers\.(\w+) import', r'from app.api.v1.endpoints.\1 import'),
    ]
    
    backend_files = list(Path("backend/app").rglob("*.py"))
    
    for file_path in backend_files:
        if file_path.name == "__init__.py":
            continue
            
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            print_success(f"Updated imports in {file_path.relative_to('backend')}")

def create_frontend_structure():
    """Create new frontend folder structure"""
    print_header("STEP 5: Create Frontend Structure")
    
    frontend_dirs = [
        "frontend/public",
        "frontend/src/assets/images",
        "frontend/src/assets/fonts",
        "frontend/src/components/common/Button",
        "frontend/src/components/common/Card",
        "frontend/src/components/common/Modal",
        "frontend/src/components/common/Loader",
        "frontend/src/components/layout/Navbar",
        "frontend/src/components/layout/Footer",
        "frontend/src/components/layout/Cursor",
        "frontend/src/components/features/hero",
        "frontend/src/components/features/skills",
        "frontend/src/components/features/projects",
        "frontend/src/components/features/about",
        "frontend/src/components/features/contact",
        "frontend/src/components/features/resume",
        "frontend/src/components/features/certifications",
        "frontend/src/components/features/admin",
        "frontend/src/pages/HomePage",
        "frontend/src/pages/AboutPage",
        "frontend/src/pages/SkillsPage",
        "frontend/src/pages/ProjectsPage",
        "frontend/src/pages/ContactPage",
        "frontend/src/pages/ResumePage",
        "frontend/src/pages/CertificationsPage",
        "frontend/src/pages/VaultPage",
        "frontend/src/context",
        "frontend/src/hooks",
        "frontend/src/services",
        "frontend/src/utils",
        "frontend/src/config",
        "frontend/tests",
    ]
    
    for dir_path in frontend_dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    
    print_success(f"Created {len(frontend_dirs)} directories")

def copy_frontend_files():
    """Copy and reorganize frontend files"""
    print_header("STEP 6: Copy Frontend Files")
    
    # Root files
    root_files = [
        ("package.json", "package.json"),
        ("package-lock.json", "package-lock.json"),
        ("vite.config.js", "vite.config.js"),
        ("index.html", "index.html"),
        (".env.development", ".env.development"),
        (".env.production", ".env.production"),
    ]
    
    for src, dst in root_files:
        src_path = Path("portfolio-frontend") / src
        dst_path = Path("frontend") / dst
        if src_path.exists():
            shutil.copy2(src_path, dst_path)
            print_success(f"{src} → frontend/{dst}")
    
    # Main entry files
    main_files = [
        ("src/main.jsx", "src/main.jsx"),
        ("src/App.jsx", "src/App.jsx"),
        ("src/App.css", "src/App.css"),
        ("src/index.css", "src/index.css"),
    ]
    
    for src, dst in main_files:
        src_path = Path("portfolio-frontend") / src
        dst_path = Path("frontend") / dst
        if src_path.exists():
            shutil.copy2(src_path, dst_path)
            print_success(f"{src} → frontend/{dst}")
    
    # Copy components (to be reorganized)
    components_src = Path("portfolio-frontend/src/components")
    if components_src.exists():
        # Layout components
        layout_comps = ["Navbar", "Footer", "Cursor"]
        for comp in layout_comps:
            for ext in [".jsx", ".css"]:
                src = components_src / f"{comp}{ext}"
                if src.exists():
                    dst = Path(f"frontend/src/components/layout/{comp}/{comp}{ext}")
                    shutil.copy2(src, dst)
                    print_success(f"components/{comp}{ext} → components/layout/{comp}/{comp}{ext}")
        
        # Feature components
        feature_mapping = {
            "Hero": "hero",
            "Skills": "skills",
            "Projects": "projects",
            "About": "about",
            "AboutCards": "about",
            "Contact": "contact",
            "ContactLinks": "contact",
            "ResumePanel": "resume",
            "ResumeUpload": "resume",
            "PhotoSlider": "hero",
            "DocumentVault": "admin",
            "ChangePassword": "admin",
            "ForgotPassword": "admin",
        }
        
        for comp, feature in feature_mapping.items():
            for ext in [".jsx", ".css"]:
                src = components_src / f"{comp}{ext}"
                if src.exists():
                    dst = Path(f"frontend/src/components/features/{feature}/{comp}{ext}")
                    shutil.copy2(src, dst)
                    print_success(f"components/{comp}{ext} → components/features/{feature}/{comp}{ext}")
    
    # Copy pages
    pages_src = Path("portfolio-frontend/src/pages")
    if pages_src.exists():
        for page_file in pages_src.glob("*"):
            if page_file.is_file():
                page_name = page_file.stem  # e.g., "HomePage"
                dst_dir = Path(f"frontend/src/pages/{page_name}")
                dst_dir.mkdir(exist_ok=True)
                dst = dst_dir / page_file.name
                shutil.copy2(page_file, dst)
                print_success(f"pages/{page_file.name} → pages/{page_name}/{page_file.name}")
    
    # Copy context
    context_src = Path("portfolio-frontend/src/context")
    if context_src.exists():
        shutil.copytree(context_src, Path("frontend/src/context"), dirs_exist_ok=True)
        print_success("Copied context/")
    
    # Copy data
    data_src = Path("portfolio-frontend/src/data")
    if data_src.exists():
        data_dst = Path("frontend/src/utils")
        shutil.copytree(data_src, data_dst, dirs_exist_ok=True)
        print_success("Copied data/ → utils/")
    
    # Move config
    config_src = Path("portfolio-frontend/src/config.js")
    if config_src.exists():
        dst = Path("frontend/src/config/config.js")
        shutil.copy2(config_src, dst)
        print_success("config.js → config/config.js")

def create_professional_files():
    """Create additional professional configuration files"""
    print_header("STEP 7: Create Professional Config Files")
    
    # Files already created by previous steps
    files_created = [
        ".editorconfig",
        ".gitattributes",
        "docker-compose.yml",
        "README.md",
        "backend/Dockerfile",
        "backend/.dockerignore",
        "backend/.env.example",
        "backend/requirements-dev.txt",
    ]
    
    for f in files_created:
        if Path(f).exists():
            print_success(f"Already created: {f}")

def print_final_instructions():
    """Print final manual steps"""
    print_header("REFACTOR COMPLETE!")
    
    print(f"\n{Color.BOLD}✅ What was done automatically:{Color.END}")
    print("  • Created new backend/ folder with professional structure")
    print("  • Created new frontend/ folder with organized components")
    print("  • Copied all files to new locations")
    print("  • Updated most import statements")
    print("  • Backed up original folders")
    
    print(f"\n{Color.BOLD}{Color.YELLOW}⚠️  Manual steps remaining:{Color.END}")
    print(f"\n{Color.BOLD}1. Update Frontend Imports{Color.END}")
    print("   • Open VS Code")
    print("   • Press Ctrl+Shift+H (Find & Replace in Files)")
    print("   • Set 'Files to include' to: frontend/src/**/*")
    print("   • Replace old import paths with new organized paths")
    
    print(f"\n{Color.BOLD}2. Test Backend Locally{Color.END}")
    print("   cd backend")
    print("   python -m uvicorn app.main:app --reload")
    print("   Visit: http://localhost:8000/docs")
    
    print(f"\n{Color.BOLD}3. Test Frontend Locally{Color.END}")
    print("   cd frontend")
    print("   npm install")
    print("   npm run dev")
    print("   Visit: http://localhost:3000")
    
    print(f"\n{Color.BOLD}4. Update Render/Vercel{Color.END}")
    print("   • Render start command: uvicorn app.main:app --host 0.0.0.0 --port $PORT")
    print("   • Vercel root directory: frontend")
    
    print(f"\n{Color.BOLD}5. Commit Changes{Color.END}")
    print("   git add .")
    print("   git commit -m 'refactor: professional folder structure'")
    print("   git push")
    
    print(f"\n{Color.BOLD}{Color.GREEN}📚 See MIGRATION_GUIDE.md for detailed instructions{Color.END}\n")

def main():
    print_header("PROFESSIONAL PORTFOLIO REFACTOR")
    print_info("This will reorganize your entire codebase")
    print_warning("Make sure you've committed your current work!")
    
    response = input(f"\n{Color.BOLD}Continue? (yes/no): {Color.END}").strip().lower()
    if response != 'yes':
        print_error("Refactor cancelled")
        return
    
    try:
        backup_existing()
        create_backend_structure()
        copy_backend_files()
        update_backend_imports()
        create_frontend_structure()
        copy_frontend_files()
        create_professional_files()
        print_final_instructions()
        
    except Exception as e:
        print_error(f"Error during refactor: {e}")
        print_warning("You can restore from Backend_backup/ and portfolio-frontend_backup/")
        raise

if __name__ == "__main__":
    main()
