from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    publication_year: int
    page_count: int
    language: str

class BookCreateModel(BaseModel):
    title: str
    author: str
    publication_year: int
    
    
class BookUpdateModel(BaseModel):
    title: str 
    author: str 
    publisher: str 
    page_count: int
    language: str