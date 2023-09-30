from datetime import datetime
from higganbothampaint import db
from flask_login import UserMixin


# @login_manager.user_loader
# def load_user(user_id):
# 	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	phone_number = db.Column(db.String(10), unique=True, nullable=False) # Should I allow different accounts to be created with a same number
	password = db.Column(db.String(60), nullable=False)
	first_name = db.Column(db.String(60), nullable=True, default='John')
	last_name = db.Column(db.String(60), nullable=True, default='Doe')

	def __repr__(self):
		return f"User('{self.first_name}','{self.last_name}','{self.email}', '{self.phone_number}')"

# this is scheduled estimate, 
class ScheduleEstimate(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(60), nullable=False)
	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	street_address = db.Column(db.String(100), nullable=False)
	city_address = db.Column(db.String(100), nullable=False)
	state_address = db.Column(db.String(2), nullable=False)
	zip_code_address = db.Column(db.String(5), nullable=False)


	def __repr__(self):
		return f"'{self.date}', '{self.date}', '{self.customer_id}',\nAddress: '{self.street_address}', \n'{self.city_address}', '{self.state_address}', '{self.zip_code_address}'," 
