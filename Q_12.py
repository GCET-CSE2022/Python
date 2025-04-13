# factorial function
def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# taking user input
n = int(input("Enter a number: "))

# calling the function and printing result
result = factorial(n)
print(f"Factorial of {n} is {result}")
