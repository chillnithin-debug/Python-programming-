# Sets in python:
# Set is a collection datatype which is used to stored mutliple values in a single varaible.
# Sets are unordered, unindexed, mutable, and they do not allow duplicate values. 
# They are useful when you want to store unique elements and performs the mathematical operationsl like union, intersection, and difference. 
# Syntax: 
# my_set = {element1,element2,element3}

# Characteristics of Sets: 
# unordered:
# example : {1,2,3} and {3,2,1} are considered the same set.
# s1 = {1,2,3,4}
# s2 = {3,2,1,4}
# print(s1 == s2)
# print(s2)
# unindexed: You cannot access set elements by the index like lists or tuples.
# s1 = {1,2,3,4}
# print(s1[2]) # error 
# Duplicate values: Duplicate values are automatically removed from the set
# s1 = {1,1,2,3,3,5,1,4,2,2,5}
# print(s1) # {1,2,3,4,5}

# Creating a set:

# S1 = {10,20,30,40,50} 
# # mixed datatype values. 
# S2 = {10,10.2,"Hello",True}

# # Eampty Set:
# E = {} # dict
# ES = set()
# print(ES)
# print(type(ES)) # set

# Accessing sets:
# We cannot directly access an element using index but we access an element using loops.
# roles = {"Deva","Simon","Dayal","Kali","Dheya"}
# for i in roles:
#     print(i)

# Adding an element in sets:
# add():# adds only single element in any position 
# A = {12,78,25,52,95,44}
# A.add(128) 
# print(A)
# # update():# adds the mutliple values in the set
# A = {12,78,25,52,95,44}
# A.update([11,10])
# print(A)

# Deleting the elemets in set:
# A = {12,12,12,12,12,78,25,52,95,44}
# # remove():  Removes the element, but it gives an error if the value is not found in the set
# # A.remove(6)
# print(A)
# # discard(): Removes the element, but it gives no error if the value is not found in the set
# A.discard(6)
# print(A)
# # clear(): Removes the every element from the set.
# A.clear() # set()
# print(A)
# # pop(): Removes the random element from the set. 
# A.pop()
# print(A) 

# Mathematical Operations in set:
# Union "U" = "|": Prints all unique values or elements from the both sets. 
# A = {1,2,3,4}
# B = {3,4,5,6}
# print(A | B) # {1,2,3,4,5,6}
# # Intersection "∩" = "&": Prints the common elements from the set
# print(A & B) # {3,4} 
# # Difference "-" = "-": removes the common elements from the lists but prints only the first sets values
# print(A - B) # 1,2
# print(B - A) # 5,6
# # Symmetric difference "Δ" = "^": 
# # removes the common elements from the lists but prints only the first sets values.
# print(A ^ B) # 1,2,5,6

# Mathematical operations using functions: 
# A = {1,2,3,4}
# B = {3,4,5,6}
# # Union: union()
# print(A.union(B))
# # Intersection: intersection()
# print(A.intersection(B))
# # Difference: difference()
# print(A.difference(B))
# # Symmetric difference: symmetric_difference()
# print(A.symmetric_difference(B))

A = {1,2,5,78,95,56,79,25,26}
# length:
print(len(A))
# max:
print(max(A))
# min:
print(min(A))
# sum:
print(sum(A))

# sort
print(count(A))
# reverse
# count 
