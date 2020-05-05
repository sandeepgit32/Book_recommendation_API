from .. import db

class BookAuthor(db.Model):
    """ BookAuthor Model for storing book and author related details togather"""
    __tablename__ = "book_author"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.String(100), db.ForeignKey('book.public_id'), nullable=False)
    author_id = db.Column(db.String(100), db.ForeignKey('author.public_id'), nullable=False)
    book = db.relationship('Book', backref=db.backref('authors', lazy='dynamic'))
    author = db.relationship('Author', backref=db.backref('books', lazy='dynamic'))

    def __repr__(self):
        return "<BookAuthor '{}_{}'>".format(self.book_id, self.author_id)