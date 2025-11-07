#base=(input("Enter the base value: "))
#height=float(input("Enter the height value: "))
#def area_of_triangle(base,height):
    #return 0.5*base*height
#result=area_of_triangle(base,height)
#print('result:',result)

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
print('------------------SALARY CALCULATION PROGRAMME-------------------------------------')
basic_salary = float(input('Enter basic salary: '))
benefits = float(input('Enter benefits: '))

def calculate_gross_salary(basic_salary, benefits):
    return basic_salary + benefits
result=gross_salary=calculate_gross_salary(basic_salary, benefits)

def calculate_nssf(gross_salary):
    if gross_salary > 18000:
        NSSF = 1080
    else:
        NSSF = 0.06 * gross_salary
    return NSSF
NSSF = calculate_nssf(gross_salary)

def calculate_nhif(gross_salary):
    if gross_salary > 100000:
        NHIF = 1700
    elif gross_salary > 90000:
        NHIF = 1600
    elif gross_salary > 80000:  
        NHIF = 1500
    elif gross_salary > 70000:
        NHIF = 1400
    elif gross_salary > 60000:
        NHIF = 1300
    elif gross_salary > 50000:
        NHIF = 1200
    elif gross_salary > 45000:
        NHIF = 1100
    elif gross_salary > 40000:
        NHIF = 1000
    elif gross_salary > 35000:
        NHIF = 950
    elif gross_salary > 30000:
        NHIF = 900
    elif gross_salary > 25000:
        NHIF = 850
    elif gross_salary > 20000:
        NHIF = 750
    elif gross_salary > 15000:
        NHIF = 600
    elif gross_salary > 12000:
        NHIF = 500
    elif gross_salary > 8000:
        NHIF = 400
    elif gross_salary > 6000:
        NHIF = 300
    else:
        NHIF = 150
    return NHIF
NHIF = calculate_nhif(gross_salary)
NHDF = 0.015 * gross_salary 

taxable_income = gross_salary - (NSSF + NHDF)
def calculate_payee(taxable_income):
    if taxable_income > 800000:
        PAYEE = 0.35 * taxable_income
    elif taxable_income > 467667:
        PAYEE = 0.30 * taxable_income
    elif taxable_income > 32333:
        PAYEE = 0.25 * taxable_income
    elif taxable_income > 24000:
        PAYEE = 0.20 * taxable_income
    elif taxable_income > 12298:
        PAYEE = 0.15 * taxable_income
    else:
        PAYEE = 0.10 * taxable_income
    return PAYEE
PAYEE = calculate_payee(taxable_income)
net_salary = gross_salary - (PAYEE + NSSF + NHDF + NHIF)
print("Net Salary:", net_salary)
print("------ SALARY BREAKDOWN ------")
print(f"Gross Salary: {gross_salary}")
print(f"NSSF Deduction: {NSSF}")
print(f"NHIF Deduction: {NHIF}")
print(f"NHDF Deduction: {NHDF:.2f}")
