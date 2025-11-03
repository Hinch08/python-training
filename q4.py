#Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
#Hint: Check if it contains an “@” symbol and “.” symbol.
email_address=str(input('Enter your email here:'))

if "@"in email_address and ".":
    print('valid email')
else:
    print('invalid email address include @ or .')