import re
from flask_app import app
from flask import render_template, flash, redirect, request, session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/recipe')
def dashboard():
    # display sign up form, goes to '/sign_up_handle'
    if 'id' not in session:
        return redirect('/')
    data = {
        'id' : session['id']
    }
    user = User.get_user_by_id(data)
    print(user)
    list_recipes = Recipe.get_all_recipes_with_users()
    # display all recipes with their user
    
    return render_template('recipes.html', user = user, list_recipes = list_recipes)

@app.route('/recipe/<int:recipe_id>')
def display_single_recipe(recipe_id):
    if 'id' not in session:
        return redirect('/')
    data1= {
        'id': recipe_id
    }
    data2= {
        'id': session['id']
    }
    user = User.get_user_by_id(data2)
    current_recipe = Recipe.get_recipe_info(data1)
    print(current_recipe)
    return render_template("single_recipe.html",user=user, current_recipe = current_recipe )

@app.route('/recipe/edit/<int:recipe_id>')
def update_recipe(recipe_id):
    if 'id' not in session:
        return redirect('/')
    data = {
        'id': recipe_id
    }
    current_recipe = Recipe.get_recipe_info(data)
    return render_template("update_recipe.html", current_recipe = current_recipe )

@app.route('/recipe/update/validate/<int:recipe_id>', methods = ['POST'])
def validate_update_recipe(recipe_id):
    if Recipe.validate_new_recipe(request.form) == False:
        return redirect(f'/recipe/edit/{recipe_id}')
    data = {
        **request.form,
        "id" : recipe_id
    }
    
    Recipe.update_one(data)
    return redirect('/recipe')

@app.route('/recipe/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    if 'id' not in session:
        return redirect('/')
    data = {
        'id': recipe_id
    }
    Recipe.delete_recipe(data)
    return redirect("/recipe")


@app.route('/recipe/create')
def create_new_recipe_form():
    if 'id' not in session:
        return redirect('/')
    
    # display a form to create a new recipe
    return render_template('recipe_create_form.html')

@app.route('/recipe/validate', methods = ['POST'])
def validate_new_recipe():
    if Recipe.validate_new_recipe(request.form) == False:
        return redirect('/recipe/create')
    data = {
        **request.form,
        "user_id" : session["id"]
    }
    print("this is the print data")
    print(data)
    new_recipe = Recipe.create_new_recipe(data)
    session["new_recipe"] = new_recipe
    return redirect('/recipe')

@app.route('/recipe/logout')
def logout_of_recipes():
    session.clear()
    return redirect('/')