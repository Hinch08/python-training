students={
    'name':'John Obuor',
    'age':'15',
    'class':'grade 10',
    'school':'high school',
    'performance':'average'
}
print(students)
print(students.get('name'))
print(students.get('age'))
print(students.get('class'))
print(students.get('school'))
print(students.get('performance'))
students['I.D']='1234567'
students['cars_they_drive']='Ford chevy'
students['name']='John Kihungu'
print(students)
students.update({
    'name':'Mary Kibotho',
    'age':'14',
    'class':'grade 9',
    'school':'primary',
    'performance':'Good',
})
print(students)
students.pop('cars_they_drive')
print(students)

students.popitem()
print(students)

print(students.keys())
print(students.items())
print(students.values())
print(students)

