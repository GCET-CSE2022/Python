# program to check if a number is prime or not ?

import math

num = int(input("Enter a number: \n"))

if num < 2:
    print(num, "is not a Prime Number")
else:
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            print(num, "is not a Prime Number")
            break
    else:
        
        print(num, "is a Prime Number")

    