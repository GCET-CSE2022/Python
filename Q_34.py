'''
Author: Yaseen  
Date: 21.04.2025  

Q34. Write a Python program to check whether the string is Symmetrical or
Palindrome
'''
def is_Symm_Palin(str):
    palindrome= str==str[::-1]
    len1=len(str1)
    half=len1//2
    if len1%2==0:
        symmetric = str1[:half] == str1[half:]
    else:
        symmetric = str1[:half] == str1[half+1:]
    print(f"is String Palindrome->{palindrome}\nis String Symmetric->{symmetric}")
str1=input("Enter the String to check if Palindrome or not: ")
is_Symm_Palin(str1)
