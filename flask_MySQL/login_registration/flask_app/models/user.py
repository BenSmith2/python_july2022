from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE, EMAIL_REGEX


class User:
    def __init__(self,data):
        self.id= data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email_address']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len (data['first_name']) < 2:
            flash("name must be longer than 1 characters")
            is_valid = False
        if len( data['last_name'] ) < 2:
            flash("name must be longer than 1 characters")
            is_valid = False
        if not EMAIL_REGEX.match(data['email_address']):
            flash("not a valid email address")
            is_valid = False
        if data['password'] != data['validate_password']:
            flash("Your password do not match")
            is_valid = False
        return is_valid

    @classmethod
    def validate_email(cls, data):
        query = "SELECT * FROM user WHERE email_address = %(email_address)s"

        result = connectToMySQL(DATABASE).query_db(query, data)

        if len(result) == 0:
            return True
        else:
            return False

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM user WHERE email_address = %(email_address)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
        

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO user (first_name, last_name, email_address, password)"
        query += "VALUES ( %(first_name)s, %(last_name)s, %(email_address)s, %(password)s )"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) == 0:
            return False
        return result[0]
        