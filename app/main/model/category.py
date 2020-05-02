from .. import db

class Category(db.Model):
    """ Category Model for storing category related details """
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<Category '{}'>".format(self.name)