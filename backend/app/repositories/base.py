"""
Base Repository
Provides common CRUD operations for all repositories
"""

from typing import Generic, TypeVar, Optional, List, Any
import aiosqlite

T = TypeVar('T')


class BaseRepository(Generic[T]):
    """Base repository with common CRUD operations"""
    
    def __init__(self, db: aiosqlite.Connection, table_name: str):
        self.db = db
        self.table_name = table_name
    
    async def get_by_id(self, id: int) -> Optional[dict]:
        """Get a single record by ID"""
        cursor = await self.db.execute(
            f"SELECT * FROM {self.table_name} WHERE id = ?",
            (id,)
        )
        row = await cursor.fetchone()
        return dict(row) if row else None
    
    async def get_all(self, order_by: str = "id", order_dir: str = "ASC") -> List[dict]:
        """Get all records"""
        cursor = await self.db.execute(
            f"SELECT * FROM {self.table_name} ORDER BY {order_by} {order_dir}"
        )
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]
    
    async def create(self, data: dict) -> int:
        """Create a new record and return its ID"""
        columns = ", ".join(data.keys())
        placeholders = ", ".join("?" * len(data))
        
        cursor = await self.db.execute(
            f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})",
            tuple(data.values())
        )
        await self.db.commit()
        return cursor.lastrowid
    
    async def update(self, id: int, data: dict) -> bool:
        """Update a record by ID"""
        set_clause = ", ".join(f"{k}=?" for k in data.keys())
        
        cursor = await self.db.execute(
            f"UPDATE {self.table_name} SET {set_clause} WHERE id=?",
            (*data.values(), id)
        )
        await self.db.commit()
        return cursor.rowcount > 0
    
    async def delete(self, id: int) -> bool:
        """Delete a record by ID"""
        cursor = await self.db.execute(
            f"DELETE FROM {self.table_name} WHERE id=?",
            (id,)
        )
        await self.db.commit()
        return cursor.rowcount > 0
    
    async def exists(self, id: int) -> bool:
        """Check if a record exists"""
        cursor = await self.db.execute(
            f"SELECT 1 FROM {self.table_name} WHERE id=? LIMIT 1",
            (id,)
        )
        row = await cursor.fetchone()
        return row is not None
    
    async def count(self) -> int:
        """Count total records"""
        cursor = await self.db.execute(
            f"SELECT COUNT(*) as count FROM {self.table_name}"
        )
        row = await cursor.fetchone()
        return row["count"] if row else 0
