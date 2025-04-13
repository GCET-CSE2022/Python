'''
Author: Yaseen  
Date: 13.04.2025  
Purpose: To reverse a given string  
'''

class Rev:
    def Rev_Str(self):
        str1 = input("Enter the string: ")
        str2 = str1[::-1]
        return str2

print("Reversed string is:", Rev().Rev_Str())
