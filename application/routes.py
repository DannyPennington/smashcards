from flask import render_template
from application import app
from application.models import Character

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
