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
cors_origins_str = os.getenv("CORS_ORIGINS", "") 
if cors_origins_str:
    try:
        import json
        allowed_origins = json.loads(cors_origins_str)
    except:
        allowed_origins = ["*"]
else:
    allowed_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/uploads/gallery", StaticFiles(directory=str(GALLERY_DIR)), name="gallery")
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
