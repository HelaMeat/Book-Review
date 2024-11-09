from uuid import UUID
from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime

class Book():
    uid: UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            default=lambda: UUID(int=datetime.now().timestamp())
        )
    )
    title: str
    author: str
    publisher: str
    publication_year: int
    page_count: int
    language: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self) -> str:
        return f"<Book {self.title}"