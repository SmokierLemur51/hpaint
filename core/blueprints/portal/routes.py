from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for

# from .forms import 
from ...models.models import db
from ...models.models import ContactRequest, EstimateRequest, StatusCode

portal = Blueprint('portal', __name__, template_folder="templates/portal", url_prefix="/portal")


""" Temporary rotues """
@portal.route("/tables/insert")
def insert_data():
    # from ...models.tests.populate import populate_contact_requests
    # populate_contact_requests(db)
    return redirect(url_for('portal.home'))

""" Main Routes """
@portal.route("/")
def home():
    elements = {
        "title": "Higginbotham Paint",
        "contact_requests": db.session.scalars(db.select(ContactRequest)).all(),
    }
    return render_template("home.html", elements=elements)



@portal.route("/contact-requests")
def contact_requests():
    elements = {
        "title": "Higginbotham Paint",
    }
    return render_template("contact_requests.html", elements=elements)


@portal.route("/contact-requests/<int:id>")
def contact_request(id):
    contact = db.get_or_404(ContactRequest, id)
    elements = {
        "title": "{}".format(contact.name),
    }
    return render_template("contact_request_x.html", elements=elements, contact=contact)

# should add route for posting json data from frontend

@portal.route("/estimate-requests")
def estimate_requests():
    elements = {"title": "Estimate Requests"}
    return render_template("estimate_requests.html", elements=elements)


