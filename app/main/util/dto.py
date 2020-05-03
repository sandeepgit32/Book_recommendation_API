from flask_restplus import Namespace, fields

class BookAuthorDto:
    api = Namespace('bookauthor', description='book author related operations')
    bookauthor = api.model('bookauthor', {
        'book_id': fields.String(required=True, description='book ID', attribute='book_id'),
        'author_id': fields.String(required=True, description='author ID', attribute='author_id'),
    })
    book = api.model('bookauthor', {
        'book_id': fields.String(required=True, description='book ID', attribute='book_id'),
        'book_name': fields.String(required=True, description='book name', attribute='book.name'),
    })
    author = api.model('bookauthor', {
        'author_id': fields.String(required=True, description='author ID', attribute='author_id'),
        'author_name': fields.String(required=True, description='author name', attribute='author.name'),
    })

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier (optional)')
    })


class BookDto:
    api = Namespace('book', description='book related operations')
    book = api.model('book', {
        'public_id': fields.String(description='book id'),
        'name': fields.String(description='book name'),
        'publisher': fields.String(description='publisher'),
        'rating': fields.Float(description='rating')
    })
    book_with_category = api.inherit('book with category', book, {
        'category_id': fields.String(attribute='category.public_id'),
        'category_name': fields.String(attribute='category.name')
    })
    book_with_authors = api.inherit('book with authors', book_with_category, {
        'authors': fields.List(fields.Nested(BookAuthorDto.author))
    })


class AuthorDto:
    api = Namespace('author', description='author related operations')
    author = api.model('author', {
        'author_id': fields.String(required=True, description='author ID', attribute='public_id'),
        'name': fields.String(required=True, description='author name'),
    })
    author_with_books = api.inherit('author with books', author, {
        'books': fields.List(fields.Nested(BookAuthorDto.book))
    })


class CategoryDto:
    api = Namespace('category', description='category related operations')
    category = api.model('category', {
        'category_id': fields.String(required=True, description='category ID', attribute='public_id'),
        'name': fields.String(required=True, description='category name'),
    })
    category_with_books = api.inherit('category with books', category, {
        'books': fields.List(fields.Nested(BookDto.book))
    })