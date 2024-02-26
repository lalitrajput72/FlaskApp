import mysql.connector
from flask import make_response

class employee:
    def __init__(self, name="", email="", age=0):
        self.name = name
        self.email = email
        self.age = age
        # Connect with database
        try:
            self.connection = mysql.connector.connect(host="localhost", user="root", password="Rajput@72", database="mysql")
            self.connection.autocommit=True
            self.cursor = self.connection.cursor(dictionary=True)
            print("Connection established successfully")
        except:
            print("Some error while connecting the database")
    def get_employee(self):
        self.cursor.execute("select * from employee")
        result = self.cursor.fetchall()
        res = make_response(result, 200)
        res.headers["access-control-allow-orign"]="*"
        return res
    def add_employee(self, data):
        self.cursor.execute(f"Insert into employee(name, email, age) VALUES('{data.json['name']}', '{data.json['email']}', '{data.json['age']}')")
        return make_response("message : {'Employee added successfully'}", 201)
    def update_employee(self, data):
        self.cursor.execute(f"Update employee set name='{data.json['name']}', email='{data.json['email']}', age='{data.json['age']}' where id='{data.json['id']}'")
        if self.cursor.rowcount > 0:
            return make_response("message : {'Employee updated successfully'}", 201)
        else:
            return make_response("message : {'No update made'}", 202)
    def delete_employee(self, data):
        self.cursor.execute(f"delete from employee where id={data}")
        if self.cursor.rowcount > 0:
            return make_response("message : {'Employee deleted successfully'}", 200)
        else:
            return make_response("message : {'No delete made'}", 202)
    def patch_employee(self, data, id):
        query = ""
        for key in data.json:
            query = query + f"{key}='{data.json[key]}',"
        query = query[0 : len(query)-1]
        print(query)
        self.cursor.execute(f"update employee set {query} where id={id}")
        if self.cursor.rowcount:
            return make_response("message : {'Employee Patched successfully'}", 201)
        else:
            return "No update made"
    def get_paginated_data(self, limit, page):
        limit = int(limit)
        page = int(page)
        start = (page*limit)-limit
        self.cursor.execute(f"select * from employee LIMIT {start}, {limit}")
        result = self.cursor.fetchall()
        if self.cursor.rowcount:
            return make_response({"page_no":page, "limit":limit, "payload" : result}, 200)
        else:
            return make_response("message : {No data found}", 204)