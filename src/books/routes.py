from fastapi import FastAPI,Header
from typing import Optional, List
from schemas import BookCreateModel

app = FastAPI()

@app.get('/')
async def get():
    return {'message': 'Hello, World!'}

@app.get('/greet')
async def get_ded(name:Optional[str] = "user" , age:int = 24) -> dict:
    return {'message': f"This is a {name}" , "age":age}

@app.post('/create_book')
async def create_book(book_data:BookCreateModel):
    return {'title' : book_data.title, 
            'author' : book_data.author , 
            'publication_year' : book_data.publication_year}    
    

@app.get('/get_header')
async def getHead(accept:str = Header(None)):
    request_headers = {}
    request_headers['Accept'] = accept
    return request_headers