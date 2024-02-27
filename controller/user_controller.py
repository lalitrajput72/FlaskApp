from app import app
from model.user_model import user_model
from model.auth_model import auth_model
from flask import request

user_model = user_model()
auth_model = auth_model()

@app.route("/users/login", methods=["POST"])
def user_login_controller():
    return user_model.user_login(request)


@app.route("/users/get")
@auth_model.token_auth("/users/get")
def get_all_user():
    return user_model.get_all_users()
