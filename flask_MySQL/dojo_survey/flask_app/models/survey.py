from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.dojo_location = data['dojo_location']
        self.favorite_language = data['favorite_language']
        self.comments = data['comments']
        self.created_at_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_survey(cls,data):
        query = "INSERT INTO users_sruveyed (name, dojo_location, favorite_language, comments) VALUES (%(name)s, %(dojo_location)s, %(favorite_language)s, %(comments)s ) "
        connectToMySQL('dojo_survey').query_db(query, data)
        return

    @classmethod
    def result(cls):
        query = "SELECT * from users_sruveyed"

        result = connectToMySQL('dojo_survey').query_db(query)

        return result[-1]

    @staticmethod
    def validate_survey(data):
        is_valid = True
        if len(data['name']) < 1:
            flash("Name must be at least 1 character.")
            is_valid = False
        if len(data['comments']) < 10:
            flash("Comment must be at least 10 characters.")
            is_valid = False
        return is_valid