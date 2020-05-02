from .. import db

class BookAuthor(db.Model):
    """ Book Model for storing book related details """
    __tablename__ = "book_author"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<BookAuthor '{}_{}'>".format(self.book_id, self.author_id)