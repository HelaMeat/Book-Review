from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from src.books.models import Book

engine = AsyncEngine(
        create_engine(
        url = Config.DATABASE_URL,
        echo = True
    )
)

async def init_db():
    async with engine.begin() as conn:
        
        await conn.execute(text("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, publisher TEXT, publication_year INTEGER, page_count INTEGER, language TEXT)"))