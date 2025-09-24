#if statement:
if True:
    print("Yes condition is true")
# #if - else statement 
Age = int(input("Enter your Age: "))
if Age>=18: 
    print("He/her is a major.")
else:
    print("He/her is a minor.")

#if-elif-else:
#if-elif-else is also called as chained conditional statements. 
#It is used when you have more than two possible outcomes. 
#it checks conditions in order and excutes the block for the first one that is true. 
#The final ELSE is optionaland runs if none of the preceding conditions were met. 
#syntax:
# if condition:
#     block1 
# elif condition:
#     block2
# elif condition:
#     block3
# elif condition:
#     block4
# else: 
#     block5(optional of none of the above is true)
 
#example: 
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: O")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
elif marks >= 45:
    print("Grade: P")
else:
    print("Grade: F")

#Nested if-else conditions:
#In nested if-else control flow statement we can place control flow statements inside other one.
#This is also called as Nesting conditional statements.
# Syntax:
# if condition:
#     if condition: 
#         block 3
#     else:
#         block 4
# else: 
#     block 2 
#Example :
# Drivers_Age = int(input("Tell your Age: "))
# Drivers_lic = bool(input("Show your Lic:  "))
# if Drivers_Age >= 18:
#     print("Yes you are major")
#     if Drivers_lic == True:
#         print("You can go ")
#     else: 
#         print("Fine: 2000")
# else:
#     print("your are minor")
#     print("tell your father number,fine is 20,000")

Drivers_Age = int(input("Tell your Age: "))
Drivers_lic = input("Do you have a License? (yes/no): ")

if Drivers_Age >= 18:
    print("Yes, you are major")
    if Drivers_lic == "yes":
        print("You can go")
    else:
        print("Fine: 2000")
else:
    print("You are minor")
    print("Tell your father number, fine is 20,000")
