from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for

# from .forms import 
from ...models.models import db
from ...models.models import ContactRequest, EstimateRequest, StatusCode


portal = Blueprint('portal', __name__, template_folder="templates/portal", url_prefix="/portal")


""" Temporary rotues, development phase only. """
@portal.route("/tables/insert")
def insert_data():
    # from ...models.tests.populate import populate_estimate_requests
    # populate_estimate_requests(db)
    return redirect(url_for('portal.home'))


""" Main Routes """
@portal.route("/")
def home():
    elements = {
        "title": "Higginbotham Paint",
        "contact_requests": db.session.scalars(db.select(ContactRequest)).all(),
    }
    return render_template("home.html", elements=elements)


# Contact requests, filtered by status. Default status is Neww
@portal.route("/contact-requests")
def contact_requests():
    elements = {
        "title": "Higginbotham Paint",
    }
    return render_template("contact_requests.html", elements=elements)


# Specific contact request, given its own page to help with focus when calling. 
# You can also
#   - Create a note on the contact request. 
#   - Convert into an estimate
@portal.route("/contact-requests/<int:id>")
def contact_request(id):
    request_ = db.get_or_404(request_Request, id)
    # NewNote
    elements = {
        "title": f"{request_.name}'s Request",
    }
    return render_template("contact_request_x.html", elements=elements, request_=request_)


# All estimate requests, paginated and sorted by newest that are of New status. 
@portal.route("/estimate-requests")
def estimate_requests():
    elements = {"title": "Estimate Requests"}
    return render_template("estimate_requests.html", elements=elements)


# Specific Customer/Lead estimate request page.
# You can:
#   - create notes for it
#   - convert to proposal/estimate
#   - generate and email/text pdf
@portal.route("/estimate-requests/<int:id>")
def estimate_request(id):
    request_ = db.get_or_404(EstimateRequest, id)
    elements = {
        "title": f"{request_.name}'s Request"
    }
    return render_template("estimate_request_x.html", elements=elements, request_=request_)


# Admin created estimates/proposals. Sorted by status.
@portal.route("/estimates")
def estimates():
    # create_estimate = CreateEstimateForm()
    # update_estiamte = UpdateEstimateForm()
    elements = {
        "title": "Estimates",
    }
    return render_template("estimates.html", elements=elements)


@portal.route("/estimates/<int:id>")
def estimate(id):
    # estimate = db.get_or_404(Estimate, id)
    elements = {
        "title": f"{id}'s Estimates",
    }
    return render_template("estimate.html", elements=elements)
