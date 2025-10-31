#research on count,sort,index,reverse,max,min,copy
fruits=['apples','bananas','coconut','apples','grapes','grapes']
print(fruits.count('apples'))
#fruits.sort()
#print(fruits)
#print(fruits.index('bananas'))
#fruits.reverse()
#print(fruits)
#numbers=[1,2,3,4,5,6]
#print(max(numbers))
#print(min(numbers))
#print(numbers.copy())
list1=['apple','bananas','coconut']
list1.reverse()
list1.append('bananas')
list1.insert(0,'grapes')
list1.sort()
print(list1)
values=[1,2,3,4,'apples',5,'bananas']
values=sorted(values,key=str)
print(values)

list1=["Brenda","Joy"]
list2=[6,7,8,9,10]
combine=list1+list2
print(combine)

num1=[1,2,3]
num2=[4,5,6]
num1.extend(num2)
print(num1)

value1=['x','y','z']
value2=[10,20,30]
value1.append(value2)
print(value1)

trainees=['john',[2,['james','mary']]]
print(trainees[1][0])
print(trainees[1][1][0])
trainees.append(56)
trainees.insert(8,[1][1][0])
print(trainees)
