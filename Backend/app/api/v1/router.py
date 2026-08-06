"""API v1 Router - Aggregates all endpoints"""

from fastapi import APIRouter

from app.api.v1.endpoints import (
    auth, skills, projects, contact, resume,
    documents, gallery, about, contact_links,
    resume_media, hero_video, code_card, certifications
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(skills.router, prefix="/skills", tags=["Skills"])
api_router.include_router(projects.router, prefix="/projects", tags=["Projects"])
api_router.include_router(contact.router, prefix="/contact", tags=["Contact"])
api_router.include_router(resume.router, prefix="/resume", tags=["Resume"])
api_router.include_router(documents.router, prefix="/documents", tags=["Documents"])
api_router.include_router(gallery.router, prefix="/gallery", tags=["Gallery"])
api_router.include_router(about.router, prefix="/about", tags=["About"])
api_router.include_router(contact_links.router, prefix="/contact-links", tags=["ContactLinks"])
api_router.include_router(resume_media.router, prefix="/resume-media", tags=["ResumeMedia"])
api_router.include_router(hero_video.router, prefix="/hero-video", tags=["HeroVideo"])
api_router.include_router(code_card.router, prefix="/code-card", tags=["CodeCard"])
api_router.include_router(certifications.router, prefix="/certifications", tags=["Certifications"])
