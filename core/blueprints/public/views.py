from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for

from .forms import ContactRequestForm
from ...models.models import db
from ...models.models import ContactRequest

public = Blueprint('public', __name__, template_folder="templates/public", url_prefix="/")

@public.route("/")
def index():
    elements = {
        "title": "Higginbotham Paint",
    }
    return render_template("index.html", elements=elements)



@public.route("/our-story")
def our_story():
    elements = {
        "title": "Our Story",
    }
    return render_template("our_story.html", elements=elements)


@public.route("/services")
def services():
    elements = {
        "title": "Our Services",
    }
    return render_template("services.html", elements=elements)


@public.route("/residential")
def residential():
    elements = {
        "title": "Residential",
    }
    return render_template("residential.html", elements=elements)


@public.route("/commercial")
def commercial():
    elements = {
        "title": "Commercial",
    }
    return render_template("commercial.html", elements=elements)


@public.route("/exterior")
def exterior():
    elements = {
        "title": "Exterior",
    }
    return render_template("exterior.html", elements=elements)


@public.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactRequestForm()
    print(form.errors)
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
        return redirect(url_for("overlord.contact_requests"))
        # return redirect(url_for("public.index"))
    elements = {
        "title": "Contact Us",
    }
    return render_template("contact.html", elements=elements, form=form)



@public.route("/testimonials")
def testimonials():
    elements = {
        "title": "Testimonials",
    }
    return render_template("testimonials.html", elements=elements)
