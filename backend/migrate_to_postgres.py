"""
SQLite to PostgreSQL Migration Script
Migrates all data from SQLite to PostgreSQL
"""

import asyncio
import aiosqlite
import asyncpg
import os
from pathlib import Path

# Configuration
SQLITE_DB = Path(__file__).parent / "portfolio.db"
POSTGRES_URL = os.getenv("DATABASE_URL", "")

# Convert postgres:// to postgresql://
if POSTGRES_URL.startswith("postgres://"):
    POSTGRES_URL = POSTGRES_URL.replace("postgres://", "postgresql://", 1)


async def migrate():
    """Migrate data from SQLite to PostgreSQL"""
    
    if not POSTGRES_URL:
        print("❌ ERROR: DATABASE_URL environment variable not set!")
        print("Set it with your PostgreSQL connection string:")
        print('export DATABASE_URL="postgres://user:pass@host:5432/dbname"')
        return
    
    if not SQLITE_DB.exists():
        print(f"❌ ERROR: SQLite database not found at {SQLITE_DB}")
        return
    
    print("🔄 Starting migration from SQLite to PostgreSQL...")
    print(f"   SQLite: {SQLITE_DB}")
    print(f"   PostgreSQL: {POSTGRES_URL[:30]}...")
    
    # Connect to both databases
    sqlite_conn = await aiosqlite.connect(SQLITE_DB)
    sqlite_conn.row_factory = aiosqlite.Row
    
    pg_conn = await asyncpg.connect(POSTGRES_URL)
    
    try:
        # Tables to migrate (in order due to foreign keys)
        tables = [
            "admin",
            "skill_categories",
            "skills",
            "contact_messages",
            "resume",
            "resume_media",
            "projects",
            "code_card",
            "certifications",
            "hero_video",
            "documents",
            "gallery_images",
            "about_cards",
            "contact_links",
        ]
        
        for table in tables:
            print(f"\n📦 Migrating table: {table}")
            
            # Get all rows from SQLite
            cursor = await sqlite_conn.execute(f"SELECT * FROM {table}")
            rows = await cursor.fetchall()
            
            if not rows:
                print(f"   ⚠️  No data in {table}")
                continue
            
            print(f"   Found {len(rows)} rows")
            
            # Get column names
            columns = [desc[0] for desc in cursor.description]
            
            # Skip 'id' column for auto-increment
            insert_columns = [col for col in columns if col != 'id']
            placeholders = ", ".join([f"${i+1}" for i in range(len(insert_columns))])
            column_names = ", ".join(insert_columns)
            
            # Insert into PostgreSQL
            inserted = 0
            for row in rows:
                row_dict = dict(row)
                values = [row_dict[col] for col in insert_columns]
                
                try:
                    await pg_conn.execute(
                        f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})",
                        *values
                    )
                    inserted += 1
                except Exception as e:
                    print(f"   ⚠️  Error inserting row: {e}")
                    continue
            
            print(f"   ✅ Inserted {inserted}/{len(rows)} rows")
            
            # Reset sequence for auto-increment
            await pg_conn.execute(f"""
                SELECT setval(pg_get_serial_sequence('{table}', 'id'), 
                              COALESCE((SELECT MAX(id) FROM {table}), 1), 
                              true)
            """)
        
        print("\n✅ Migration completed successfully!")
        print("\n📋 Summary:")
        for table in tables:
            result = await pg_conn.fetchval(f"SELECT COUNT(*) FROM {table}")
            print(f"   {table}: {result} rows")
        
    except Exception as e:
        print(f"\n❌ Migration failed: {e}")
        raise
    
    finally:
        await sqlite_conn.close()
        await pg_conn.close()


if __name__ == "__main__":
    asyncio.run(migrate())
