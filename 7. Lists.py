#Collection Data Types 
#list,tuple,set,dictionary
# List 
#index   0  1  2  3  4
# list1 = [10,20,30,40,50] #list with integers
# list2 = [10.1,20.2,30.3,40.4,50.5]#list with float
# list3 = ["apple","banana","mango"]#list with Strings
# list4 = [True,False,True,False] #list with Boolean
# list5 = [10,10.1,"apple",True,"False"] #list with mixed datatypes
#        #  0  1      2      3     4
# print(list5)

#Accessing Elements in list
# Accessing Elements are retriving a value stored a perticular position using index values. 
# index value is used to store a value in a perticular position 
# index are start from 0 to n-1
# list1 = [10,20,30,40,50]
# print(list1[0]) # 10
# print(list1[1]) # 20 
# print(list1[2]) # 30
# print(list1[3]) # 40 
# print(list1[4]) # 50
# print(list1[-1]) # 50
# print(list1[-2]) # 40 
# print(list1[-3]) # 30
# print(list1[-4]) # 20 
# print(list1[-5]) # 10

# Adding the elements in list 
# We can add the new values or elements to a list in different ways those are:  # list1 = [10,20,30,40,50,60]
# 1. append(): Adds a single element or value at the end of the list.
#list1.append(70)
# 2. insert(): Adds a single element or value at the perticular position using index
# list1.insert(2,25)
# 3. extend(): Adds the multiple values or elements by combining the another list 
#list1.insert([80,90,100])

#              0             1      2    3    4     5
# Kalkicast = ["prabhas","Amitha b","DQ","KH","SSR","Anudeep"]
# # Add a new role for prabhas owner
# Kalkicast.append("Bhramanandham")
# print(Kalkicast)
# Kalkicast.insert(3,"Deepika P")
# print(Kalkicast)
# Kalkicast.extend(["RGV","Vijay D"])
# print(Kalkicast)
# # insert the new role After KH MT
# Kalkicast.insert(5,"Deepika P")
# print(Kalkicast)

# Removing Elements 
# Deleting the elements or values using different ways:
# 1. remove(): it removes a single element which is occured first from the list 
# Kalkicast.remove("DQ")
# print(Kalkicast)
# 2. pop(): it removes a single element from a perticular position frpm lists 
# Kalkicast.pop(5)
# print(Kalkicast)
# 3. clear(): It removes the every element from the list.
# Kalkicast.clear()
# print(Kalkicast)

#Changing Elements: 
# list1 = [10,25,30,40,50,60]
# #index   0  1  2  3  4  5
# list1[1] = 20
# print(list1)
# Mathematical operation 
#  1. concatenation: Which joins two different lists 
# a = [1,2]
# b = [5,8]
# c = a+b
# print(c)
# 2.Repetition: Repeats the lists multiple times 
# a = ["hi","hello"]
# n = int(input("Enter the n value:"))
# print(a*n)
# Searching and Checking:
# We can check if an elements or values exists in a list or not:
# in operator: 
# It is a membership operator, which returns the Trues values if the elements exists in the lists.
# a = [2,4,6,8,8,8,10,12,14]
# if 2 in a:
#     print("Yes item is present in the list ")
# not in operator:
# It is a membership operator, which returns the Trues values if the elements is not exists in the list.
# a = [2,4,6,8,8,10,12,14]
#idx 0 1 2 3 4  5  6  7
# if 2 in a:
#     print("Yes item is present in the list ")
# # not in operator:
# print(3 not in a)
# index(): 
# Which gives the position of the first occurrence of an element or value.
# print(a.index(8)) # 3
# #count():  Which gives the number of elements in the lists. 
# print(a.count(8)) # 2

# Sorting: sort()
# It arranges elements either in ascending order (small to large) or descending order (large to small).
# Reversing: reverse():
# It Flips the list so the last element will becomes the first element.
# st = [25,12,31,2,18,7,45,10,67,50,17,15,99]
# # reverse = 99,15,17,50,67,10,45,7,18,2,31,12,25
# st.reverse()
# print(st)
# st = [25,12,31,2,18,7,45,10,67,50,17,15,99]
#AO = 2,7,10,12,15,17,18,25,31,45,50,67,99
# st.sort()
# #DO = 99 67 50 45 31 25 18 17 15 12 10 7 2
# st.reverse()
# print(st) 
# using sorting for DO
# st = [25,12,31,2,18,7,45,10,67,50,17,15,99]
# st.sort(reverse=True)#DO = 99 67 50 45 31 25 18 17 15 12 10 7 2
# print(st)

# Copying the list:
# copying creates a new list with the same elements, so chsnges in the new list do not affect the orginal list. 
# frd1 = ["A","C","D","B","A","C","C","D","B","B"]
# frd2 = frd1.copy()
# print(frd2)

#Built - in function 
# Python Programming provides many ready-made functions to work with the items
# length: len() : It returns the number of items in the list.
# st = [25,12,31,2,18,7,45,10,67,50,17,15,99]
# print(len(st)) # 13
# # maximum: max():  It returns the maximum number in the list.
# print(max(st)) # 99
# # minimum: min(): It returns the manimum number in the list.
# print(min(st)) # 2
# # sum(): It returns the total sum of lists.
# print(sum(st)) # 398
# b = "hello world to the python programming"
# print(b.split())


# Multipli values using input data to the list :map()
# b =  input("Enter the List items: ").split() # i/p: 10 20 30 40 50 
# print(b) #o/p= ['10','20','30','40','50'] # values in string
# a = list(map(int,input("Enter the List items: ").split())) # i/p: 10 20 30 40 50
# print(max(a))
# print(a) #o/p= [10,20,30,40,50] # values in numbers
# c = list(input("Enter the List items: ").split()) # i/p: 10 20
# print(c) #o/p=['1','0',' ','2','0']

# Traversing a List:
# Accessing the elements using a loop
# using for loop 
# cars = ["thar","jaguer","Audi","bmw","hhh"]
# index    0      1       2       3    4
# iterating only indexs of list
# l = len(cars) #5
# for i in range(0,l): # 0 1 2 3 4
#     print(i)
# iterating the values in the list using index values:
# l = len(cars) #5
# for i in range(0,l): # 0 1 2 3 4
#     print(cars[i]) # 0 1 2 3 4

# iterating the values in the list 
# for car in cars:
#     print(car)
# output:
# thar
# jaguer
# Audi
# bmw
# hhh

# Adding elements to the list using for loop: 
# a 10 20 30 40 50 
# list1 = []
# n = int(input("Enter the number of items: ")) #11
# for i in range(n):# i 0 1 2 3 4 5 6 7 8 9 10
#     v = int(input("Enter the items: "))
#     list1.append(v)
# print(list1)
#give the input values to the lists from 0 to 10
# list1 = []
# n = int(input("Enter the number of items: ")) #11
# for i in range(n):# i 0 1 2 3 4 5 6 7 8 9 10
#     list1.append(i) # adds i values 
# print(list1)
#give the input values to the lists from 1 to 10
# list1 = []
# n = int(input("Enter the number of items: ")) #11
# for i in range(1,n):# i  1 2 3 4 5 6 7 8 9 10
#     list1.append(i) # adds i values 
# print(list1)
# sum of list items = 10 20 30 40 50 without using sum().
# a = [10,20,30,40,50]
# sum = 0
# for i in a:
#     sum = sum + i
# print(sum)
# #Convert ["p","y","t","h","o","n"] to python
# b = ["p","y","t","h","o","n"]
# word = ""
# for i in b:
#     word = word + i
# print(word)
# Find the Maximum and minimum number from list without using max() and min(). 
# numbers = [59,200,8,5,219,229,227,54,68,84,58]
# max_n = numbers[0] #229
# min_n = numbers[0] #5 
# for i in numbers: #i = 59,200,8,5,219,229,227,54,68,84,58
#     if i > max_n: # 227 > 229
#         max_n = i
#     if i < min_n: # 227 < 5
#         min_n = i
# print(max_n)
# print(min_n)


# numbers = [59,200,8,5,219,229,227,54,68,84,58]
# numbers.clear()
# print(numbers)
# print(numbers[0]) # minimum value
# print(numbers[10]) # maximum value
 
# Searching for an element in a List
# P_names = ["Modi","Revanth Reddy","PSPK","YSR"]
# searching_name = input("Enter the name to be search in the list: ") # ysr ktr 
# found = False
# l = len(P_names) #l = 4
# for i in range(l): # 0 1 2 3
#     if searching_name == P_names[i]:
#         found = True
    
# if found: 
#     print("Yes")
# else: 
#     print("No")

# Count even and odd numbers 
# a = [2,5,99,7,6,23,44,48,52,77,62,61,0]
# evn_cnt = 0
# odd_cnt = 0
# for i in a:
#     if i%2==0:
#         evn_cnt += 1
#     else:
#         odd_cnt += 1
# print("Number of even numbers in the list: ",evn_cnt)
# print("Number of odd numbers in the list: ",odd_cnt)
# Reversing a list without reverse
# a = [2,5,99,7,6,23,44,48,52,77,62,61]
# #i   0 1  2 3 4  5  6  7  8  9  10 11 
# l = len(a) # 12
# r_list = []
# for i in range(l-1,-1,-1):
#     r_list.append(a[i])
# print(r_list)
# Removing all negative numbers using loop  
# o = 5, 6, 23, 48, 52, 62
# a = [-2,5,-99,-7,6,23,-44,48,52,-77,62,-61]
# p_list = []
# for i in a:
#     if i > 0:
#         p_list.append(i)
# print(p_list)

# Multiply each element with 2 in the list
a = [-2,5,-99,-7,6,23,-44,48,52,-77,62,-61]
b = []
for i in a:
    b.append(i*2)
print(b)