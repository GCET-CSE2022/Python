'''
Author: Yaseen
Date: 13.04.2025

Q22. Write a program to get the cube sum of first n natural numbers
'''

n = int(input("Enter the number up to which cube sum is needed: "))
total = 0

while n > 0:
    total = total + pow(n, 3)
    n -= 1

print("The result is:", total)
