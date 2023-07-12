
#A function returns a list but not generator
def arealist():
    list = []
    for i in range(10):
        list.append(i**2)
    return list
print(arealist())

# Here is generator
def areaGenerator():
    for i in range(10):
        yield i**2

print('calling areaGenerator() function:')
print(areaGenerator()) # returns a generator object

# It doesn't occupie a place in memory. Whenever it needs an item, it goes to the function, it generates the specific item and then it returns it
print('calling each item in area() func - the function returns a generator object:')
for i in areaGenerator():
    print( i)

#A list but not generator
print('Making a list in one line and no need a function')
list = [i**2 for i in range(10)]
print(list)

#Here is generator
print('generator but in one line instead a function')
generator = (i**2 for i in range(10))
print(generator) # returns a generator object

for i in generator:
    print(i)




