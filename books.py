from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'One', 'author': 'author 1', 'category': 'biology'},
    {'title': 'Two', 'author': 'author 2', 'category': 'maths'},
    {'title': 'Three', 'author': 'author 3', 'category': 'english'},
    {'title': 'Four', 'author': 'author 4', 'category': 'chemistry'},
    {'title': 'Five', 'author': 'author 2', 'category': 'science'},
    {'title': 'Six', 'author': 'author 7', 'category': 'malayalam'},
]


# Endpoint order matters

# Get Request Methods

@app.get('/books')
async def read_all_books():
    return BOOKS

# Query parameters
@app.get('/books/')
def read_category_by_param(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return        

# Path parameters
@app.get('/books/{book_title}')
def read_books(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

# Get all books from a specific author using path or query param
@app.get('/books/byauthor/{author}')
async def read_book_by_author(author :str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get('/books/{dynamic_param}')
async def read_book(dynamic_param):
    return {'dynamic_param': dynamic_param}

# Combination of both Path param and Query param
@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

########################################################################

# POST Request Methods

@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS

########################################################################

# PUT Request Methods

@app.put('/books/update_book')
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
    return BOOKS

########################################################################

# DELETE Request Methods
@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
    return BOOKS