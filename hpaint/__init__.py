from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from hpaint.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()



def create_app(config_class=Config):
	app = Flask(__name__, static_url_path="/static")
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	
	login_manager.login_view = "login"
	login_manager.login_message_category = "info"
	
	from hpaint.main.routes import main
	app.register_blueprint(main)

	return app



app = create_app()	

