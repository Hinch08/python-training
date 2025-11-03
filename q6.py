#Write a program that lets the user input a password. 
# Give them only 4 attempts to check the passwords entered against “admin@123”.
#  If the password is correct access is granted. 
# After you show them a message , the account is blocked.
secret_password='admin@123'
max_attempts=4
attempts=0

while attempts<max_attempts:
    user_input=input('enter your password:')
    if secret_password==user_input:
        print('Access granted')
    else:
        attempts+=1
        remaining_attempts=max_attempts-attempts
        if remaining_attempts>0:
            print(f"password incorrect,you have remaining attempts{remaining_attempts}")
        else:
            print('incorrect password.zero attempts left,try again later')
if attempts==max_attempts and user_input != secret_password:
    print('Too many attempts,Account blocked!')            
