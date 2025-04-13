# program to find the area of a circle 


def areaOfCircle (Radius) :
    PI = 3.14
    return ("The Area of Circle is :",PI * (Radius * Radius))

Radius = int(input("Enter the Radius :\n"))
Area = areaOfCircle (Radius)
print("The Area of circle is : \n",Area)