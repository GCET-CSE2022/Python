"""
Author: Numan
Dated: 21-04-2025

"""


# 29. Program to accept the strings which contains all vowels


def check_Vowel(str):
    vowels=set('aeiou')
    
    s=set({})
    
    for char in str:
        if char in vowels:
            s.add(char)
    else:
        pass
    if(len(s)==len(vowels)):
        print("Accepted")
    else:
        print("Not Accepted")    
string="aeiouasd"
check_Vowel(string)
