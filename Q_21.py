'''
Author: Yaseen
Date: 13.04.2025

Q21. Write a program to multiply the elements of a list and then divide the result by the size of the list and return the remainder
'''

L1 = []
i = 1
n = int(input("Enter the number of elements: "))

# Taking input from the user
while n > 0:
    L1.append(int(input(f"Enter the number {i}: ")))
    n -= 1
    i += 1

i = 1  # Reusing 'i' to store product of elements
for el in L1:
    i = el * i

result = i % len(L1)
print("The remainder of the array is: ", result)
