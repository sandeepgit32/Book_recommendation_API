from app.main import db
from app.main.model.category import Category


def get_all_categories():
    return Category.query.all()


def get_a_category(public_id):
    return Category.query.filter_by(public_id=public_id).first()