'''
Author: Yaseen  
Date: 13.04.2025  

Q19. Write a program to calculate the power of a given number (n^p) using a loop  
'''
n = int(input("Enter the number: "))
p = int(input("Enter the power: "))
val = 1 
while p > 0:
    val = val * n
    p = p - 1
print("The value is:", val)
