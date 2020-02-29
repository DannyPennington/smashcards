from flask import render_template
from application import app
from application.models import Character

@app.route("/")
@app.route("/home")
def home():
    chars = Character.query.all()
    return render_template("home.html", title="Home", chars=chars)

@app.route("/about")
def about():
    return render_template("about.html", title="About")
