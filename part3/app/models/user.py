from .basemodel import BaseModel
import re
import bcrypt
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

from app import db
from .basemodel import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    _first_name = db.Column(db.String(50), nullable=False)
    _last_name = db.Column(db.String(50), nullable=False)
    _email = db.Column(db.String(120), nullable=False, unique=True)
    _password = db.Column(db.String(128), nullable=False)
    _is_admin = db.Column(db.Boolean, default=False)

    places = db.relationship('Place', backref='owner', lazy=True)
    reviews = db.relationship('Review', backref='reviewer', lazy=True)

    @hybrid_property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @hybrid_property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @hybrid_property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @hybrid_property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        self._is_admin = value

    def add_place(self, place):
        """Associate a place with the user."""
        if self.places is not None:
            self.places.append(place)
            db.session.commit()

    def add_review(self, review):
        """Add review."""
        if self.reviews is not None:
            self.reviews.append(review)
            db.session.commit()

    def delete_review(self, review):
        """Delete review."""
        if review in self.reviews:
            self.reviews.remove(review)
            db.session.commit()

    def to_dict(self):
        return {
            '_id': self.id,
            '_first_name': self.first_name,
            '_last_name': self.last_name,
            '_email': self.email,
            '_password': self.password
        }

    def to_safe_dict(self):
        """Return a dictionary without the password field"""
        return {
            '_id': self.id,
            '_first_name': self.first_name,
            '_last_name': self.last_name,
            '_email': self.email,
            '_is_admin': self.is_admin
        }
