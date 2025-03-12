from app.models.user import User
from app.persistence.repository import SQLAlchemyRepository

class UserRepository(SQLAlchemyRepository):
    """
    UserRepository extends the base SQLAlchemyRepository to provide
    specialized methods for interacting with the User model.
    """

    def __init__(self):
        """
        Initializes the UserRepository with the User model.
        This leverages all CRUD methods from the parent SQLAlchemyRepository.
        """
        super().__init__(User)

    def get_user_by_email(self, email):
        """
        Retrieves a user from the database by email.
        """
        return self.model.query.filter_by(email=email).first()
