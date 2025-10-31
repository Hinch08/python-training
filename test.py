#research on count,sort,index,reverse,max,min,copy
#fruits=['apples','bananas','coconut','apples','grapes','grapes']
#print(fruits.count('apples'))
#fruits.sort()
#print(fruits)
#print(fruits.index('bananas'))
#fruits.reverse()
#print(fruits)
#numbers=[1,2,3,4,5,6]
#print(max(numbers))
#print(min(numbers))
#print(numbers.copy())
#list1=['apple','bananas','coconut']
#list1.reverse()
#list1.append('bananas')
#list1.remove('apple')
#list1.insert(0,'grapes')
#list1.sort()
#print(list1)
#values=[1,2,3,4,'apples',5,'bananas']
#values=sorted(values,key=str)
#print(values)

fruits=['Apples','apples','Bananas','Coconut']
fruits.sort()
print(fruits)

fruits.sort(reverse=True)#can sort in descending order
print(fruits)

print(max(fruits))#finds the largest value in a list.
print(min(fruits))#Finds the smallest value in a list.

numbers=[1,2,3,4,5]
print(max(numbers))
print(min(numbers))
numbers.reverse()
max=max(numbers)
print(numbers)
print()