my_ds=[23,"Jane",(560),["Lesson","Maths",{"currency":"KES"}],987,(76,"John")]
print(my_ds[3][2]["currency"])
print(my_ds[2])
print(my_ds[3][1])
my_ds[3][2].update({'currency':'KES','Amount':'90'})
print(my_ds[3][2])
#my_list=list(my_ds[5])
#print(my_list)
#my_list[5]='Jane'
#print(my_list)
#[76,'John']
#my_ds[5]=tuple(my_list)
print(my_ds)
#SLICING AND STEPPING
name='Jane Doe'
print(name[::-4])
#basically we are skipping over elements
value=str(my_ds[4])
print(value)
print(type(value))
print(value.split(' '))

#x=value[::-4]
#print(x)
#my_ds[5]=int(x)
y=value[0]+'-'+value[1]+'-'+value[2]
a=y.split('-')
print(a)
a.reverse()
print(a)

b=a[0]+a[1]+a[2]
print(b)
my_ds=b.split