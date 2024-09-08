import os
from flask import (
    Blueprint,
    current_app,
    redirect,
    render_template,
    url_for,
)
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)

from . import forms, queries
from ...extensions import fbcrypt
from ...models.models import db, User
from ...models.queries import load_role


users = Blueprint('users', __name__, template_folder="templates/users")


@users.route('/login', methods=['GET', 'POST'])
def login():
    # redirect to the portal homepage if authenticated
    if current_user.is_authenticated:
        return redirect(url_for('portal.home'))
    # login page information
    elements = {
        "title": "Login",    
    }
    f = forms.LoginForm()
    if f.validate_on_submit():
        u = queries.get_user(db, f.username.data)
        print(f"User Pass: {u.password}, Given: {f.password.data}")
        if u and fbcrypt.check_password_hash(u.password, f.password.data):
            login_user(u)
            return redirect('/redirect-user')
        else:
            flash('Invalid credentials.', 'danger')
    return render_template("login.html", elements=elements, form=f)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('public.index'))


# Register administrative user
@users.route("/register-user-administration", methods=["GET", "POST"])
def register_user():
    elements = {
        "title": "Register User",    
    }
    f = forms.RegisterUserf()
    if f.validate_on_submit():
        if f.password.data == f.password_match.data:
            u = User(
                role_id=load_role(db, "admin").id,
                username=f.username.data,
                password=fbcrypt.generate_password_hash(f.password.data),
            )
            try:
                db.session.add(u)
                db.session.commit()
                return redirect(url_for("users.login"))
            except Exception as e:
                db.session.rollback()
                print(e)
                flash("Error, please try again.")
                return render_template("register_user.html", elements=elements, form=f)
        else:
            flash("Passwords must match.")
            return render_template("register_user.html", elements=elements, form=f)
    return render_template("register_user.html", elements=elements, form=f)
