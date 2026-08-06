#!/usr/bin/env python3
"""
Automated backend refactor script
Reorganizes Backend/ into professional backend/ structure
"""

import shutil
import os
from pathlib import Path

# Define the source and destination
OLD_BACKEND = Path("Backend")
NEW_BACKEND = Path("backend")

def main():
    print("🚀 Starting backend refactor...")
    
    # Create new structure
    print("\n📁 Creating new directory structure...")
    dirs = [
        NEW_BACKEND / "app",
        NEW_BACKEND / "app/api/v1/endpoints",
        NEW_BACKEND / "app/core",
        NEW_BACKEND / "app/db",
        NEW_BACKEND / "app/schemas",
        NEW_BACKEND / "app/services",
        NEW_BACKEND / "tests",
        NEW_BACKEND / "uploads",
    ]
    
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        (d / "__init__.py").touch()
    
    print("✅ Directory structure created")
    
    # Copy files to new locations
    print("\n📦 Copying files...")
    
    # Root files
    files_to_copy = [
        ("requirements.txt", "requirements.txt"),
        ("requirements-dev.txt", "requirements-dev.txt"),
        (".python-version", ".python-version"),
        (".env.example", ".env.example"),
        (".env", ".env"),  # If exists
        ("Dockerfile", "Dockerfile"),
        (".dockerignore", ".dockerignore"),
    ]
    
    for src, dst in files_to_copy:
        src_path = OLD_BACKEND / src
        dst_path = NEW_BACKEND / dst
        if src_path.exists():
            shutil.copy2(src_path, dst_path)
            print(f"  ✓ {src} → {dst}")
    
    # Core files
    if (OLD_BACKEND / "config.py").exists():
        shutil.copy2(OLD_BACKEND / "config.py", NEW_BACKEND / "app/config.py")
        print(f"  ✓ config.py → app/config.py")
    
    if (OLD_BACKEND / "database.py").exists():
        shutil.copy2(OLD_BACKEND / "database.py", NEW_BACKEND / "app/db/database.py")
        print(f"  ✓ database.py → app/db/database.py")
    
    if (OLD_BACKEND / "auth.py").exists():
        shutil.copy2(OLD_BACKEND / "auth.py", NEW_BACKEND / "app/core/security.py")
        print(f"  ✓ auth.py → app/core/security.py")
    
    if (OLD_BACKEND / "email_service.py").exists():
        shutil.copy2(OLD_BACKEND / "email_service.py", NEW_BACKEND / "app/services/email_service.py")
        print(f"  ✓ email_service.py → app/services/email_service.py")
    
    if (OLD_BACKEND / "models.py").exists():
        shutil.copy2(OLD_BACKEND / "models.py", NEW_BACKEND / "app/schemas/models.py")
        print(f"  ✓ models.py → app/schemas/models.py")
    
    # Copy routers
    routers_dir = OLD_BACKEND / "routers"
    if routers_dir.exists():
        endpoints_dir = NEW_BACKEND / "app/api/v1/endpoints"
        for router_file in routers_dir.glob("*.py"):
            if router_file.name != "__init__.py":
                shutil.copy2(router_file, endpoints_dir / router_file.name)
                print(f"  ✓ routers/{router_file.name} → app/api/v1/endpoints/{router_file.name}")
    
    # Copy uploads if exists
    uploads_src = OLD_BACKEND / "uploads"
    uploads_dst = NEW_BACKEND / "uploads"
    if uploads_src.exists():
        if uploads_dst.exists():
            shutil.rmtree(uploads_dst)
        shutil.copytree(uploads_src, uploads_dst)
        print(f"  ✓ uploads/ → uploads/")
    
    print("\n✅ Files copied successfully!")
    print("\n⚠️  IMPORTANT: You still need to:")
    print("  1. Update all import statements in the new files")
    print("  2. Create app/main.py with the new structure")
    print("  3. Create app/api/v1/router.py to aggregate endpoints")
    print("  4. Test the new structure locally")
    print("  5. Update Render start command to: uvicorn app.main:app --host 0.0.0.0 --port $PORT")
    print("\n📚 See MIGRATION_GUIDE.md for detailed import updates")

if __name__ == "__main__":
    main()
