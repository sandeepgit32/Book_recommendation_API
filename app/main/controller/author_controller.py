from flask import request
from flask_restplus import Resource

from ..util.dto import AuthorDto
from ..service.author_service import save_new_author, get_all_authors, get_an_author

api = AuthorDto.api
_author = AuthorDto.author
_authorWithBooks = AuthorDto.author_with_books


@api.route('/')
class AuthorList(Resource):
    @api.doc('get list of authors')
    @api.marshal_list_with(_author, envelope='data')
    def get(self):
        """List all authors"""
        return get_all_authors()

    @api.response(201, 'Author successfully added.')
    @api.doc('create a new author')
    @api.expect(_author, validate=True)
    def post(self):
        """Creates a new Author """
        data = request.json
        return save_new_author(data=data)


@api.route('/<id>')
@api.param('id', 'The Author identifier')
@api.response(404, 'Author not found.')
class Author(Resource):
    @api.doc('get a author')
    @api.marshal_with(_authorWithBooks)
    def get(self, id):
        """get a author given its identifier"""
        author = get_an_author(id)
        if not author:
            api.abort(404)
        else:
            return author