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