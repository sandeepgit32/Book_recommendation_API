from app.main import db
from app.main.model.author import Author


def save_new_author(data):
    author = Author.query.filter_by(name=data['name']).first()
    if not author:
        new_author = Author(
            name=data['name'],
            public_id=data['author_id']
        )
        save_changes(new_author)
        response_object = {
            'status': 'success',
            'message': 'Successfully added.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'failed',
            'message': 'Author already exists.',
        }
        return response_object, 409


def get_all_authors():
    return Author.query.all()


def get_an_author(public_id):
    return Author.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
