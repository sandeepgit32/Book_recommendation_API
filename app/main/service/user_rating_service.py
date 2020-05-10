from app.main import db
from app.main.model.user_rating import UserRating


def save_new_user_rating(data):
    user_rating = UserRating.query.filter_by(username=data['username'])\
                        .filter_by(book_id=data['book_id']).first()
    if not user_rating:
        new_user_rating = UserRating(
            username=data['username'],
            book_id=data['book_id'],
            rating=data['rating']
        )
        save_changes(new_user_rating)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'You already rated the book.',
        }
        return response_object, 409


# def get_all_book_ratings_for_an_user(username):
#     return UserRating.query.all.filter_by(username=username)


# def get_all_user_ratings_for_a_book(book_id):
#     return UserRating.query.all.filter_by(book_id=book_id)


def save_changes(data):
    db.session.add(data)
    db.session.commit()

