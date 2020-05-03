from .. import db

class Book(db.Model):
    """ Book Model for storing book related details """
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    publisher = db.Column(db.String(255), nullable=True)
    rating = db.Column(db.Float)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    category_id = db.Column(db.String(100), db.ForeignKey('category.public_id'))
    category = db.relationship('Category', backref=db.backref('books', lazy='dynamic'))

    def __repr__(self):
        return "<Book '{}'>".format(self.name)