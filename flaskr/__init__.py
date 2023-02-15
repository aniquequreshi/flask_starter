from flask import Flask

from config import Config
from flaskr.extensions import db

# This create_app receives the Config value
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    from flaskr.extensions import db

    # Import models before initializing db
    from flaskr.auth.models import User
    # from flaskr.site.models import Item, Note
    import flaskr.site.models
    
    db.init_app(app)    

    # Create tables if they don't exist
    # Tables will be created if needed, but not altered.
    with app.app_context():
        db.create_all()


    # Register blueprints here
    from flaskr.auth.routes import auth
    app.register_blueprint(auth)

    from flaskr.site.routes import site
    app.register_blueprint(site)

    return app