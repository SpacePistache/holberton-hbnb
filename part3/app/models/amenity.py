from .basemodel import BaseModel
from app import db

class Amenity(BaseModel):
    """Amenity model representing facilities available at a place."""
    __tablename__ = 'amenities'

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(50), nullable=False, unique=True)


    def __init__(self, name):
        """Initialize a new amenity with required attributes."""
        super().__init__()
        self.name = name


    def to_dict(self):
        """Return a dictionary representation of the amenity."""
        return {
            'id': self.id,
            'name': self.name
        }


    def to_safe_dict(self):
        """Return a dictionary without sensitive data (if any)."""
        return self.to_dict()
