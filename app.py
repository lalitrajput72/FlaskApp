from flask import Flask
app = Flask(__name__)

@app.route("/welcome")
def welcome():
    print(app)
    return "Welcome to python Flask"


@app.route("/home")
def home():
    return "This is home"

from controller import *