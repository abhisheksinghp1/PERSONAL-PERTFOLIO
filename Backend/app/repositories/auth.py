"""
Admin Repository
Handles database operations for admin authentication
"""

from typing import Optional
import aiosqlite
from .base import BaseRepository


class AdminRepository(BaseRepository):
    """Repository for admin users"""
    
    def __init__(self, db: aiosqlite.Connection):
        super().__init__(db, "admin")
    
    async def get_by_username(self, username: str) -> Optional[dict]:
        """Get admin by username"""
        cursor = await self.db.execute(
            "SELECT * FROM admin WHERE username=?",
            (username,)
        )
        row = await cursor.fetchone()
        return dict(row) if row else None
    
    async def verify_credentials(self, username: str, password_hash: str) -> Optional[dict]:
        """Verify admin credentials"""
        cursor = await self.db.execute(
            "SELECT id, username FROM admin WHERE username=? AND password_hash=?",
            (username, password_hash)
        )
        row = await cursor.fetchone()
        return dict(row) if row else None
    
    async def update_password(self, username: str, new_password_hash: str) -> bool:
        """Update admin password"""
        cursor = await self.db.execute(
            "UPDATE admin SET password_hash=? WHERE username=?",
            (new_password_hash, username)
        )
        await self.db.commit()
        return cursor.rowcount > 0
