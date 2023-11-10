from flask import Blueprint, render_template


main = Blueprint('main', __name__, template_folder="templates")

# main customer pages 

@main.route("/")
def index():
    context = {'title': "StarterProject", 'company_name': 'Higginbotham Paint'}
    return render_template('index.html', context=context) 


@main.route("/services")
def services():
    context = {'title': "StarterProject", 'company_name': 'Higginbotham Paint'}
    return render_template('services.html', context=context)


@main.route("/about")
def about():
    context = {'title': "StarterProject", 'company_name': 'Higginbotham Paint'}
    return render_template('about.html', context=context)


# form processing