from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Character, Users
from application.forms import RegistrationForm

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/characters")
def characters():
    chars = Character.query.all()
    return render_template("characters.html", title="Fighters", chars=chars)

@app.route("/registration", methods=["GET","POST"])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(forename=form.forename.data, surname=form.surname.data, username=form.username.data, email=form.email.data, password=hash_pw)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("registration.html", title="Sign up here", form=form)
