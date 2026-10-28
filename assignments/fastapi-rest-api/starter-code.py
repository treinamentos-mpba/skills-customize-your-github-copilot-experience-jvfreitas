from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/books", response_model=list[Book])
def list_books():
    # Return all books.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    # Assign an ID, save the book, and return it.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # Return the requested book or raise HTTPException with status 404.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate):
    # Replace the book's title and author or raise HTTPException with status 404.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # Delete the requested book or raise HTTPException with status 404.
    pass
