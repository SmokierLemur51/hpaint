from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for

from .forms import CreateEstimateForm
from .queries import (
    get_contact_requests,
    get_estimates,
)
from ...models.models import db
from ...models.models import ContactRequest, EstimateRequest, StatusCode, Estimate
from ..public.forms import ContactRequestForm

portal = Blueprint('portal', __name__, template_folder="templates/portal", url_prefix="/portal")


""" Temporary rotues, development phase only. """
@portal.route("/tables/insert")
def insert_data():
    # from ...models.tests.populate import populate_estimate_requests
    # populate_estimate_requests(db)
    return redirect(url_for('portal.home'))


""" Main Routes """
# Landing page of the admin portal. General overview of what is happening.
@portal.route("/")
def home():
    elements = {
        "title": "Higginbotham Paint",
    }
    return render_template("home.html", elements=elements,
        contacts=get_contact_requests(contacted_filter=False))


# Contact requests, filtered by status. Default status is Neww
@portal.route("/contact-requests")
def contact_requests():
    elements = {
        "title": "Higginbotham Paint",
    }
    return render_template("contact_requests.html", elements=elements, 
        contacts=get_contact_requests(contacted_filter=False))


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

# This route is for converting a contact request into an estimate. 
@portal.route("/contact-requests/create-estimate/<int:id>", methods=['GET', 'POST'])
def convert_to_estimate(id):
    contact = db.get_or_404(ContactRequest, id)
    form = CreateEstimateForm()
    # pop 
    if request.method == 'GET':
        form.contact_request_id.data = contact.id
        form.name.data = contact.name
        form.phone.data = contact.phone
        form.email.data = contact.email

    if form.validate_on_submit():
        new_ = Estimate(
            contact_request_id=form.contact_request_id.data,
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            total=form.total.data,
            street=form.street.data,
            street2=form.street2.data,
            city=form.city.data,
            state=form.state.data,
            zip_code=form.zip_code.data,
        )
        with current_app.app_context():    
            db.session.add(new_)
            db.session.commit()
        flash("Estimate successfully created.")
        return redirect(url_for("public.index"))
    # end of form
    elements = {'title': 'Create Estimate'}
    return render_template('create_estimate_from_x.html', elements=elements, contact=contact, form=form)


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
    return render_template("estimates.html", elements=elements, estimates=get_estimates(db))


# Specific estimate/proposal. 
# You can:
#   - export to pdf
#   - send email 
#   - schedule 
@portal.route("/estimates/<int:id>")
def estimate(id):
    # estimate = db.get_or_404(Estimate, id)
    elements = {
        "title": f"{id}'s Estimates",
    }
    return render_template("estimate.html", elements=elements)


