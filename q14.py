while True:
    value1=input("Enter first number value: ")
    value2=input("Enter second number value: ")

    if value1.count('-')>1 or ('-'in value1[1:]):
        validity1=False
    elif value1.count('.')>1:
        validity1=False
    else:
        temp1=value1.replace('-','').replace('.','')
        validity1=temp1.isdigit()

    if value2.count('-')>1 or ('-'in value2[1:]):
        validity2=False
    elif value2.count('.')>1:
        validity2=False
    else:
        temp2=value2.replace('.','').replace('-','')
        validity2=temp2.isdigit()
    if validity1 and validity2:
        num1=float(value1)
        num2=float(value2)
        break
    sum=num1+num2
    print(f"The sum is {sum}")

else:
    print("Invalid input(s). Please enter numeric values.")

