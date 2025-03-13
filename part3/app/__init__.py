from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app(config_class="config.DevelopmentConfig"):
    """Factory function to create the Flask application"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    #  Configure Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'

    db.init_app(app)
    bcrypt.init_app(app)
    migrate = Migrate(app, db)

    #  Import models after initialisation of db
    with app.app_context():
        from app.models.user import User

    #  Import and save Blueprints / Namespace
    from app.api.v1.users import api as users_ns
    from app.api.v1.amenities import api as amenities_ns
    from app.api.v1.places import api as places_ns
    from app.api.v1.reviews import api as reviews_ns

    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    return app
