import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from pathlib import Path

from app.db.database import init_db, GALLERY_DIR, SKILL_IMAGES_DIR
from app.api.v1.router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title="Abhishek Pratap Singh — Portfolio API",
    version="2.0.0",
    description="Professional portfolio backend with admin panel",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# CORS
from app.config import settings

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.cors_origin] if settings.cors_origin != "*" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (only if directories exist)
if GALLERY_DIR.exists():
    app.mount("/uploads/gallery", StaticFiles(directory=str(GALLERY_DIR)), name="gallery")
if SKILL_IMAGES_DIR.exists():
    app.mount("/uploads/skill_images", StaticFiles(directory=str(SKILL_IMAGES_DIR)), name="skill_images")

# API routes
app.include_router(api_router, prefix="/api")


# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "2.0.0"}


@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "Portfolio API v2 running",
        "docs": "/docs",
        "health": "/health"
    }
