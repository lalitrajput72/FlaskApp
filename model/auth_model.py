import json

import mysql.connector
from flask import make_response, request
import jwt
import re

class auth_model:
    def __init__(self, id =0, name="", password="", email="", role_id=""):
        self.id = id
        self.name = name
        self.password = password
        self.email = email
        self.role_id = role_id
        try:
            self.connection = mysql.connector.connect(host="localhost", user="root", password="Rajput@72", database="mysql")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(dictionary=True)
            print("Connection established successfully")
        except:
            print("Connection couldn't be established")
    def token_auth(self, endpoint):
        def inner1(func):
            def inner2(*args):
                authorization = request.headers.get("Authorization")
                if re.match("^Bearer *([^ ]+) *$", authorization, flags=0):
                    token = authorization.split(" ")[1]
                    try:
                        jwt_decoded = jwt.decode(token, "lalitrajput", algorithms = "HS256")
                    except jwt.ExpiredSignatureError:
                        return make_response("{message : Login timeout. Please login again}")
                    role_id = jwt_decoded['payload']['role_id']
                    self.cursor.execute(f"select roles from access_endpoint_view where endpoint='{endpoint}'")
                    roles = self.cursor.fetchall()
                    if len(roles) > 0:
                        allowed_roles = roles[0]['roles']
                        print(role_id)
                        if str(role_id) in allowed_roles:
                            return func(*args)
                        else:
                            return make_response("{Error : Role doesn't have permission to this endpoint}", 403)
                    else:
                        return make_response("{ERROR : Unknown endpoint}", 404)
                else:
                    return make_response("{ERROR : Invalid Token}")
            return inner2
        return inner1