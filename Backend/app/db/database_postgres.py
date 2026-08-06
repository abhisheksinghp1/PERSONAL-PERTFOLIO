"""
PostgreSQL Database Configuration
Production-ready async PostgreSQL with SQLAlchemy
"""

import os
from pathlib import Path
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import text

# Database URL from environment (Render provides this)
DATABASE_URL = os.getenv("DATABASE_URL", "")

# Convert postgres:// to postgresql+asyncpg:// for SQLAlchemy
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)

# File storage paths
_BASE = Path(os.getenv("DATA_DIR", str(Path(__file__).parent.parent.parent)))
UPLOAD_DIR = _BASE / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

DOCS_DIR = UPLOAD_DIR / "documents"
DOCS_DIR.mkdir(exist_ok=True)

GALLERY_DIR = UPLOAD_DIR / "gallery"
GALLERY_DIR.mkdir(exist_ok=True)

RESUME_MEDIA_DIR = UPLOAD_DIR / "resume_media"
RESUME_MEDIA_DIR.mkdir(exist_ok=True)

SKILL_IMAGES_DIR = UPLOAD_DIR / "skill_images"
SKILL_IMAGES_DIR.mkdir(exist_ok=True)

HERO_VIDEO_DIR = UPLOAD_DIR / "hero_video"
HERO_VIDEO_DIR.mkdir(exist_ok=True)

CERT_DIR = UPLOAD_DIR / "certifications"
CERT_DIR.mkdir(exist_ok=True)

# SQLAlchemy setup
Base = declarative_base()

# Create async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # Set to True for SQL debug logging
    pool_pre_ping=True,  # Verify connections before using
    pool_size=5,
    max_overflow=10,
)

# Session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    """Dependency for FastAPI endpoints"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


async def init_db():
    """Initialize database schema and seed data"""
    async with engine.begin() as conn:
        # Create all tables
        await conn.run_sync(Base.metadata.create_all)
        
        # Create tables with raw SQL
        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS contact_messages (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                subject TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT NOW()
            )
        """))

        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS admin (
                id SERIAL PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL
            )
        """))

        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS skill_categories (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                icon TEXT NOT NULL DEFAULT '⚙️',
                color TEXT NOT NULL DEFAULT '#6c63ff',
                sort_order INTEGER NOT NULL DEFAULT 0
            )
        """))

        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS skills (
                id SERIAL PRIMARY KEY,
                category_id INTEGER NOT NULL REFERENCES skill_categories(id) ON DELETE CASCADE,
                name TEXT NOT NULL,
                level INTEGER NOT NULL DEFAULT 80,
                sort_order INTEGER NOT NULL DEFAULT 0,
                image_url TEXT NOT NULL DEFAULT ''
            )
        """))

        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS resume (
                id SERIAL PRIMARY KEY,
                filename TEXT NOT NULL,
                uploaded_at TIMESTAMP NOT NULL DEFAULT NOW()
            )
        """))

        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS resume_media (
                id SERIAL PRIMARY KEY,
                type TEXT NOT NULL CHECK(type IN ('image','video')),
                filename TEXT NOT NULL,
                original_name TEXT NOT NULL,
                mime_type TEXT NOT NULL,
                size_bytes INTEGER NOT NULL,
                uploaded_at TIMESTAMP NOT NULL DEFAULT NOW()
            )
        """))

        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS projects (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                tech TEXT NOT NULL DEFAULT '[]',
                github TEXT NOT NULL DEFAULT '#',
                live TEXT NOT NULL DEFAULT '#',
                color TEXT NOT NULL DEFAULT '#6c63ff',
                icon TEXT NOT NULL DEFAULT '🚀',
                stars INTEGER NOT NULL DEFAULT 0,
                forks INTEGER NOT NULL DEFAULT 0,
                sort_order INTEGER NOT NULL DEFAULT 0,
                created_at TIMESTAMP NOT NULL DEFAULT NOW()
            )
        """))

        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS code_card (
                id SERIAL PRIMARY KEY,
                filename TEXT NOT NULL DEFAULT 'developer.py',
                content TEXT NOT NULL,
                updated_at TIMESTAMP NOT NULL DEFAULT NOW()
            )
        """))

        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS certifications (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                organization TEXT NOT NULL,
                description TEXT NOT NULL DEFAULT '',
                issue_date TEXT NOT NULL DEFAULT '',
                credential_id TEXT NOT NULL DEFAULT '',
                pdf_filename TEXT NOT NULL DEFAULT '',
                img_filename TEXT NOT NULL DEFAULT '',
                card_color TEXT NOT NULL DEFAULT '#6c63ff',
                created_at TIMESTAMP NOT NULL DEFAULT NOW()
            )
        """))

        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS hero_video (
                id SERIAL PRIMARY KEY,
                filename TEXT NOT NULL,
                mime_type TEXT NOT NULL DEFAULT 'video/mp4',
                media_type TEXT NOT NULL DEFAULT 'video',
                sort_order INTEGER NOT NULL DEFAULT 0,
                uploaded_at TIMESTAMP NOT NULL DEFAULT NOW()
            )
        """))

        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS documents (
                id SERIAL PRIMARY KEY,
                filename TEXT NOT NULL,
                original_name TEXT NOT NULL,
                mime_type TEXT NOT NULL,
                size_bytes INTEGER NOT NULL,
                uploaded_at TIMESTAMP NOT NULL DEFAULT NOW()
            )
        """))

        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS gallery_images (
                id SERIAL PRIMARY KEY,
                filename TEXT NOT NULL,
                caption TEXT DEFAULT '',
                media_type TEXT NOT NULL DEFAULT 'image',
                sort_order INTEGER NOT NULL DEFAULT 0,
                uploaded_at TIMESTAMP NOT NULL DEFAULT NOW()
            )
        """))

        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS about_cards (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                emoji TEXT NOT NULL DEFAULT '✨',
                color TEXT NOT NULL DEFAULT '#6c63ff',
                sort_order INTEGER NOT NULL DEFAULT 0,
                created_at TIMESTAMP NOT NULL DEFAULT NOW()
            )
        """))

        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS contact_links (
                id SERIAL PRIMARY KEY,
                label TEXT NOT NULL,
                value TEXT NOT NULL,
                url TEXT NOT NULL DEFAULT '',
                icon TEXT NOT NULL DEFAULT '🔗',
                type TEXT NOT NULL DEFAULT 'link',
                sort_order INTEGER NOT NULL DEFAULT 0,
                created_at TIMESTAMP NOT NULL DEFAULT NOW()
            )
        """))

    # Seed default data
    await seed_default_data()


async def seed_default_data():
    """Seed database with default data"""
    async with AsyncSessionLocal() as session:
        from app.config import settings
        import hashlib
        
        # Check if admin exists
        result = await session.execute(text("SELECT COUNT(*) FROM admin"))
        admin_count = result.scalar()
        
        if admin_count == 0:
            # Create default admin
            admin_user = settings.admin_username.strip()
            admin_pass = settings.admin_password.strip()
            if admin_user and admin_pass:
                pw_hash = hashlib.sha256(admin_pass.encode()).hexdigest()
                await session.execute(
                    text("INSERT INTO admin (username, password_hash) VALUES (:u, :p)"),
                    {"u": admin_user, "p": pw_hash}
                )
                await session.commit()
        
        # Seed skill categories
        result = await session.execute(text("SELECT COUNT(*) FROM skill_categories"))
        cat_count = result.scalar()
        
        if cat_count == 0:
            categories = [
                ("Backend", "⚙️", "#6c63ff", 1),
                ("DevOps", "🚀", "#43e97b", 2),
                ("Database", "🗄️", "#ff6584", 3),
            ]
            for name, icon, color, order in categories:
                await session.execute(
                    text("INSERT INTO skill_categories (name, icon, color, sort_order) VALUES (:n, :i, :c, :o)"),
                    {"n": name, "i": icon, "c": color, "o": order}
                )
            await session.commit()
        
        # Seed skills
        result = await session.execute(text("SELECT COUNT(*) FROM skills"))
        skill_count = result.scalar()
        
        if skill_count == 0:
            skills_data = [
                ("Backend", "Python", 95, 1),
                ("Backend", "FastAPI", 90, 2),
                ("Backend", "Django", 88, 3),
                ("DevOps", "Docker", 88, 1),
                ("DevOps", "Kubernetes", 80, 2),
                ("Database", "PostgreSQL", 85, 1),
                ("Database", "MySQL", 82, 2),
            ]
            
            for cat_name, skill_name, level, order in skills_data:
                result = await session.execute(
                    text("SELECT id FROM skill_categories WHERE name = :n"),
                    {"n": cat_name}
                )
                cat_id = result.scalar()
                if cat_id:
                    await session.execute(
                        text("INSERT INTO skills (category_id, name, level, sort_order) VALUES (:c, :n, :l, :o)"),
                        {"c": cat_id, "n": skill_name, "l": level, "o": order}
                    )
            await session.commit()


async def execute_query(query: str, params: dict = None):
    """Execute a raw SQL query"""
    async with AsyncSessionLocal() as session:
        result = await session.execute(text(query), params or {})
        await session.commit()
        return result
