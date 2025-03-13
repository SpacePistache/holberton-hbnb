from app.persistence.repository import SQLAlchemyRepository
from app.persistence.user_repository import UserRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app import db

class HBnBFacade:
    """Facade class to manage operations on users, places, amenities, and reviews."""
    
    def __init__(self):
        """Initialize repositories for managing different entities."""
        self.session = db.session
        self.user_repository = UserRepository()
        self.place_repository = SQLAlchemyRepository(Place)
        self.review_repository = SQLAlchemyRepository(Review)
        self.amenity_repository = SQLAlchemyRepository(Amenity)

    # USER
    def create_user(self, user_data):
        """Create a new user with hashed password."""
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.session.add(user)
        self.session.commit()
        return user

    def get_users(self):
        """Retrieve all users."""
        return self.user_repository.get_all()

    def get_user(self, user_id):
        """Retrieve a user by ID."""
        return self.user_repository.get(user_id)

    def get_user_by_email(self, email):
        """Retrieve a user by email."""
        return self.user_repository.get_user_by_email(email)

    def update_user(self, user_id, user_data):
        """Update user information."""
        self.user_repository.update(user_id, user_data)

    # AMENITY
    def create_amenity(self, amenity_data):
        """Create a new amenity."""
        amenity = Amenity(**amenity_data)
        self.amenity_repository.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Retrieve an amenity by ID."""
        return self.amenity_repository.get(amenity_id)

    def get_all_amenities(self):
        """Retrieve all amenities."""
        return self.amenity_repository.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """Update an amenity's information."""
        self.amenity_repository.update(amenity_id, amenity_data)

    # PLACE
    def create_place(self, place_data):
        """Create a new place and associate it with an owner and amenities."""
        user = self.user_repository.get(place_data['owner_id'])
        if not user:
            raise KeyError('Invalid input data: owner not found')
        del place_data['owner_id']
        place_data['owner'] = user
        amenities = place_data.pop('amenities', [])

        place = Place(**place_data)
        self.place_repository.add(place)
        user.add_place(place)
        
        for amenity_data in amenities:
            amenity = self.get_amenity(amenity_data['id'])
            if amenity:
                place.add_amenity(amenity)
        
        return place

    def get_place(self, place_id):
        """Retrieve a place by ID."""
        return self.place_repository.get(place_id)

    def get_all_places(self):
        """Retrieve all places."""
        return self.place_repository.get_all()

    def update_place(self, place_id, place_data):
        """Update place information."""
        self.place_repository.update(place_id, place_data)

    # REVIEWS
    def create_review(self, review_data):
        """Create a new review and associate it with a user and a place."""
        user = self.user_repository.get(review_data['user_id'])
        if not user:
            raise KeyError('Invalid input data: user not found')
        del review_data['user_id']
        review_data['user'] = user
        
        place = self.place_repository.get(review_data['place_id'])
        if not place:
            raise KeyError('Invalid input data: place not found')
        del review_data['place_id']
        review_data['place'] = place

        review = Review(**review_data)
        self.review_repository.add(review)
        user.add_review(review)
        place.add_review(review)
        return review

    def get_review(self, review_id):
        """Retrieve a review by ID."""
        return self.review_repository.get(review_id)

    def get_all_reviews(self):
        """Retrieve all reviews."""
        return self.review_repository.get_all()

    def get_reviews_by_place(self, place_id):
        """Retrieve all reviews associated with a specific place."""
        place = self.place_repository.get(place_id)
        if not place:
            raise KeyError('Place not found')
        return place.reviews

    def update_review(self, review_id, review_data):
        """Update a review's content."""
        self.review_repository.update(review_id, review_data)

    def delete_review(self, review_id):
        """Delete a review and remove its associations with user and place."""
        review = self.review_repository.get(review_id)
        if not review:
            raise KeyError('Review not found')
        
        user = self.user_repository.get(review.user.id)
        place = self.place_repository.get(review.place.id)

        user.delete_review(review)
        place.delete_review(review)
        self.review_repository.delete(review_id)
