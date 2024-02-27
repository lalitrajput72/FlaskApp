import mysql.connector
from flask import make_response
from datetime import datetime, timedelta
import jwt

class user_model:
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
    def get_all_users(self):
        self.cursor.execute("select * from users")
        result = self.cursor.fetchall()
        if self.cursor.rowcount > 0:
            return make_response(result, 200)
        else:
            return make_response("message : {NO DATA FOUND}", 201)
    def user_login(self, data):
        self.cursor.execute(f"select id, name, email, role_id from users where name='{data.json['name']}' and password='{data.json['password']}'")
        result = self.cursor.fetchall()
        exp_time = datetime.now() + timedelta(minutes=15)
        exp_epoch_time = int(exp_time.timestamp())
        payload = {
            "payload" : result[0],
            "exp": exp_epoch_time
        }
        token = jwt.encode(payload, "lalitrajput", algorithm = "HS256")
        return make_response({"token" : token}, 200)