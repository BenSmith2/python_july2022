from flask_app import app
from flask import render_template, flash, redirect, request, session
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def display_login_sign_up():
    # display sign up form, goes to '/sign_up_handle'
    return render_template('login_sign_up.html')


@app.route('/users/sign_up_handle', methods = ['POST'])
def sign_up_handle():
    # handles signup form and validates info from '/'
    if User.validate_registration(request.form) == False:
        return redirect('/')

    user_exists = User.validate_email(request.form)
    if user_exists == False:
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
    current_user = User.create_user(data)
    session['user_id'] = current_user
    return redirect('/dashboard')


@app.route('/users/login_validate', methods = ['POST'])
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
    session['user_id'] = user.id
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    # display sign up form, goes to '/sign_up_handle'
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    user = User.get_user_by_id(data)
    print(user)
    return render_template('user_dashboard.html', user = user)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')