#8,9,10,11,14 with functions
#WHY USE FUNCTI0NS?
#A Reusable block of code
#code organization
#code modularity
#code reusability
#better debugging
#scalability of code
#python functions are created using the def keyword
#Syntax---->
# def function_name():
#   #//function body
#defines what the function actually does.
#function call,call the function to execute and return a value
#all python functions end in brackets()
#for example
#are used with return key word
#NOTE:return keyword signifies the end of a function and nothing can call below
# VARIABLE SCOPES: 
#a scope determines accessibility of a variable.
#types of scopes:
#1.local scope,2.globa scope
#local variable-A variables accesible within only a block
##global variable-a variable accessible throughout the program/entire program
#Accessible both within and outside 
#parameters:define the following concepts
#parameters are temporary values passed in a function to make it reusable.
#parameters are passed within a function definition
#arguments:These are real values passed when calling a function in place of parameters,when calling a function.
#NOTE nu
# 
# mber of arguments passed has to match the number and order of parameters.
a=4
b=5
c=a+b
def add_numbers():
    a=4
    b=5
    c=a+b
    return c
#function call
sum=add_numbers()
print(sum)

def add_numbers(a,b):
    return a+b
sum1=add_numbers(4,5)
sum2=add_numbers(10,20)
print(sum1+sum2)
#q1,q2,q3
#slide 20
#slide 20
maths=float(input("Enter mathematics marks: "))
eng=float(input("Enter english marks: "))
kisw=float(input("Enter kiswahili marks: "))
sci=float(input("Enter science marks: "))
sst=float(input("Enter social studies marks: "))
def total_marks(maths,eng,kisw,sci,sst):
    return maths+eng+kisw+sci+sst
result=total_marks(maths,eng,kisw,sci,sst)
print("Total marks:",result)

def get_average(x):
    return x/5
average=get_average(result)
print("Average marks:",average)

def grade(average):
    if average>80:
        return 'A'
    elif average>60:    
        return 'B'
    elif average>50:
        return 'C'
    elif average>40:
        return 'D'
    else:
        return 'E' 
final_grade=grade(average)
print("Final grade:",final_grade)
