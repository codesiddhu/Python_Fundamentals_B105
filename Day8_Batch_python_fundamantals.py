# Continous Of part of Dictionary  data type 
# implementation of forloop of a dictionary 
useraccounts ={"username":"sreedhar","firstname":"sreedhar","lastname":"royals","dob":"30/05/2002","pwd":"1144"}
for k,v in useraccounts.items():
    print(f"key {k}", "==>",end="")
    print(f"values:{v} \n ")


# i wan to get only key from the useraccounts 

for key in useraccounts.keys():
    print(f"only keys : {key}")

# i want to get the only values from the dictionary

for values in useraccounts.values():
    print(f"values {values}")