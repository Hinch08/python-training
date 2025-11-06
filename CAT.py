my_string=str(input('enter your string:'))
def reverse_string(s):
    return s[::-1]
result=reverse_string(my_string)
print(result)

list=[1,2,3,4,5,6,7,8,9,10,11,12]
def even_numbers(list):
    even_list=[]
    for number in list:
        if number%2==0:
            even_list.append(number)
    return even_list
result=even_numbers(list)
print(result)

def squares():
    square_list=[]
    for number in range(1,31):
        square_list.append(number**2)
    print(square_list)
            
squares()






            