#A collection of unique unordered items.
#These sets are represented using curly braces-{}
#-----properties of sets----------
#1.They are unordered.(Have no indexing).
#2.They are unique.-Their value are unique.-Have no duplicate values.
#3.They are mutable-They can be changed.
#example:
#numbers={1,1,2,3,4}
#print(numbers)
#print(type(numbers))
#numbers=list(numbers)
#print(numbers)
#print(len(numbers))
#print(max(numbers))
#print(min(numbers))
#numbers.append(1)
#numbers.insert(0,'mary')
#print(numbers)
#METHODS/SET OPERATIONS(HOW DO WE ACCES ITEMS IN A SET?)
#values={'X','DD','YY'}
#print(values)
#print(73 in numbers)

numbers={100,75,56,23}
#print(numbers)
#print(numbers)
#print(type(numbers))
#print(73 in numbers)
#numbers=list(numbers)
#print(numbers)
#numbers.add("Mexico")
print(numbers)

#updating a set after making it a list
numbers.update([500,600,700])
print(numbers)

#Removing items from a set
#.remove()
#pass an item to be removed
#if  item doesnt exist it throws an error .discard
numbers.remove(100)
print(numbers)

numbers.discard(1)
print(numbers)

numbers.clear()
print(numbers)


