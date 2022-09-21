
from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/dojo')
def dojo_create_form():
    dojos = Dojo.show_dojos()
    return render_template('dojo_create.html', dojos = dojos)

@app.route('/add_dojo', methods = ["POST"])
def add_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.add_dojo(data)
    return redirect('/dojo')

@app.route("/dojo_info/<int:dojo_id>")
def dojo_info(dojo_id):
    print(dojo_id)
    data = {
        'id': dojo_id
    }

    
    dojo = Dojo.show_dojo_info(data)
    

    return render_template("dojo_info.html", dojo = dojo)

@app.route("/delete_dojo/<int:dojo_id>")
def delete_dojo(dojo_id):
    data = {
        "id":dojo_id
    }
    Dojo.delete_dojo(data)
    return redirect("/dojo")