# models.py
# pylint: disable=missing-docstring
# pylint: disable=import-error

from wsgi import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __repr__(self):
        return '<id {}>'.format(self.id)