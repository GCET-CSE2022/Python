# Taking inputs for the sides
h = int(input("Enter Hypotenuse: "))
p = int(input("Enter Perpendicular: "))
b = int(input("Enter Base: "))


# Check if the triangle is right-angled using the Pythagorean Theorem
if h**2 == p**2+ b**2:
    print("The Triangle is right angled")
else:
    print("Not right angled")
