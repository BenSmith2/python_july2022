from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from flask_app.models.user import User


class Recipe:
    def __init__(self,data):
        self.id= data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_30 = data['under_30']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


    @staticmethod
    def validate_new_recipe(data):
        is_valid = True
        print(data['name'])
        if data["name"] =="":
            flash("name must not be empty")
            is_valid = False
        if data["description"] == "":
            flash("description must not be empty")
            is_valid = False
        if data["instructions"] == "":
            flash("instructions must not be empty")
            is_valid = False
        if data["date_cooked"] == "":
            flash("date cooked must not be empty")
            is_valid = False
        if len(data["name"]) < 3:
            flash("name must be at least 3 characters long")
            is_valid = False
        if len(data["description"]) <3:
            flash("description must be at least 3 characters long")
            is_valid = False
        if len(data["instructions"]) <3:
            flash("instructions must be at least 3 characters long")
            is_valid = False
        return is_valid


    @classmethod
    def create_new_recipe(cls,data):
        query = "INSERT INTO recipes (name, description, under_30, instructions, date_cooked, user_id)"
        query += "VALUES ( %(name)s, %(description)s, %(under_30)s, %(instructions)s, %(date_cooked)s, %(user_id)s )"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_recipe_info(cls, data):
        query = "SELECT * FROM pies JOIN users ON pies.user_id = users.id AND pies.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result)>0:
            current_recipe = cls(result[0])
            user_data = {
                **result[0],
                "created_at": result[0]['users.created_at'],
                "updated_at": result[0]['users.updated_at'],
                "id": result[0]['users.id'],
            }
            current_recipe.user = User(user_data)
            return current_recipe
        else:
            return None

    @classmethod
    def get_all_recipes_with_users(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        
        list_recipes = []
        for row in results:
            current_recipe = cls(row) 
            user_data = {
                **row,
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at'],
                'id': row['users.id']
            }
            current_user = User( user_data )
            current_recipe.user = current_user
            list_recipes.append(current_recipe)
        return list_recipes

    @classmethod
    def update_one(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_cooked = %(date_cooked)s WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
