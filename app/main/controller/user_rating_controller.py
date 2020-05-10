from flask import request
from flask_restplus import Resource

from ..util.dto import UserRatingDto
from ..service.user_rating_service import save_new_user_rating

api = UserRatingDto.api
_user_rating = UserRatingDto.user_rating


@api.route('/')
class UserBookRating(Resource):
    @api.response(201, 'User successfully rated the book.')
    @api.doc('create a new user')
    @api.expect(_user_rating, validate=True)
    def post(self):
        """Creates a new User Book rating"""
        data = request.json
        return save_new_user_rating(data=data)

