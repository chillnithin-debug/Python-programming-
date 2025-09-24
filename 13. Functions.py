# # Functions: 
# # A function is a block of code that performs a specific task.
# # It allows us to group instructions together and reuse them whenever we needed. 
# # Instead of writing the same code again and again, we just define a function once and call it whenever required. 
# # Syntax:
# # def function_name(parameters):
# #     # function body code
# #     return value # optional
# # function_name()
# # example:
# def greet():
#     print("Hello World1")
# greet()
# # Calling a Function:
# # Calling a Function means telling python to run the code inside a function by using it's name followed by paranthese().
# # If the function needs input (parameter), We provide values(argument) inside the parantheses. 
# # When we call a function, Python jumps to the function, excutes it's code,and then comes back to continue the program.
# def greet(): # function name 
#     print("Hello World1") # 
# greet() # calling a function. 

# # Passing Parameters & Arguments. 
# # Parameters: A variable declared inside the function definition. It's acts like an empty container waiting to receive a value.
# # Arguments: The actual value we pass into the function when calling it. It fills the empty container(Parameter.)
# # example: 
# def greet(name):
#     print("Hello",name)
# greet("Nandhan")
# # same task without function.
# name = "Nandhan" # here name is input variable(Parameter), and "Nandhan" is value to the parameter (Argument.)
# print("Hello",name)

# # Types of Functions Arguments:
# # A. Positional Arguments:
# # When we pass Arguments in the same order as the function parameter, they are called positional Arguments.
# # here the order(position) is very important. 
# def greet(rollno,name): # step 2 values store
#     print("Hello",name,"your rollno is",rollno) # step3: excute the line 
# greet("L6","Nandhan") # step1: function calling

# # B. Keyword Arguments: 
# # When we pass values or Arguments by writing the parameter(variable = value), they are called as Keyword Arguments.
# def greet(rollno,name,branch): 
#     print("Hello",name,"your rollno is",rollno) 
# greet(name="Nandhan",rollno="L6",branch="CSM")

# # Default Arguments:
# # When a parameter has default value(assigning the value in parameter) in the function definition, it becomes a default argument. 
# def greet(name="Student"): 
#     print("Hello",name) 
# greet()
# greet(name="Nandhan")

# # D. Varible-Length Arguments:
# # Sometimes we don't know how many arguments will be passed to a function. 
# # Python provides two special ways to handle this:
# # 1. *args:(Varible-Length Arguments): 
# # Collects mutliple values into a tuple. 
# # L = 10,20,30,40,50
# A = 20
# def sum1(*List1):
#     sum2 = 0 
#     for i in range(len(List1)):
#         sum2 = sum2 + List1[i]
#     print(sum2) #150
#     print(type(List1))
# sum1(10,20,30,40,50)
# # 2. **kwargs:(Keyword Varible-Length Arguments)
# # Collects multiple key=value pair into a dictionary. 
# def details(**info):
#     for i,j in info.items():
#         print(i,":",j)
# details(Name="Nandhan",Rollno="L6",Branch="CSM")

# # Scope of the variable:
# # Scope of the variable: 
# # The scope of a variable means the part of the program where that variable can be accessed or used. 
# # In python, variables can be local and global, depending on where they are created. 
# # Local Variable: 
# # A variable declared inside a function is called a local variable. 
# # It exists only while the function is running.
# # It cannot be used outside that function. 
# # Global Variable: 
# # A variable declared outside all function is called a global variable. 
# # It can be accessed anywhere in the program(inside or outside functions). 
# # examples:
# # x = 10 # Global variable
# # def var1():
# #     y = 5 # Local variable 
# #     print("inside var1 function",x,y)
# # var1()
# # def var2():
# #     print("inside var2 function",x,y)
# # var2()

# # print("outside function",x,y)
# # example 2:
# x = 10 # Global variable
# def var1():
#     x = 5 # Local variable 
#     print("inside var1 function",x)
# var1()
# def var2():
#     print("inside var2 function",x)
# var2()

# print("outside function",x)

# # Lambda function:
# # A lambda function is a small, anonymous function in python. 
# # Unlike normal functions defined using def, a lambda function does not have a name. 
# # it is usually used for short,simple operations. 
# # Syntax:
# # lambda arguments: expression
# # normal function for squaring a number 
# #normal function
# def sqe(a):
#     print(a*a) # 25
# sqe(5)
# # lambda function
# n = [10,20,30]
# squ = lambda a:a*a,n
# print(squ(5)) # 25


# factorial 
# 5! = 5 * 4 * 3 * 2 * 1
def factorial(n):
    fact = 1 # 120
    for i in range(1,n+1,1): # 1 2 3 4 5
        fact = fact * i # 120 * 1
    print(fact)
factorial(5)
#recursive: 
def Rfactorial(n):
    if n == 0: # base case 
        return 1
    else:
        return n * Rfactorial(n-1) # recursion case 
Rfactorial(5)

