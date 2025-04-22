## Author: peermomin
## Date: 22-04-2025

## Python code to cheack if a number is palindrome.

def is_palindrome(number):
    # covert to string
    num_str = str(number)
    # check if string is equal to its reverse
    return num_str == num_str[::-1]

# get input from user
number = int(input("Enter a number: "))
if is_palindrome(number):
    print("{} is a palindrome.\n".format(number))
else:
    print("{} is not a palindrome.\n".format(number))

## Python program to find sum of squares of first n natural numbers 

def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

n = int(input("Enter number of naturals: "))
num_sum = sum_of_squares(n)
print("sum of squares of {} natural numbers is {}".format(n,num_sum))