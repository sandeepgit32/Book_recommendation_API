# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.book_controller import api as book_ns
from .main.controller.author_controller import api as author_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='BOOK RECOMMENDATION API',
          version='1.0',
          description='A rest api for book recommendation using flask restplus'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(book_ns, path='/book')
api.add_namespace(author_ns, path='/author')