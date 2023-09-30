from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from higganbothampaint.forms import RegisterForm, ScheduleEstimateForm
from higganbothampaint.models import ScheduleEstimate

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home", methods=['GET', 'POST'])
def home():
	form = ScheduleEstimateForm()
	return render_template("main/home.html", form=form) # argument for jinja variables


@main.route("/about", methods=['GET', 'POST'])
def about():
	form = ScheduleEstimateForm()
	if form.validate_on_submit():
		flash('Scheduling successful! Please check your email for additional information.', 'success')
		# work on models to make this possible
	else:
		flash('Scheduling unsuccessful. Please check required fields.', 'danger')
	# I think reviews should go here
	return render_template("main/about.html", title='About', form=form)



@main.route("/login", methods=['GET', 'POST'])
def services():
	form = ScheduleEstimateForm()
	return render_template("main/services.html", title='Services', form=form)


# - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - Form Processing - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - -

@main.route("/process-estimate", methods=['POST'])
def process_estimate_form():
	# try:
	# 	data = request.get_json()

	# 	new_estimate = 
	# except Exception as e:
	pass

# - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - ReviewLoading - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - -
 
@main.route("/reviews")
def reviews():
	''' here we implant the api to google reviews, could not find an api in the google console cloud
	    maybe make a database of the reviews? Could run it on the backend and have
		a function filter out the bad ones and render it to the about template...
	''' 
	# https://embedsocial.com/blog/embed-google-reviews/
	return render_template("reviews.html")

