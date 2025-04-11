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

# count() returns how many times a value appears in tuple
names = ('momin','numan','faheem','yaseen','momin',20,20,1,3)
print(names.count(20)) # two times
print(names.count('momin')) # two times
print(names.count('faheem'),'\n') # one times

# index() returns index of first occurence of value
t = (1,2,2,5)
print(t.index(2)) # returns 1
print(t.index(5)) # returns 3