from database.data import books, authors

async def get_books():
    books_list = books
    for book in books_list:
        author = next((author for author in authors if author["id"] == book["authorId"]), None)
        book["author"] = author
    return books_list

async def get_book_by_id(id):
    return next((book for book in books if book["id"] == id), None)

async def create_book(title, author_id):
    books_next_id = max([int(book["id"]) for book in books]) + 1
    book = {
        "id": str(books_next_id),
        "title": title,
        "author_id": author_id
    }
    books.append(book)
    return book

async def update_book(id, title, author_id):
    book = await get_book_by_id(id)
    if book:
        book["title"] = title
        book["author_id"] = author_id
        return book


async def delete_book(id):
    book = await get_book_by_id(id)
    if book:
        books.remove(book)
        return book
