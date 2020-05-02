from flask import request
from flask_restplus import Resource

from ..util.dto import BookDto
from ..service.book_service import save_new_book, get_all_books, get_a_book

api = BookDto.api
_bookGet = BookDto.bookGet
_bookPost = BookDto.bookPost


@api.route('/')
class BookList(Resource):
    @api.doc('get list of books')
    @api.marshal_list_with(_bookGet, envelope='data')
    def get(self):
        """List all books"""
        return get_all_books()

    @api.response(201, 'Book successfully added.')
    @api.doc('create a new book')
    @api.expect(_bookPost, validate=True)
    def post(self):
        """Creates a new Book """
        data = request.json
        return save_new_book(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Book identifier')
@api.response(404, 'Book not found.')
class Book(Resource):
    @api.doc('get a book')
    @api.marshal_with(_bookGet)
    def get(self, public_id):
        """get a book given its identifier"""
        book = get_a_book(public_id)
        if not book:
            api.abort(404)
        else:
            return book