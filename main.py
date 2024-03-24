import random
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from mangum import Mangum
from models import get_books, store_books, Book


app = FastAPI()
handler = Mangum(app)

BOOKS = get_books() # fetch books from json file


@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/list-books")
async def list_books():  
    return {"books": BOOKS}

@app.get("/random-book")
async def random_book():
    return random.choice(BOOKS)

@app.post("/add-book")
async def add_book(book: Book):
    book.book_id = uuid4().hex
    json_book = jsonable_encoder(book)
    BOOKS.append(json_book)
    # add book to json file.
    await store_books(BOOKS)
    return {"Book": json_book}

@app.get("/book-by-index/{index}")
async def book_by_index(index: int):
    if index-1 < len(BOOKS):
        return BOOKS[index]
    else:
        return HTTPException(status_code=404, detail=f"Book index [{index}] out of range [{len(BOOKS)}]")
    
@app.delete("/book-by-index")
async def remove_book(book_index: int):
    if book_index-1 > len(BOOKS):
            return HTTPException(status_code=404, detail=f"Book index [{book_index}] out of range [{len(BOOKS)}]")
    deleted_book = BOOKS.pop(book_index-1)
    await store_books(BOOKS)
    return {"Result":f"Book {deleted_book} on index [{book_index}] removed Successfully."}