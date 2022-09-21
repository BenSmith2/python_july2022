from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninja')
def ninjas_create():
    dojos = Dojo.show_dojos()
    return render_template('ninja_create.html', dojos = dojos)

@app.route('/add_ninja', methods = ["POST"])
def add_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo']
    }

    Ninja.add_ninja(data)
    return redirect("/ninja")

