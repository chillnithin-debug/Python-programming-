# Tuples:
# immutable, Also allows the duplicate values 

#example: 
# T = (10,20,30)
# print(T)
# print(type(T))

# Creating a Tuple:
# Empty Tuple:
# E = ()
# tuple with numbers:
# T = (10,20,30)
# tuple with String:
# St = ("A","B","C","a","b","c")
# # tuple with mixed datatypes 
# M = (10,10.5,"hi",True,"False")
# # Tuple with a single value
# S = (10,) # tuple
# a = 10 # int
# b = [10] #list
# print(type(S))
# print(type(a))
# print(type(b))


# Accessing an element from the tuple. 
# A = (10,20,30,40,50) 
# #i    0  1  2  3  4
# #i   -5 -4 -3 -2 -1
# print(A[0]) # 10
# print(A[1]) # 20
# print(A[2]) # 30
# print(A[3]) # 40
# print(A[4]) # 50
# print(A[-1]) # 50
# print(A[-2]) # 40
# print(A[-3]) # 30
# print(A[-4]) # 20
# print(A[-5]) # 10

# Slicing the tuple: 
# A = (10,20,30,40,50) 
# print(A[1:4])
# print(A[:3])

# Changing the values:
# A = (10,20,30,40,50)
# A[2] = 60
# print(A) #TypeError: 'tuple' object does not support item assignment

# Mathemarical operations 
# concatenation: 
# t1 = (1,2,3)
# t2 = (4,5)
# C = t1+t2
# print(C)
# Repetition
# t1 = (1,2,3)
# C = t1*3
# print(C)

# Searching and Checking:
# in operator:
# not in operator:

# SC = ("apple","Banana","Mango")
# print("apple" in SC) # True
# print("apple" not in SC) # False 

# index():
# count():
# T1 = (2,4,4,4,6,8,10,12,14)
# print(T1.index(4))
# print(T1.count(4))

# len,max,min,sum
# T1 = (2,4,4,4,6,8,10,12,14) 
# print(len(T1))
# print(max(T1))
# print(min(T1))
# print(sum(T1))

# nested tuple:
# Tuple in tuple
#  in =   0 1   0 1
# N = (1,2,(3,4),(5,6)) # N = (1,2,3,4,5,6)
# #i  =0 1   2     3     #  i= 0 1 2 3 4 5  
# print(N[2]) # (3,4)
# print(N[2][1]) # 4

# Iterate the tuple using for loop.
# T1 = (2,4,4,4,6,8,10,12,14) 
# for i in T1:
#     print(i)

# Sum of all elements in the tuple. 
# find the length of the tuple without using len().
T1 = (2,4,4,4,6,8,10,12,14) 
length = 0
for i in T1:
    length += 1
print(length)

# Multiply each element with 2 in the tuple
a = (-2,5,-99,-7,6,23,-44,48,52,-77,62,-61)
b = [] # list 
for i in a:
    b.append(i*2)
print(b)