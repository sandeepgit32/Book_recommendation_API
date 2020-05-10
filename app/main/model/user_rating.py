from .. import db

class UserRating(db.Model):
    """ UserRating Model for storing users' rating for books """
    __tablename__ = "user_rating"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), db.ForeignKey('user.username'), nullable=False)
    book_id = db.Column(db.String(100), db.ForeignKey('book.public_id'), nullable=False)
    book = db.relationship('Book', backref=db.backref('users', lazy='dynamic'))
    user = db.relationship('User', backref=db.backref('books', lazy='dynamic'))
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return "<UserRating '{}'>".format(self.name)