from flask import request
from flask_restplus import Resource

from ..util.dto import CategoryDto
from ..service.category_service import get_all_categories, get_a_category

api = CategoryDto.api
_category = CategoryDto.category
_categoryWithBooks = CategoryDto.category_with_books


@api.route('/')
class CategoryList(Resource):
    @api.doc('get list of categories')
    @api.marshal_list_with(_category, envelope='data')
    def get(self):
        """List all categories"""
        return get_all_categories()


@api.route('/<public_id>')
@api.param('public_id', 'The Category identifier')
@api.response(404, 'Category not found.')
class Category(Resource):
    @api.doc('get a category')
    @api.marshal_with(_categoryWithBooks)
    def get(self, public_id):
        """get a category given its identifier"""
        category = get_a_category(public_id)
        if not category:
            api.abort(404)
        else:
            return category