from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired



class ContactRequestForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    phone = StringField(label='Phone', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired()])
    message = StringField(label='How can we help?') 
    submit = SubmitField(label="Submit")


class EstimateRequestForm(FlaskForm):
    pass



