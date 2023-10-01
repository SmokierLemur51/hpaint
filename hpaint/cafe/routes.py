from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from hpaint.forms import RegisterForm, ScheduleEstimateForm
from hpaint.models import ScheduleEstimate

cafe = Blueprint("cafe", __name__)

@cafe.route("/cafe")
def cafe_login():

	return render_template("auth/login.html")



@cafe.route("/cafe/home")
def cafe_home():

	return render_template("auth/cafe/cafe_home.html")