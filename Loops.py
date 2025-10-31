#A loop is basically a programming structure that repeats a block of code multiple times until a condition is met.
#It is also caled iteration.

#why use loops?
#-To avoid writing repetitive code.
#-Automatically to process collections of Data,better and faster.
#-when the condition is met the loops breaks.

#TYPES OF LOOPS
#for loop-iterates through a sequence.(str,lists,tuples)(uses for keyword)
#Used when iterating through a sequence
#-Used when you know a number of iterations.
fruits=['mango','orange','kiwi','banana','apple']#collection
#for fruits in fruits:#loop
    #print(fruits)#output
#for is the key word
#fruits is a single value(variable representing a single value of fruits in fruit i the fruits list)
#for i in fruits:
#print(i)

#for number in range(1,501):
    #print(number)    
#for range(100)->starts from 0 and ends at 99
#for range(1000)->starts from 0 and ends at 999
#while loop-this repeates as long as the condition is true.(uses for whileword).
#While loop,used when you don't know how many times the loop will run.
#while loops keeps running until the condition is false.

i=0
while i < 5:
    print(i)
    i+=1

name='Alice'
for i in name:
    print(i)

num=0
for i in range(10,41):
    num=+i
    print('Your sum is:',num)

total=sum(range(10,41))
print(total)

# Ask user for start and end values
#start = int(input("Enter the starting number: "))
#end = int(input("Enter the ending number: "))

# Ask user for a number
#num = int(input("Enter a number: "))

# Print multiplication table
#print(f"\nMultiplication Table for {num}:\n")

#for i in range(1, 11):
    #print(f"{num} x {i} = {num * i}")

#list1=[]
#for i in range(1,51):
    #list.append(i)
    #rint(list)

#list2=[]
#for i in list1:
    #if i%7 ==0 or i%5 ==0:
        #ist2.append(i)
#print(list2)    

#odd_numbers=[]
#for i in range(10,51):
    #if i%2 !=0:
        #odd_numbers.append(i)
        #if len(odd_numbers)==10:
            #break
    #print(i)

#for i in range(1,50):
    #if i%2==0:
        #print(i)

ls1=[('jay',20),('Mo',30),('mya',32)]
sum=0
for i in ls1:
    sum+=int(i[1])
    #print(i[1])
    print(sum)

