from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired



class RegisterUserForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = StringField(label='Password', validators=[DataRequired()])
    password_match = StringField(label='Re-Enter Password', validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = StringField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Submit")

