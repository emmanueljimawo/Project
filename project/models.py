from project import db, bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class FeatureRequest(db.Model):

    __tablename__ = "requests"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.Text, nullable=False)
    client = db.Column(db.String(12), nullable=False)
    client_priority = db.Column(db.Integer, nullable=False)
    target_date = db.Column(db.DateTime, nullable=False)
    product_area = db.Column(db.String(12), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.username'))

    def __init__(self, title, description, client,\
     client_priority, target_date, product_area, author):
        self.title = title
        self.description = description
        self.client = client
        self.client_priority = client_priority
        self.target_date = target_date
        self.product_area = product_area
        self.author_id = author

    def __repr__(self):
        return f"Feature('{self.title}','{self.client}','{self.client_priority}',\
        '{self.target_date}','{self.product_area}')"


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    features = relationship("FeatureRequest", backref="author", lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f"User('{self.username}')"
