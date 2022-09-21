students = [
         {'first_name' :  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# students ={'first_name':  'Michael', 'last_name' : 'Jordan'}
        #  {'first_name' : 'John', 'last_name' : 'Rosales'},
        #  {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        #  {'first_name' : 'KB', 'last_name' : 'Tonel'}
# def iterateDictionary(key_name, students):
#     for i in range(len(students)):
#         print(students[i][key_name])

# def iterateDictionary(students):
#     # for dic in students:
#     for student in students.keys():
#         print(f"{student} {students[student]}")

def iterateDictionary(students):
    for student in range(len(students)):
        print(f"student: {students[student]['first_name']} {students[student]['last_name']}")

def iterateDictionary2(key, students):
        for student in range(len(students)):
            print(students[student][key])

iterateDictionary2("first_name",students)
iterateDictionary2("last_name",students)
# iterateDictionary2(["first_name","last_name"],students)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def iterateDojo(dojo):
    for key, val in dojo.items():
        print(key)
        for v in val:
             print(v)

iterateDojo(dojo)
# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon