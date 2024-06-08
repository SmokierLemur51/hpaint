"""

"""
from dotenv import load_dotenv
from flask import Flask

# settings.py env loading
load_dotenv()



def create_app(**config_overrides) -> Flask:
    app = Flask(__name__, static_url_path="/static")
    
    # .env file config
    app.config.from_pyfile("settings.py")

    # config obj
    from .config import Config
    app.config.from_object(Config)

    # config overrides
    app.config.update(config_overrides)
    
    # blueprints
    from .blueprints.public.routes import public
    app.register_blueprint(public)

    # database
    from .models.models import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
