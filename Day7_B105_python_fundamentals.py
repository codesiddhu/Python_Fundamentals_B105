# tuple 
'''
 tuple
'''

student = ("siddhu","royals","prakash","rani","dhanusj")
print(student)
print(type(student))
print(student[1])

for a in student:
    print(a)

# introduction to Dictionary
'''
dictionary is nothing but a combination of key pair value
it is classfied as a mutable datatypes
it is represented by the {}
'''

# i want to create allien game:

allien = {'color':'green',"points":5,"level":"stage1"}
print(allien)

# i want to know the color of the allien 
print(allien["color"])

# facebook

facebook ={"username":"sreedhar","firstname":"sreedhar","lastname":"royals","dob":"30/05/2002","pwd":"1144"}
print(facebook)
print(type(facebook))

# i want to  access  to the username
print(facebook["username"])

# i want to delete to the last name
del facebook['lastname']
print(facebook)

# i want modify/chanage the password 
facebook['pwd'] = 3060
print(facebook) 