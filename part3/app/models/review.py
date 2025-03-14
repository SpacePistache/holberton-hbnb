from .basemodel import BaseModel
from .place import Place
from .user import User
from app import db

class Review(BaseModel):
     __tablename__ = 'reviews'

id = db.Column(db.Integer, primary_key=True)
comment = db.Column(db.String(255), nullable=False)
place_id = db.Column(db.Integer, db.ForeignKey('places.id'), nullable=False)
user = db.relationship('Review', backref='user', lazy=True)

place = db.relationship('Place', backref='reviews')


@property
def text(self):
		return self.__text
	
@text.setter
def text(self, value):
		if not value:
			raise ValueError("Text cannot be empty")
		if not isinstance(value, str):
			raise TypeError("Text must be a string")
		self.__text = value

@property
def rating(self):
		return self.__rating
	
@rating.setter
def rating(self, value):
		if not isinstance(value, int):
			raise TypeError("Rating must be an integer")
		super().is_between('Rating', value, 1, 6)
		self.__rating = value

@property
def place(self):
		return self.__place
	
@place.setter
def place(self, value):
		if not isinstance(value, Place):
			raise TypeError("Place must be a place instance")
		self.__place = value

@property
def user(self):
		return self.__user
	
@user.setter
def user(self, value):
		if not isinstance(value, User):
			raise TypeError("User must be a user instance")
		self.__user = value

def to_dict(self):
		return {
			'id': self.id,
			'text': self.text,
			'rating': self.rating,
			'place_id': self.place.id,
			'user_id': self.user.id
		}
