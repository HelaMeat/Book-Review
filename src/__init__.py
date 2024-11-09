from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

# This context manager is used to initialize the database and close when the server stops.
@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server starting")
    await init_db()
    yield 
    print(f"server stopped")

version = 'v1'
 
app = FastAPI(
    lifespan=life_span,
    version = version
)

app.include_router(book_router, prefix=f'/api/{version}/books', tags=['books'])