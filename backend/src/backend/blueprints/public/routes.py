from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for

from .forms import ContactRequestForm, EstimateRequestForm
from ...models.models import db
from ...models.models import ContactRequest, EstimateRequest


public = Blueprint('public', __name__, template_folder="templates/public", url_prefix="/")


@public.route("/", methods=['GET', 'POST'])
def index():
    form = ContactRequestForm()
    if form.validate_on_submit():
        new_ = ContactRequest(
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            message=form.message.data,
        )
        with current_app.app_context():    
            db.session.add(new_)
            db.session.commit()
        flash("Thank you! We will be in touch.")
        return redirect(url_for("public.index"))
    elements = {
        "title": "Higginbotham Paint",
    }
    return render_template("index.html", elements=elements, form=form)



@public.route("/our-story")
def about():
    elements = {
        "title": "Our Story",
    }
    return render_template("about.html", elements=elements)


@public.route("/services")
def services():
    form = EstimateRequestForm()
    if form.validate_on_submit():
        new_ = EstimateRequest(
            job_type="general",
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            message=form.message.data,
        )
        with current_app.app_context():    
            db.session.add(new_)
            db.session.commit()
        flash("Thank you! We will be in touch.")
        return redirect(url_for("public.index"))
    elements = {
        "title": "Our Services",
    }
    return render_template("services.html", elements=elements)


@public.route("/services/residential")
def residential():
    form = EstimateRequestForm()
    if form.validate_on_submit():
        new_ = EstimateRequest(
            job_type="residential",
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            message=form.message.data,
        )
        with current_app.app_context():    
            db.session.add(new_)
            db.session.commit()
        flash("Thank you! We will be in touch.")
        return redirect(url_for("public.index"))
    elements = {
        "title": "Residential",
    }
    return render_template("residential.html", elements=elements)


@public.route("/services/commercial")
def commercial():
    form = EstimateRequestForm()
    if form.validate_on_submit():
        new_ = EstimateRequest(
            job_type="commercial",
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            message=form.message.data,
        )
        with current_app.app_context():    
            db.session.add(new_)
            db.session.commit()
        flash("Thank you! We will be in touch.")
        return redirect(url_for("public.index"))
    elements = {
        "title": "Commercial",
    }
    return render_template("commercial.html", elements=elements)


@public.route("/services/exterior")
def exterior():
    form = EstimateRequestForm()
    if form.validate_on_submit():
        new_ = EstimateRequest(
            job_type="exterior",
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            message=form.message.data,
        )
        with current_app.app_context():    
            db.session.add(new_)
            db.session.commit()
        flash("Thank you! We will be in touch.")
        return redirect(url_for("public.index"))
    elements = {
        "title": "Exterior",
    }
    return render_template("exterior.html", elements=elements)



@public.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactRequestForm()
    if form.validate_on_submit():
        new_ = ContactRequest(
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            message=form.message.data,
        )
        with current_app.app_context():    
            db.session.add(new_)
            db.session.commit()
        flash("Thank you! We will be in touch.")
        return redirect(url_for("public.index"))
    elements = {
        "title": "Contact Us",
    }
    return render_template("contact.html", elements=elements, form=form)


@public.route("/testimonials")
def testimonials():
    # new testimonial form ... 
    elements = {
        "title": "Testimonials",
    }
    return render_template("testimonials.html", elements=elements)
