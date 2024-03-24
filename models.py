
import json
import os
from typing import Literal
from uuid import uuid4
from pydantic import BaseModel


class Book(BaseModel):
    name: str
    price: float
    genre: Literal["fiction", "non-fiction"]
    book_id:  str| None = uuid4().hex


BOOKS_DATA_SOURCE = "books.json"


def get_books():
    BOOKS=[]
    if os.path.exists(BOOKS_DATA_SOURCE):
        with open(BOOKS_DATA_SOURCE, "r") as f:
            json_data = f.read()
            BOOKS= json.loads(json_data)
    return BOOKS

async def store_books(books: list[Book]):
        with open(BOOKS_DATA_SOURCE, "w") as f:
             json.dump(books, f)

