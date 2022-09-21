# stores our class and methods that use logic between our db and routes
from flask_app.config.mysqlconnection import connectToMySQL

class User():

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.middle_name = data['middle_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls, additional_query=""):
        query = f"SELECT * FROM users {additional_query}" 
        print(query)
        result = connectToMySQL('users').query_db(query)
        print(result)
        return result
    
    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, middle_name, email ) VALUES ( %(first_name)s , %(last_name)s , %(middle_name)s , %(email)s)" 
        return connectToMySQL('users').query_db(query, data)

    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL('users').query_db(query, data)
    
    @classmethod
    def edit_user(cls, data, id):
        query = "UPDATE users SET first_name = %(first_name)s, middle_name= %(middle_name)s, last_name = %(last_name)s,email = %(email)s WHERE id = " + f'{id}'
        return connectToMySQL("users").query_db(query, data)