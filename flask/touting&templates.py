# routing means mapping url to a python function when user visits URL flask runs the fucntion and return something like htmpl pages

from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Welcome to homepage"