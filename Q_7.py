# Creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "course": "Computer Science",
    "grades": [85, 90, 92]
}

# Accessing dictionary elements
print("Name:", student["name"])
print("Age:", student.get("age"))  # using get() method

# Adding a new key-value pair
student["university"] = "XYZ University"
print("After adding university:", student)

# Updating a value
student["age"] = 22
print("After updating age:", student)

# Deleting a key-value pair
del student["grades"]
print("After deleting grades:", student)

# Looping through keys and values
print("\nLooping through dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "course" in student:
    print("\nCourse exists in student dictionary.")

# Dictionary methods
keys = student.keys()
values = student.values()
items = student.items()

print("\nKeys:", keys)
print("Values:", values)
print("Items:", items)

# Copying dictionary
student_copy = student.copy()
print("\nCopied Dictionary:", student_copy)

# Clearing dictionary
student.clear()
print("After clearing:", student)
