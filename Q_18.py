'''
Author: Yaseen
Date: 13.04.2025
Purpose: Convert the input integer value to a Roman numeral
'''

def To_Roman(num):
    Int_Value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    Roman_Symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    Roman_Output = ''
    i = 0
    while num > 0:
        count = num // Int_Value[i]
        Roman_Output += Roman_Symbol[i] * count
        num -= Int_Value[i] * count
        i += 1
    return Roman_Output


num = int(input("Enter the INTEGER value: "))
if num > 0:
    print("The integer value is: ", num)
    print("The Roman numeral equivalent is: ", To_Roman(num))
else:
    print("Invalid input")
