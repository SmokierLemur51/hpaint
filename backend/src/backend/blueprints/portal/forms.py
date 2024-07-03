""" 
Required Forms:

Login
CreateUser
ChangePassword
CreateContactNote
CreateEstimateNote

"""
from flask_wtf import FlaskForm
from wtforms import (
    DecimalField, EmailField, HiddenField, SelectField, StringField, TextAreaField, SubmitField
)
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    pass


class CreateUser(FlaskForm):
    pass


class CreateEstimateForm(FlaskForm):
    contact_request_id = HiddenField()
    name = StringField(label='Name', validators=[DataRequired()])
    phone = StringField(label='Phone', validators=[DataRequired()])
    email = EmailField(label='Email')
    street = StringField(label='Street', validators=[DataRequired()])
    street2 = StringField(label='Street 2')
    city = StringField(label='City', validators=[DataRequired()])
    state = SelectField(label='State', validators=[DataRequired()])
    zip_code = StringField(label='Zip Code', validators=[DataRequired()])
    total = DecimalField('Total Price', places=2, validators=[DataRequired()])
    save = SubmitField('Save Changes')


class CreateContactNote(FlaskForm):
    pass


class CreateEstimateNote(FlaskForm):
    pass


class CreateEstimateProposal(FlaskForm):
    pass


class UpdateEstimateProposal(FlaskForm):
    pass
