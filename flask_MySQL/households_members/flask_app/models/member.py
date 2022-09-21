from flask_app.config.mysqlconnection import connectToMySQL
# do all the query's
# this is going to conenct to our db and a dictionary will be passed into the 'data' argument
class Member():
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data["age"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.household_id = data ['household_id']

    @classmethod
    def get_all_members(cls):
        # established a local variable named query and storred a string which happens to be a sql query
        query = "SELECT * FROM members;"
        # results is a variable where we call the connectToMySQL function from mysqlconnection config file. we used . notation to call the querydb function and pased our query variable as an argument
        # results will get a list of dictionaries from whatevber .querydb returns from the connecttomysql function
        # every dictionary will be a row in our database
        # the keys of the dictionary will be the column and the values will be the row value of that column
        results = connectToMySQL('members_and_households').query_db(query)

        members=[]

        for row in results:
            members.append(cls(row)) 
            # this is for each column appending to the list and instatiating each one of the columns data into instances of Members
        return members
        # what we are doing is creating a list from the columns in mysql given to us from results variable and then creating a new list of Member classes stored in a list 

    @classmethod
    def add_member(cls, data):
        query = "INSERT INTO members (first_name, last_name, age,household_id) VALUES ( %(first_name)s, %(last_name)s,%(age)s,%(household_id)s );"
        return connectToMySQL("members_and_households").query_db(query, data)

    @classmethod
    def update_user(cls):
        query = "UPDATE members SET first_name=%(fn)s WHERE id %(id_num)s"
        data = {
            fn:
        }