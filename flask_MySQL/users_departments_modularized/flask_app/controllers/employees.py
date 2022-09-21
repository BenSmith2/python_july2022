from flask import render_template
# from flask_app.controllers import employees,
from flask_app import app
# controllers control app routes and where to redirect
from flask_app.models.employee import Employee

@app.route('/')
def index():

    employees = Employee.get_all_employees()

    return render_template('employees.html')