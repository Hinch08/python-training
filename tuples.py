#<**TUPLES**>
#-These are data structures used to hold multiple values that can be changed or removed.
#Are represented using normal brackets()
#   PROPERTIES OF TUPLES
#-They are ordered-uses index to order items
#-Values can't be changed.
#-It can hold multiple values of any type.
#EXAMPLES OF A TUPLE.
days=("Monday","Tuesday","Wednesday","Thursday","Friday")
print(days)
print(type(days))
print(days[-1])#giving the last item of friday

#Finding number of items in a tuple
print(len(days))

#search for an item using index method,returning the index of a specified value
print(days.index('Tuesday'))

#COUNT METHOD-ANNOUNCES THE AMOUNT OF OCCURENCE OF AN ITEM IN A TUPLE
print(days.count('Monday'))

#TASK,HOW TO UPDATE A TUPLE-ADDING ITEMS IN A TUPLE.
#TASK ON SLIDE 38

#changing it to list#convert your tuple list to manipulate then convert back to tuple
fruits=("apple","banana","cherry","banana","mango","banana")
print(fruits.count('banana'))

fruits_list=list(fruits)
print((fruits_list))

fruits_list.pop()
print(fruits_list)

fruits_list.pop()
print(fruits_list)