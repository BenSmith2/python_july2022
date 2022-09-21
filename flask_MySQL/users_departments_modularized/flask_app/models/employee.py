from flask_app.config.mysqlconnection import connectToMySQL
# do all the query's
# this is going to conenct to our db and a dictionary will be passed into the 'data' argument
class Employee():
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.middle_name = data['middle_name']
        self.last_name = data['last_name']
        self.salary = data['salary']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.department_id = data['department_id']

    @classmethod
    def get_all_employees(cls):
        # established a local variable named query and storred a string which happens to be a sql query
        query = "SELECT * FROM employees;"
        # results is a variable where we call the connectToMySQL function from mysqlconnection config file. we used . notation to call the querydb function and pased our query variable as an argument
        # results will get a list of dictionaries from whatevber .querydb returns from the connecttomysql function
        # every dictionary will be a row in our database
        # the keys of the dictionary will be the column and the values will be the row value of that column
        results = connectToMySQL('july_2022_employees').query_db(query)

        for row in results:
            print(row)

        return results
