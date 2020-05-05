from app.main import db
from app.main.model.book import Book
from app.main.model.author import Author
from app.main.model.book_author import BookAuthor


# def save_new_bookauthor(data):
#     bookauthor = BookAuthor.query.filter_by(book_id=data['book_id'])\
#                             .filter_by(author_id=data['author_id']).first()
#     if not bookauthor:
#         book_id = data['book_id']
#         book = Book.query.filter(Book.public_id == book_id).one()
#         author_id = data['author_id']
#         author = Author.query.filter(Author.public_id == author_id).one()
#         new_bookauthor = BookAuthor(
#             book = book,
#             author = author
#         )
#         save_changes(new_bookauthor)
#         response_object = {
#             'status': 'success',
#             'message': 'Successfully added.'
#         }
#         return response_object, 201
#     else:
#         response_object = {
#             'status': 'failed',
#             'message': 'Book-Author already exists.',
#         }
#         return response_object, 409


# def save_changes(data):
#     db.session.add(data)
#     db.session.commit()


def get_all_bookauthors():
    return BookAuthor.query.all()
