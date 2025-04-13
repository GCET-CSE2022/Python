"""
Author: Numan
Dated: 11-04-2025

"""
# 5. Write a program to create,append, and remove lists in python.

list1=[12,19,"Numan",14]         # Create    
print("List1: ",list1)
print("List1: ",list1[2])        # Accessing specific element
print(type(list1))               # type of list1 <List>

list1.append(20)                 # Append
print("List1 after appending: ",list1)


del list1[2]                     # Remove
print("List1 after removing: ",list1) # Remove specific element
list1.clear()  
