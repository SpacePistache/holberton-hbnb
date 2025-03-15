from .basemodel import BaseModel
from .place import Place
from .user import User
from app import db
import uuid

class Review(BaseModel):
    __tablename__ = 'reviews'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    comment = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)


    user = db.relationship('User', backref='reviews')
    place = db.relationship('Place', backref='place_reviews')


    def to_dict(self):
        return {
			'id': self.id,
			'text': self.text,
			'rating': self.rating,
			'place_id': self.place.id,
			'user_id': self.user.id
		}
