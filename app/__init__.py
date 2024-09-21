from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config

mongo = PyMongo()

def create_app():
    # Initialize Flask application
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize MongoDB connection
    mongo.init_app(app)

    # Register blueprints
    from app.routes import user_routes
    app.register_blueprint(user_routes.bp)

    return app