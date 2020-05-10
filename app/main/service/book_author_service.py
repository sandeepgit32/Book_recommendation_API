from app.main import db
from app.main.model.book import Book
from app.main.model.author import Author
from app.main.model.book_author import BookAuthor


def get_all_bookauthors():
    return BookAuthor.query.all()
