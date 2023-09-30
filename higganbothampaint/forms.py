from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password (8-20 Characters)', validators=[DataRequired(), Length(min=8, max=20)])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Schedule Estimate')

	def validate_email(self, email):
		pass
		# create models first 



class ScheduleEstimateForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	phone_number = StringField('Phone Number', validators=[DataRequired()])
	date = DateField('Select a date.', format='%d-%m-%y', validators=[DataRequired()])
	description = TextAreaField('Description of job', validators=[DataRequired()])
	submit = SubmitField('Schedule Estimate')



