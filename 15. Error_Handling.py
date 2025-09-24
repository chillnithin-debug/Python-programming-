# types of error
# try:
  #  i = 2
 #   n = int(input("enter the n value: "))#
  #  if i%2==0:
   #     print("Yes, number is multiple of ",n)
    #else:
     #   print("No, number not is multiple of",n) 
##

# indexerror:
try:
    list = [10,20,30,]# 0 1 2
    n = int (input("enter the index values:"))
    print(list[n])
except:
    print("error: the given index is not from the list")

    # TYPE ERROR 
try:
    List = [10,20,30]
    add = 599 + 900
    print(sum)
except TypeError:
    print("invalid type operation.")

    # name error 
try:
    print(Multiple)
except NameError:
    print("Variable not declared")
    
