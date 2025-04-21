'''
Author: Yaseen  
Date: 21.04.2025  

Q34. Write a Python program to check whether the string is Symmetrical or
Palindrome
'''
def is_Palindrome(str):
    return str==str[::-1]
str1=input("Enter the String to check if Palindrome or not: ")
print("String is Palindrome: ",is_Palindrome(str1))
