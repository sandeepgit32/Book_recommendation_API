from flask import request
from flask_restplus import Resource

from ..util.dto import BookAuthorDto
from ..service.book_author_service import get_all_bookauthors

api = BookAuthorDto.api
_bookauthor = BookAuthorDto.bookauthor


# @api.route('/')
# class AuthorList(Resource):
#     @api.response(201, 'Book_Author successfully added.')
#     @api.doc('create a new book_author')
#     @api.expect(_bookauthor, validate=True)
#     def post(self):
#         """Creates a new Book_Author"""
#         data = request.json
#         return save_new_bookauthor(data=data)


@api.route('/')
class CategoryList(Resource):
    # @api.doc('get list of bookauthors')
    @api.marshal_list_with(_bookauthor, envelope='data')
    def get(self):
        """List all bookauthors"""
        return get_all_bookauthors()
