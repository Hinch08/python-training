#Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
#The goal of this exercise is to think about some internals that programs normally take care of for us. 
phone_number=int(input("Enter your phone number here:"))
password=int(input('enter your password here:'))
confirm_password=int(input('enter your confirmed password:'))

print(f"Your phone number is:{phone_number}")
print(f"your password is:{password}")
print(f"your confirmed password is:{confirm_password}")
print(len(f"{password}"))
print(len(f"{confirm_password}"))

if confirm_password>password:
    print('Error!! confirmed password is longer than password')
else:
    print('password is correct')