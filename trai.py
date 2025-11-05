secret_password='admin@123'
number_of_attempts=3
while number_of_attempts>0:
    password=input('Enter your password:')
    if password==secret_password:
        print('Access granted.Welcome admin!')
        break
    else:
        number_of_attempts-=1
        print(f'Access denied.Invalid password.Try again.You have {number_of_attempts} attempts left.')
