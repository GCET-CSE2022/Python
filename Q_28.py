"""
Author: Numan
Dated: 21-04-2025

"""

# 28. Python program to interchange first and last elements in a list


def swap(list):
    n=len(list)
   
    if (n==0):
        return "List is empty"
    else:
        temp=list[0]
        list[0]=list[-1]
        list[-1]=temp
        return list
    
my_list=[5, 8, 12, 15, 30]
print(swap(my_list))


