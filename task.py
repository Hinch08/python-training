#my_string=str(input('Enter a string: '))
#def reverse_string(my_string):
    #reversed_string = "".join(reversed(my_string))#"".join(...) concatenates the characters yielded by the iterator into a new string,
    #using an empty string as the separator.
    #return reversed_string
#reversed_result=reverse_string(my_string)
#print(reversed_result)

list=[1,2,3,4,5,6,7,8,9,10,11,12]
def even_numbers(list):
    even_list=[]
    for number in list:
        if number%2==0:
            even_list.append(number)
    return even_list
result=even_numbers(list)
print(result)
            