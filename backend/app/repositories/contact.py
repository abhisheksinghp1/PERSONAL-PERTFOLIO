"""
Contact Repository
Handles database operations for contact messages and links
"""

from typing import List
import aiosqlite
from .base import BaseRepository


class ContactRepository(BaseRepository):
    """Repository for contact messages"""
    
    def __init__(self, db: aiosqlite.Connection):
        super().__init__(db, "contact_messages")
    
    async def get_all(self, order_by: str = "created_at", order_dir: str = "DESC") -> List[dict]:
        """Get all contact messages ordered by creation date"""
        return await super().get_all(order_by, order_dir)


class ContactLinksRepository(BaseRepository):
    """Repository for contact/social links"""
    
    def __init__(self, db: aiosqlite.Connection):
        super().__init__(db, "contact_links")
    
    async def get_all(self, order_by: str = "sort_order", order_dir: str = "ASC") -> List[dict]:
        """Get all contact links ordered by sort_order"""
        return await super().get_all(order_by, order_dir)
    
    async def reorder(self, items: List[dict]) -> bool:
        """Reorder contact links"""
        for item in items:
            await self.db.execute(
                "UPDATE contact_links SET sort_order=? WHERE id=?",
                (item['sort_order'], item['id'])
            )
        await self.db.commit()
        return True
    
    async def get_next_sort_order(self) -> int:
        """Get the next available sort order"""
        cursor = await self.db.execute("SELECT MAX(sort_order) FROM contact_links")
        row = await cursor.fetchone()
        return (row[0] or 0) + 1
