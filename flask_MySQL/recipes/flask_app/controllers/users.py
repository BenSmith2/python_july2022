from flask_app import app
from flask import render_template, flash, redirect, request, session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def display_login_sign_up():
    # display sign up form, goes to '/sign_up_handle'
    return render_template('login_registration.html')


@app.route('/sign_up_handle', methods = ['POST'])
def sign_up_handle():
    # handles signup form and validates info from '/'
    if User.validate_registration(request.form) == False:
        return redirect('/')

    user_not_exists = User.validate_email(request.form)
    if user_not_exists == False:
        flash("This email is already in use")
        return redirect('/')

    password_hash = bcrypt.generate_password_hash(request.form['password'])
    print(password_hash)

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': password_hash
    }
    print(data)
    session['id'] = User.create_user(data)
    return redirect('/recipe')


@app.route('/login_validate', methods = ['POST'])
def login_validate():
    data = {
        "email": request.form["email"],
    }
    user = User.get_by_email(data)
    if not user:
        flash("User email does not  exist")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("password does not match email provided")
        return redirect('/')
    session['id'] = user.id
    return redirect('/recipe')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')