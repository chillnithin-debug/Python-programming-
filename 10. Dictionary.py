# Dictionary:
# Dictionary is a in-built collection datatype, which is used to store multiple values in a single varaible.
# Dictionary stores the data in the form of key-values pairs.
# Each key is unique and works as an index to access its corresponding value.
# Keys are immutable(can't be changed once created), while values can be anything(mutable).
# Dictionary are: Ordered(From python 3.7+ version), Mutable, Do not allows the duplicate keys
# Syntax
# my_dict = {
#     "key1":"value1",
#     "key2":"value2",
#     "key3":"value3",
#     "key4":"value4"
# }
# print(my_dict)
# Characteristics of Dictionary:
# key-value pairs: 
# Every entry of Dictionary's element is a pair: keys and values. 
# { "name":"nandhan"}
# Unique Keys: 
# example: 
# A = {"n":"Nandhan","n":"Anurag"}
# print(A) # {"n":"Anurag"}
# Keys must be immutable: 
# keys can be(valid keys): integer,float,string
# My_dict = {
#     1:"value1",
#     10.2:"value2",
#     "key3":"value3",
#     "key4":"value4"
# }

# Creating Dictionary:
# Normal Dictionary:
# BioData = {
#     "Name":"Nandhan",
#     "RollNo":66,
#     "Branch":"CSC",
#     "Place":"Kamareddy"
# }
# print(BioData)
# Dictionary using Constructor: 
# BioData1 = dict( Name="Nandhan",Roll_No=66,Branch="CSC")
# print(BioData1)
# Empty Dictionary:
# E_D = {}

# Accessing the Dictionary:
# -> To access an element we use key names inside the square brackets [] or we can use get() method.

# BioData = {
#     "Name":"Nandhan",
#     "RollNo":66,
#     "Branch":"CSC",
#     "Place":"Kamareddy"
# } 
# square brackets []
# print(BioData["Name"]) # Nandhan
# print(BioData["RollNo"]) # 66
# print(BioData["Branch"]) # CSC
# print(BioData["Place"]) # Kamareddy
# # using get() method:
# print(BioData.get("Name")) # Nandhan
# print(BioData.get("RollNo")) # 66
# print(BioData.get("Branch")) # CSC
# print(BioData.get("Place")) # Kamareddy

# Adding and Updating Dictionary:
# Adding: You can insert a new key-value pari into a dictionary.
# Updating: You can update or change the values using exsisted keys in the dictionary. 
# BioData = {
#     "Name":"Nandhan",
#     "RollNo":66,
#     "Branch":"CSC",
#     "Place":"Hyderabad"
# } 
# update:
# BioData["RollNo"] = 16
# BioData["Name"] = "Nikhil"
# print(BioData)
# # add: 
# BioData["Role"] = "Software developer"
# print(BioData)

# Removing in Dictionary:
# Python gives mutliple ways to delete items from a dictionary. 
# pop(),popitem(),clear(), del(delete)

# BioData = {
#     "Name":"Nandhan",
#     "RollNo":66,
#     "Blood grp":"B+",
#     "Branch":"CSC",
#     "Place":"Hyderabad",
#     "Role":"SDE"
# }
# print(BioData)
# # pop() : Removes the key value
# BioData.pop("Blood grp")
# print(BioData)
# # popitem(): Removes the Last inserted item from the dictionary.
# BioData.popitem()
# print(BioData)
# BioData.popitem()
# print(BioData)
# BioData.popitem()
# print(BioData)
# BioData.popitem()
# print(BioData)
# BioData.popitem()
# print(BioData)
# # del(delete): Deletes the keys from dictionary. 
# del BioData["Place"]
# print(BioData)
# # clear(): Removes every item from the dictionary. 
# BioData.clear()
# print(BioData)

# Dictionary methods:
# Methods allow you to access dictionary data easily. 
# keys(),values(), items()
# BioData = {
#     "Name":"Nandhan",
#     "RollNo":66,
#     "Blood grp":"B+",
#     "Branch":"CSC",
#     "Place":"Hyderabad",
#     "Role":"SDE"
# }
# # keys(): It prints only the keys of dictionary
# print(BioData.keys()) #  n,r,blg,brn,plc,rol
# # values(): It prints only the values of dictionary
# print(BioData.values()) # nan,b+,csc,hy,sde
# # items(): It prints both the keys and values of dictionary
# print(BioData.items())
# # update: Manually we are assigning the values with seperate lines 
# BioData["RollNo"] = 16
# BioData["Name"] = "Nikhil"
# print(BioData)
# # updating update(): update the mutliple values (this is in built method to update mutliple keys )
# BioData.update({"Role":"Web Developer","Place":"Kamareddy"})
# print(BioData)

# Loops for Dictionary:
# We can loop over keys,values,items(both).
# GR = {
#     "Name":"Kaveri",
#     "RollNo":17,
#     "Blood grp":"O-",
#     "Branch":"CSC",
#     "Place":"Kothagudem",
#     "Role":"SDE"
# }
# Loop through keys 
# by-default the loop iterate the keys from the dictionary.
# for i in GR:
#     print(i) # name,roll,bldgrp,braN,plc,role
# The loop iterates the mentioned methods elements. 
# for i in GR.keys():
#     print(i) # name,roll,bldgrp,braN,plc,role
# for i in GR.values():
#     print(i) # kav,17,o-,kg,sde
# for i in GR.items():
#     print(i)

#  Nested  Dictionary:

students = {
    "CR":{"Name":"Nikhil","RollNo":16},
    "GR":{"Name":"Kaveri","RollNo":17} }
print(students["CR"]["Name"])
