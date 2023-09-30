from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from higganbothampaint.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(config_class=Config):
	app = Flask(__name__, static_url_path="/static")
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	
	from higganbothampaint.main.routes import main

	app.register_blueprint(main)
	return app

app = create_app()	

# from higganbothampaint import routes