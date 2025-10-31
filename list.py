#items=["Mary",12.857,True,108,"This is the last item"]
#print(items)
##print(items[-2])#reverse the list
#print(items[0][0])#gives you index of mary the first letter
#items[-1]="This is no longer the last item"
#print(items)

values =[1,2,3,[4,5,6],[7,8,9,['x','y']],10]
#print(values[4][3][0])
print(len(values))
print(values[2:4])

#   LIST OPERATIONS
#ADDING ITEMS TO A LIST.
#1.append()adds items at the end of a list
#2.extends()adds multiple items
#3.insert()
values.append(11)
#values.append(100)
#value.remove#removes an item by value
#value.pop#removes an item at a specified index but u have to pass the index,otherwise it removes the last item or by default from the list
#value.clear#empties the list(removes everything from te list)
values.extend(["mango","Apple","pineapples"])#extends multiple items
values.insert(0,"pear")#pass the index and value
values.remove("mango",)
values.pop()
print(values)

values.pop(4)#pop with index,removes value at specific index
print(values)

values.clear()
print(values)

#research on count,sort,index,reverse,max,min,copy
fruits=['apples','bananas','coconut','apples','grapes','grapes']
print(fruits.count('apples'))#returns the number of occurences of a number in a list