# Author: Mubashir
# Date: 13-04-25


# 23. Python program to check whether a number is Prime or not?
              
              
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

    