# all app routes in here with calling the function and storing the session data
from flask import redirect, render_template, request, session
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def users():
    users = User.get_all_users()
    return render_template('index.html', users = users)

@app.route('/add_user', methods = ["POST"])
def add_user():
    data = {
        "first_name": request.form["first_name"] ,
        "middle_name": request.form["middle_name"] ,
        "last_name": request.form["last_name"] ,
        "email": request.form["email"] ,
    }
    User.add_user(data)
    return redirect('/') 

@app.route('/delete_user/<int:num>')
def delete_user(num):
    data = {
        "id": num
    }
    User.delete_user(data)
    return redirect('/')

@app.route('/edit_user/<int:num>')
def edit_user(num):

    add_query = "WHERE id = " + f'{num}'
    user = User.get_all_users(add_query)
    print(user)
    for user_info in user:
        session['first_name'] = user_info['first_name']
        session['middle_name'] = user_info['middle_name']
        session['last_name'] = user_info['last_name']
        session['email'] = user_info['email']
    user_being_edited = session
    return render_template('edit.html', user=user_being_edited)

@app.route('/finish_edit', methods=['POST'])
def finish_edit():
    id = session['edit_id']
    data = {
        "first_name": request.form["first_name"] ,
        "middle_name": request.form["middle_name"] ,
        "last_name": request.form["last_name"] ,
        "email": request.form["email"] ,
    }
    User.edit_user(data, id)
    return redirect('/')