from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo():

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name ) Values ( %(name)s )" 
        return connectToMySQL('ninjas_dojos_crud').query_db(query, data)
    
    @classmethod
    def delete_dojo(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s"
        return connectToMySQL('ninjas_dojos_crud').query_db(query, data)

    @classmethod
    def show_dojos(cls):
        query = "SELECT * FROM dojos"
        return connectToMySQL('ninjas_dojos_crud').query_db(query)
    @classmethod
    def show_dojo_info(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        
        results = connectToMySQL('ninjas_dojos_crud').query_db(query, data)
        dojo = cls(results[0])
        for ninja in results:
            ninja_data = {
                'id': ninja['ninjas.id'],
                'first_name': ninja['first_name'],
                'last_name': ninja['last_name'],
                'age': ninja['age'],
                'dojo_id': ninja['dojo_id'],
                'created_at': ninja['ninjas.created_at'],
                'updated_at': ninja['ninjas.updated_at']
            }
            new_ninja = Ninja(ninja_data)
            dojo.ninjas.append(new_ninja)
        print(dojo.ninjas)
        return dojo