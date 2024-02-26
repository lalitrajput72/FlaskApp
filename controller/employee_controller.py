from app import app
from model.employee import employee
from flask import request

emp = employee()


@app.route("/employee/get")
def get_employee():
    return emp.get_employee();


@app.route("/employee/add", methods=["POST"])
def addemployee():
    return emp.add_employee(request);


@app.route("/employee/update", methods=["PUT"])
def updateemployee():
    return emp.update_employee(request);


@app.route("/employee/delete/<id>", methods=["DELETE"])
def deleteemployee(id):
    return emp.delete_employee(id);