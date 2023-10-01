import os 


class Config:

	# SECRET_KEY = os.environ.get('SECRET_KEY')
	# SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
	
	SECRET_KEY = '7f352cbc6749f0e00e91da31e5399e818faacc873fe104a94b351d1d8c541b2c'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
	MAIL_SERVER = ''
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')