"""
Author: Numan
Dated: 11-04-2025

"""
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