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


class UserRatingDto:
    api = Namespace('rating', description='user related operations')
    user_rating = api.model('user rating', {
        'username': fields.String(required=True, description='user username'),
        'book_id': fields.String(description='book id'),
        'rating': fields.Float(description='rating')
    })
    books_with_ratings = api.model('books with ratings', {
        'book_id': fields.String(required=True, description='book ID', attribute='book_id'),
        'book_name': fields.String(required=True, description='book name', attribute='book.name'),
        'rating': fields.String(required=True, description='rating'),
    })
    users_with_ratings = api.model('users with ratings', {
        'username': fields.String(required=True, description='username'),
        'email': fields.String(required=True, description='user email address', attribute='user.email'),
        'rating': fields.String(required=True, description='rating'),
    })


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        # 'public_id': fields.String(description='user Identifier (optional)')
    })
    user_with_password = api.inherit('user with password', user, {
        'password': fields.String(required=True, description='user password')
    })
    users_with_rated_books = api.inherit('list of book with ratings', user, {
        'books': fields.List(fields.Nested(UserRatingDto.books_with_ratings))
    })


class BookDto:
    api = Namespace('book', description='book related operations')
    book = api.model('book', {
        'public_id': fields.String(description='book id'),
        'name': fields.String(description='book name'),
        'publisher': fields.String(description='publisher'),
        # 'rating': fields.Float(description='rating')
    })
    book_with_category = api.inherit('book with category', book, {
        'category_id': fields.String(attribute='category.public_id'),
        'category_name': fields.String(attribute='category.name')
    })
    book_with_authors = api.inherit('book with authors', book_with_category, {
        'authors': fields.List(fields.Nested(BookAuthorDto.author))
    })
    book_with_user_ratings = api.inherit('book with user ratings', book_with_authors, {
        'users': fields.List(fields.Nested(UserRatingDto.users_with_ratings))
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


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })