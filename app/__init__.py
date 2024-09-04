#This code sets up a factory function, create_app, that initializes the Flask app and registers a blueprint for your routes.
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import and register blueprints (routes)
    from .routes import main
    app.register_blueprint(main)
    
    return app
