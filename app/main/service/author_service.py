from app.main import db
from app.main.model.author import Author


def get_all_authors():
    return Author.query.all()


def get_an_author(public_id):
    return Author.query.filter_by(public_id=public_id).first()
