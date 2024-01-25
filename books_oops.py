from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=5)

BOOKS = [
    Book(1, 'Computer Science Pro', 'Ferose ali', 'A very nice book', 5),
    Book(2, 'Alchemy', 'Shefeena ferose', 'this is a great book', 4),
    Book(3, 'Do or die', 'Abu prince', 'A must read book', 5),
    Book(4, 'Life of jackass', 'Muhammed Zayn', 'Good to read for inspiration', 3),
    Book(5, 'Fundamentals of Algorithm', 'Aliyarukunju', 'Its hard to read book', 2),
    Book(6, 'Kill me or suicide yourself', 'Najeema Ali', 'Good for a computer science lad', 4),
]


@app.get('/')
async def get_all_books():
    return BOOKS


@app.post('/create_book')
async def create_book(book_request=Body()):
    BOOKS.append(book_request)
    return BOOKS

# Used the Pydantic Data validation
@app.post('/create-book')
async def createBook(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
    return BOOKS