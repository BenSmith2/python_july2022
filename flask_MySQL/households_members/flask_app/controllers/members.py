# controllers control app routes and where to redirect
from flask import redirect, render_template, request
# from flask_app.controllers import employees,
from flask_app import app
from flask_app.models.member import Member

@app.route('/')
def index():
    members=Member.get_all_members()

    return render_template("members.html", members = members)

@app.route('/save_member', methods = ['POST'])
def save_member():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "household_id": request.form["household_id"]
    }
    Member.add_member(data)
    return redirect('/')