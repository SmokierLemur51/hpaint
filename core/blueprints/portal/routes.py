from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for

# from .forms import 
from ...models.models import db
from ...models.models import ContactRequest, EstimateRequest, StatusCode

portal = Blueprint('portal', __name__, template_folder="templates/portal", url_prefix="/portal")


""" Temporary rotues """
@portal.route("/tables/insert")
def insert_data():
    # from ...models.tests.populate import populate_stat_codes
    # populate_stat_codes(db)
    return redirect(url_for('portal.home'))


@portal.route("/")
def home():
    elements = {
        "title": "Higginbotham Paint",
        # "contact_requests": db.session.scalars(db.select(StatusCode)).all(),
    }
    return render_template("home.html", elements=elements)



@portal.route("/contact-requests")
def contact_requests():
    elements = {
        "title": "Higginbotham Paint",
    }
    return render_template("cont_requests.html", elements=elements)



