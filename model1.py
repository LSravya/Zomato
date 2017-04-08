from flask_sqlalchemy import SQLAlchemy
from app import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255))
    city = db.Column(db.String(255))
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, city, category, user_id):
        self.name = name
        self.city = city
        self.category = category
        self.user_id = user_id

    def to_dict(self):
        return {
        'id': self.id,
        'name': self.name,
        'city': self.city,
        'category': self.category,
        }

    def __repr__(self):
        return "Restaurant<%d> %s" % (self.id, self.name)
