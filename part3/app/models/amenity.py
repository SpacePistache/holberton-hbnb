from .basemodel import BaseModel
from app import db

place_amenity = db.Table(
    'place_amenity',
    db.Column('place_id', db.Integer, db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenities.id'), primary_key=True)
)


class Amenity(BaseModel):

    __tablename__ = 'amenities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)


    places = db.relationship('Place', secondary=place_amenity, back_populates='amenities')

    
    def to_dict(self):
        return {
			'id': self.id,
			'name': self.name
		}



    @property
    def name(self):
       return self.__name


    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value:
            raise ValueError("Name cannot be empty")
        super().is_max_length('Name', value, 50)
        self.__name = value

    def update(self, data):
	    return super().update(data)
