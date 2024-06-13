""" 
Required Forms:

Login
CreateUser
ChangePassword
CreateContactNote
CreateEstimateNote

"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    pass


class CreateUser(FlaskForm):
    pass


class CreateContactNote(FlaskForm):
    pass


class CreateEstimateNote(FlaskForm):
    pass


class CreateEstimateProposal(FlaskForm):
    pass


class UpdateEstimateProposal(FlaskForm):
    pass
