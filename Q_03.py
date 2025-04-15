"""
Author: Numan
Dated: 11-04-2025

"""
# 3. write a program to create, concatenate and print strings and accessing sub-string from a given string.

str1=input("Enter your first Name: ")
str2=input("Enter your Middle_Name: ")
str3=input("Enter your Last Name: ")
str4=str1+" "+str2+" "+str3;     #Concatenate
print("Your Full Name is: ",str4)         #print full string    
print("Your Full Name is: ",str4[0:5])    #Accessing Substring           0 to <5
