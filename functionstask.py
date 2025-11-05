base=float(input("Enter the base value: "))
height=float(input("Enter the height value: "))
def area_of_triangle(base,height):
    return 0.5*base*height
result=area_of_triangle(base,height)
print('result:',result)

#number=float(input('enter a number: '))
#def even_odd(number):
    ##if number%2==0:
        #return 'even'
    #else:
        #return 'odd'
#result=even_odd(number)
#print('The number is:',result)

#phone = input("Enter phone number: ").strip()
#def validate_phone(phone):
    #if phone.startswith("+254"):
        #phone = phone
    #elif phone.startswith("254"):
        #phone = "+" + phone
    #elif phone.startswith("0"):
        #phone = "+254" + phone[1:]
    #elif phone.startswith("7") or phone.startswith("1"):
        #phone = "+254" + phone
    #else:
        #phone = " Invalid phone number format."
    #return phone
#converted_number = validate_phone(phone)
#print("Converted Number:", converted_number)

#maths=int(input("Enter maths marks: "))
#eng=int(input("Enter english marks: "))
#kis=int(input("Enter kiswahili marks: "))
#sci=int(input("Enter science marks: "))
#sst=int(input("Enter social studies marks: "))
#def total_marks(maths,eng,kis,sci,sst):
    #return maths+eng+kis+sci+sst
#result=total_marks(maths,eng,kis,sci,sst)
#print("Total marks:",result)