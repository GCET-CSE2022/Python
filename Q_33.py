'''
Author: peermomin  
Date: 23.04.2025  

Q_33. Python program to find sum of squares of first n natural numbers.

'''

def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

n = int(input("Enter number of naturals: "))
num_sum = sum_of_squares(n)
print("sum of squares of {} natural numbers is {}".format(n,num_sum))