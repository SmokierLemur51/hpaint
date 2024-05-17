from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for

# from .forms import ContactRequestForm
from ...models import db
from ...models import ContactRequest

public = Blueprint('public', __name__, template_folder="templates/public", url_prefix="/")

@public.route("/")
def index():
    elements = {
        "title": "Higginbotham Paint",
    }
    return render_template("index.html", elements=elements)



@public.route("/about")
def about():
    elements = {
        "title": "About Us",
    }
    return render_template("about.html", elements=elements)

