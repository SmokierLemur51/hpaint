from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired



class ContactRequestForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    phone = StringField(label='Phone', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired()])
    message = TextAreaField(label='How can we help?') 
    submit = SubmitField(label="Submit")



class EstimateRequestForm(FlaskForm):
    # Job type is specified in the routes file. No need to pass a hidden field.
    name = StringField(label='Name', validators=[DataRequired()])
    phone = StringField(label='Phone', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired()])
    message = TextAreaField(label='How can we help?') 
    submit = SubmitField(label="Submit")



class TestimonialForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    phone = StringField(label='Phone', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired()])
    message = TextAreaField(label='How can we help?') 
    submit = SubmitField(label="Submit")
