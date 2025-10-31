#numbers=(10,20,30,40,50)
#numbers_list=list(numbers)
#numbers_list.append(60)
#numbers_list.remove(30)
#numbers_list.insert(2,35)
#print(numbers_list)

#values=(15,5,30,25,10)
#values_list=list(values)
#values_list.sort(reverse=False)
#print(values_list)

fruits=('apple','banana','cherry','banana','mango','banana')
print(fruits.count('banana'))

fruits_list=list(fruits)

while 'banana'in fruits_list:
    fruits_list.remove('banana')
print(fruits_list) 

names=('Alice','Bob','Charlie','David')
names_list=list(names)
names_list.sort(reverse='True')
print(names_list)

colors1=('red','blue','green')
colors2=('purple','orange')
colors_list1=list(colors1)
colors_list2=list(colors2)
colors_list1.insert(1,'yellow')
result=colors_list1+colors_list2
print(result)

my_ds=[23,'jane',(560),['lesson','maths',{'currency':'KES'}],987,(76,'john')]
print(my_ds[3][2]['currency'])
print(my_ds[2])
print(my_ds[3][1])
my_ds[3][2].update({'currency':'KES','Amount':'90'})
print(my_ds)
my_list=list(my_ds[5])
my_list.remove('john')
my_list.append('jane')
print(my_list)
