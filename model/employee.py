import mysql.connector
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
        return result
    def add_employee(self, data):
        self.cursor.execute(f"Insert into employee(name, email, age) VALUES('{data.json['name']}', '{data.json['email']}', '{data.json['age']}')")
        return "Employee added successfully"
    def update_employee(self, data):
        self.cursor.execute(f"Update employee set name='{data.json['name']}', email='{data.json['email']}', age='{data.json['age']}' where id='{data.json['id']}'")
        if self.cursor.rowcount > 0:
            return "Employee updated successfully"
        else:
            return "No update made"
    def delete_employee(self, data):
        self.cursor.execute(f"delete from employee where id={data}")
        if self.cursor.rowcount > 0:
            return "Employee deleted successfully"
        else:
            return "No deletion made"