# project/server/models.py


import datetime

from flask import current_app

from project.server import db, bcrypt
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash
import uuid
import time

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.String(), primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)


    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.registered_on = datetime.datetime.utcnow()
        self.date_posted = datetime.datetime.utcfromtimestamp(time.time())
        self.id = str(uuid.uuid4())

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    @validates('password')
    def _validate_password(self, key, password):
        crypted = generate_password_hash(password, 'sha1', 8)
        return crypted

    def __repr__(self):
        return "<User {0}>".format(self.email)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, nullable=True)
    author_id = db.Column(db.String(), db.ForeignKey('users.id'))
    author = db.relationship("User", backref='posts')
    visible = db.Column(db.Boolean(), default=True)
    posted_by_ip_address = db.Column(db.String(), nullable=True)
    posted_by_user_agent = db.Column(db.String(), nullable=True)

    def __init__(self, **kwargs):
        super(Post, self).__init__(**kwargs)
        self.date_posted = datetime.datetime.utcfromtimestamp(time.time())
        self.id = str(uuid.uuid4())

    def __repr__(self):
        return '<Post {0}>'.format(self.id)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}