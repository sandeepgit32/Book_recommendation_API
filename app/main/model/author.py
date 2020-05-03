from .. import db

class Author(db.Model):
    """ Author Model for storing author related details """
    __tablename__ = "author"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    public_id = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return "<Author '{}'>".format(self.name)