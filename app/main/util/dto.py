from flask_restplus import Namespace, fields


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
    bookGet = api.model('book', {
        'public_id': fields.String(description='book id'),
        'name': fields.String(description='book name'),
        'publisher': fields.String(description='publisher'),
        'rating': fields.Float(description='rating'),
        'author_id': fields.String(attribute='author.public_id'),
        # 'author': fields.String(attribute='author.name')
    })
    bookPost = api.model('book', {
        'name': fields.String(required=True, description='book name'),
        'publisher': fields.String(description='publisher (optional)'),
        'rating': fields.Float(description='rating (optional)'),
        'author_id': fields.String(attribute='author.public_id'),
        # 'author': fields.String(attribute='author.name')
    })


class AuthorDto:
    api = Namespace('author', description='author related operations')
    author = api.model('author', {
        'author_id': fields.String(required=True, description='author ID', attribute='public_id'),
        'name': fields.String(required=True, description='author name'),
    })
    author_with_books = api.inherit('author with books', author, {
        'books': fields.List(fields.Nested(BookDto.bookGet))
    })