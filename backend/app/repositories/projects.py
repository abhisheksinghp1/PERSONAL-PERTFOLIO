"""
Projects Repository
Handles database operations for projects
"""

from typing import List, Optional
import aiosqlite
import json
from .base import BaseRepository


class ProjectsRepository(BaseRepository):
    """Repository for projects"""
    
    def __init__(self, db: aiosqlite.Connection):
        super().__init__(db, "projects")
    
    async def get_all(self, order_by: str = "sort_order", order_dir: str = "ASC") -> List[dict]:
        """Get all projects with parsed tech array"""
        projects = await super().get_all(order_by, order_dir)
        
        for project in projects:
            # Parse tech JSON string to list
            try:
                project['tech'] = json.loads(project.get('tech', '[]'))
            except (json.JSONDecodeError, TypeError):
                project['tech'] = []
            
            # Add stats object
            project['stats'] = {
                'stars': project.pop('stars', 0),
                'forks': project.pop('forks', 0)
            }
        
        return projects
    
    async def get_by_id(self, id: int) -> Optional[dict]:
        """Get project by ID with parsed tech array"""
        project = await super().get_by_id(id)
        
        if project:
            try:
                project['tech'] = json.loads(project.get('tech', '[]'))
            except (json.JSONDecodeError, TypeError):
                project['tech'] = []
            
            project['stats'] = {
                'stars': project.pop('stars', 0),
                'forks': project.pop('forks', 0)
            }
        
        return project
    
    async def create(self, data: dict) -> int:
        """Create project with JSON tech array"""
        if 'tech' in data and isinstance(data['tech'], list):
            data['tech'] = json.dumps(data['tech'])
        
        return await super().create(data)
    
    async def update(self, id: int, data: dict) -> bool:
        """Update project with JSON tech array"""
        if 'tech' in data and isinstance(data['tech'], list):
            data['tech'] = json.dumps(data['tech'])
        
        return await super().update(id, data)
    
    async def get_next_sort_order(self) -> int:
        """Get the next available sort order"""
        cursor = await self.db.execute("SELECT MAX(sort_order) FROM projects")
        row = await cursor.fetchone()
        return (row[0] or 0) + 1
