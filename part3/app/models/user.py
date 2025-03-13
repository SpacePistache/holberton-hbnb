from app.models.basemodel import BaseModel
import re
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from app import bcrypt
from app import db

class User(BaseModel):
    """User model representing application users."""
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """Initialize a new user with required attributes."""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.places = []
        self.reviews = []


    @validates('email')
    def validate_email(self, key, email):
        """Validate email format before saving."""
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address format.")
        return email

    @validates('password')
    def validate_password(self, key, password):
        """Ensure password meets length requirement before saving."""
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        return password

    @hybrid_property
    def full_name(self):
        """Return the user's full name."""
        return f"{self.first_name} {self.last_name}"


    def add_place(self, place):
        """Associate a place with the user."""
        self.places.append(place)

    def add_review(self, review):
        """Associate a review with the user."""
        self.reviews.append(review)

    def delete_review(self, review):
        """Remove a review associated with the user."""
        self.reviews.remove(review)

    def to_dict(self):
        """Return a dictionary representation of the user including sensitive data."""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password
        }

    def to_safe_dict(self):
        """Return a dictionary without the password field"""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')


    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
