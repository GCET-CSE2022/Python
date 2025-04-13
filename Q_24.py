# Author: Mubashir
# Date: 13-04-25

# 24.  Python Program for Program to find area of a circle?

def areaOfCircle (Radius) :
    PI = 3.14
    return ("The Area of Circle is :",PI * (Radius * Radius))

Radius = int(input("Enter the Radius :\n"))
Area = areaOfCircle (Radius)
print("The Area of circle is : \n",Area)