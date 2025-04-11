"""
Author: Numan
Dated: 11-04-2025

"""


"""
1. Write a python program to demonstrate different data types in python.
-------------------> Frequently used data types in Python <-------------------
"""

str="Numan"                    #String
int=19                         #Integer
float=5.003                    #Float
bool=False                     #Boolean
list=[12,15,19]                #List
tuple=(12,15,19)               #Tuple
dict={"name":"Numan","age":20} #Dictionary
set={1,2,3}                    #Set
frozenset=frozenset({12,15,19})#Frozenset
range=range(5)                 #Range


print(type(str))
print(type(int))
print(type(float))
print(type(bool))
print(type(list))
print(type(tuple))
print(type(dict))
print(type(set))
print(type(frozenset))
print(type(range))



# 2 Write a program to perform airthmetic operations of numbers in python.

# -----------> Arithmetic Operations <-----------


def Calculate (num1,num2,op):
    if(op=="/" and num2==0):
        return "Division by Zero is not allowed!"
    elif(op=="/" and num2!=0):
        return num1/num2
    elif(op=="*"):
        return num1*num2
    elif(op=="+"): 
        return num1+num2
    elif(op=="-"):
        return num1-num2
    else:
        return "Invalid Operator"
    
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
op=input("Choose Operator (+,-,*,/): ")
result=Calculate(num1,num2,op)    
print("Result is: ",result)


# 3. write a program to create, concatenate and print strings and accessing sub-string from a given string.

str1=input("Enter your first Name: ")
str2=input("Enter your Middle_Name: ")
str3=input("Enter your Last Name: ")
str4=str1+" "+str2+" "+str3;     #Concatenate
print("Your Full Name is: ",str4)         #print full string    
print("Your Full Name is: ",str4[0:5])    #Accessing Substring           0 to <5


# 4. Write a python script to print the current date in the following format "Sub May 29 02:26:23 IST 2017".

import time;
currTime=time.localtime()
print(currTime)
# strf()----> built in fxn in time module that formats time values into the strings.
finalTime=time.strftime("%a %b %d %H:%M:%S IST %Y", currTime)
print(finalTime)

"""
Key points:

a --> weeday
b --> month
d --> day of the month
H --> hour(24-hour format)
M --> minutes
S --> seconds
Y --> year
IST--> Indian Standard Time(HArd coded)
 
"""

# 5. Write a program to create,append, and remove lists in python.

list1=[12,19,"Numan",14]         # Create    
print("List1: ",list1)
print("List1: ",list1[2])        # Accessing specific element
print(type(list1))               # type of list1 <List>

list1.append(20)                 # Append
print("List1 after appending: ",list1)


del list1[2]                     # Remove
print("List1 after removing: ",list1) # Remove specific element
list1.clear()                      # Clear