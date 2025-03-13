from app.models.basemodel import BaseModel
from sqlalchemy.orm import validates
from app import db

class Place(BaseModel):
    """Place model representing a rental location."""
    __tablename__ = 'places'

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)


    def __init__(self, title, price, latitude, longitude, description=None):
        """Initialize a new place with required attributes."""
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude


    def to_dict(self):
        """Return a dictionary representation of the place."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

    def to_safe_dict(self):
        """Return a dictionary without sensitive data (if any)."""
        return self.to_dict()


    def to_dict_list(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }


    @validates('title')
    def validate_title(self, key, value):
        """Ensure title is a non-empty string."""
        if not value:
            raise ValueError("Title cannot be empty")
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if len(value) > 100:
            raise ValueError("Title must be 100 characters max")
        return value

    @validates('price')
    def validate_price(self, key, value):
        """Ensure price is a positive number."""
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a float")
        if value < 0:
            raise ValueError("Price must be positive.")
        return value

    @validates('latitude')
    def validate_latitude(self, key, value):
        """Ensure latitude is between -90 and 90."""
        if not isinstance(value, float):
            raise TypeError("Latitude must be a float")
        if not (-90 <= value <= 90):
            raise ValueError("Latitude must be between -90 and 90.")
        return value
    
    @validates('longitude')
    def validate_longitude(self, key, value):
        """Ensure longitude is between -180 and 180."""
        if not isinstance(value, float):
            raise TypeError("Longitude must be a float")
        if not (-180 <= value <= 180):
            raise ValueError("Longitude must be between -180 and 180.")
        return value
