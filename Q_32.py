#Author: FAB  
#Dated: 21st April, 2025
#Q_32 Python program to sort a list of tuples by second Item

t_list = [('a', 3), ('b', 1), ('c', 2)]

# Sort by second item using lambda function
sorted_list = sorted(t_list, key=lambda x: x[1])

print("Sorted by second item:", sorted_list)
