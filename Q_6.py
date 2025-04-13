## Tuples conatin heterogeneous elements

# Syntax

tuple_1 = (21,'yaseen','cse',4.22)
print(type(tuple_1))
print(tuple_1)

# Another Syntax

tuple_2 = "faheem","cse",21
print(type(tuple_2))
print(tuple_2)

# Accessing tuple

tuple_3 = ('yaseen','numan','faheem',21,20,21)
name = tuple_3[0]
age = tuple_3[3]
print("\nMy name is {} and I'm {}".format(name,age))

# len() length of tuple
studentId = (2211,3332,4432,4322)
print(len(studentId))

# min() and max()
# minimum and maximum value in tuple
print(min(studentId))
print(max(studentId))

# sum() returns the the total sum of elemens if they are numeric 
prices = (100,120,95)
print(sum(prices))

# tuple() converts others list or strings to tuple
list_1 = ['nadeem',21,'cs']
print(type(list_1))
print(list_1)

tp = tuple(list_1)
print(type(tp))
print(tp)

name = 'momin'
nameTuple = tuple(name)
print(nameTuple) # output: ('m','o','m','i','n') 

## Types of tuples

# Empty tuple
emptyTuple = ()
print(emptyTuple)

# Integer tuple
integerTuple = (15,23,13,12)
print(integerTuple)

# Mixed tuple
mixedTuple = ('yaseen',21,'pinglena')
print(mixedTuple)

# Nested tuple
nestedTuple = ('momin',('cse',2022),[21,6.2,'ant'])
print('\n',nestedTuple[2])
print(nestedTuple[2][1])

# tuples are immutable
studentDetails = ('faheem','5th sem')
print('\n',studentDetails)

# studentDetails[1] = 6
# does not support object assignmentcls

# tuple unpacking and parenthesis is optional

animal = 'dog','cat','eagle'
print('\n',animal)

a,b,c = animal
print(a) # dog
print(b) # cat
print(c) # eagle

# creating a tuple with one element
tuple_0 = ('momin')
print('\n',type(tuple_0))

tuple_0 = ('momin',)
print(tuple_0)
print(type(tuple_0))

tuple_1 = 'numan',
print(tuple_1)
print(type(tuple_1))

# count() returns how many times a value appears in tuple
names = ('momin','numan','faheem','yaseen','momin',20,20,1,3)
print(names.count(20)) # two times
print(names.count('momin')) # two times
print(names.count('faheem'),'\n') # one times

# index() returns index of first occurence of value
t = (1,2,2,5)
print(t.index(2)) # returns 1
print(t.index(5)) # returns 3