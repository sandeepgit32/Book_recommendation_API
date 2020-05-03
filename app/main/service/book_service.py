import uuid
from app.main import db
from app.main.model.book import Book
from app.main.model.author import Author
from app.main.model.book_author import BookAuthor
from app.main.model.category import Category
from sqlalchemy import text


def save_new_book(data):
    book = Book.query.filter_by(name=data['name']).first()
    if not book:
        category_id = data['category_id']
        category = Category.query.filter(Category.public_id == category_id).one()
        if 'public_id' in data.keys():
            public_id = data['public_id']
        else:
            public_id = str(uuid.uuid4())
        new_book = Book(
            public_id=public_id,
            name=data['name'],
            publisher=data['publisher'],
            rating=data['rating'],
            category=category
        )
        save_changes(new_book)
        response_object = {
            'status': 'success',
            'message': 'Successfully added.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'failed',
            'message': 'Book already exists.'
        }
        return response_object, 409


def get_all_books():
    return Book.query.all()


def get_a_book(public_id):
    return Book.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
