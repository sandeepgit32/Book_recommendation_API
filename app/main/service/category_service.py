from app.main import db
from app.main.model.category import Category


def save_new_category(data):
    category = Category.query.filter_by(name=data['name']).first()
    if not category:
        new_category = Category(
            name=data['name'],
            public_id=data['category_id']
        )
        save_changes(new_category)
        response_object = {
            'status': 'success',
            'message': 'Successfully added.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'failed',
            'message': 'Category already exists.',
        }
        return response_object, 409


def get_all_categories():
    return Category.query.all()


def get_a_category(public_id):
    return Category.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
