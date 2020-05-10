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
        category = Category.query.filter_by(public_id=category_id).first()
        if not category:
            new_category = Category(
                name=data['category_name'],
                public_id=category_id
            )
            save_changes(new_category)
        else:
            new_category = category
        # category = Category.query.filter(Category.public_id == category_id).one()
        if 'public_id' in data.keys():
            book_id = data['public_id']
        else:
            book_id = str(uuid.uuid4())
        new_book = Book(
            public_id=book_id,
            name=data['name'],
            publisher=data['publisher'],
            # rating=data['rating'],
            category=new_category
        )
        save_changes(new_book)

        author_list = data['authors']
        for item in author_list:
            author_id = item['author_id']
            author = Author.query.filter_by(public_id=author_id).first()
            if not author:
                author_name = item['author_name']
                new_author = Author(
                    public_id=author_id,
                    name=author_name
                )
                save_changes(new_author)
                new_bookauthor = BookAuthor(
                    book = new_book,
                    author = new_author
                )
            else:
                new_bookauthor = BookAuthor(
                    book = new_book,
                    author = author
                )
            save_changes(new_bookauthor)

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
