"""
Skills Repository
Handles database operations for skills and categories
"""

from typing import List, Optional
import aiosqlite
from .base import BaseRepository


class SkillCategoryRepository(BaseRepository):
    """Repository for skill categories"""
    
    def __init__(self, db: aiosqlite.Connection):
        super().__init__(db, "skill_categories")
    
    async def get_with_skills(self) -> List[dict]:
        """Get all categories with their skills"""
        categories = await self.get_all(order_by="sort_order")
        
        for category in categories:
            cursor = await self.db.execute(
                "SELECT id, name, level, sort_order, image_url "
                "FROM skills WHERE category_id=? ORDER BY sort_order, id",
                (category["id"],)
            )
            skills = await cursor.fetchall()
            category["skills"] = [dict(skill) for skill in skills]
        
        return categories
    
    async def get_by_name(self, name: str) -> Optional[dict]:
        """Get category by name"""
        cursor = await self.db.execute(
            f"SELECT * FROM {self.table_name} WHERE name=?",
            (name,)
        )
        row = await cursor.fetchone()
        return dict(row) if row else None


class SkillsRepository(BaseRepository):
    """Repository for skills"""
    
    def __init__(self, db: aiosqlite.Connection):
        super().__init__(db, "skills")
    
    async def get_by_category(self, category_id: int) -> List[dict]:
        """Get all skills in a category"""
        cursor = await self.db.execute(
            "SELECT * FROM skills WHERE category_id=? ORDER BY sort_order, id",
            (category_id,)
        )
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]
    
    async def update_image(self, skill_id: int, image_url: str) -> bool:
        """Update skill image URL"""
        return await self.update(skill_id, {"image_url": image_url})
    
    async def remove_image(self, skill_id: int) -> bool:
        """Remove skill image"""
        return await self.update(skill_id, {"image_url": ""})
