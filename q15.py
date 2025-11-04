# Input basic details
basic_salary = float(input('Enter basic salary: '))
benefits = float(input('Enter your benefits: '))

# Gross salary
gross_salary = basic_salary + benefits

# NSSF (6% capped at 1080 for Tier II)
if gross_salary > 18000:
    NSSF = 1080
else:
    NSSF = 0.06 * gross_salary

# NHDF (1.5% of gross salary)
NHDF = 0.015 * gross_salary

# NHIF calculation by bracket
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

# Taxable income
taxable_income = gross_salary - (NSSF + NHDF)

# PAYE rates
if taxable_income > 800000:
    PAYEE = 0.35 * taxable_income
elif taxable_income > 467667:
    PAYEE = 0.30 * taxable_income
elif taxable_income > 32333:
    PAYEE = 0.25 * taxable_income
else:
    PAYEE = 0.10 * taxable_income

# Net salary
net_salary = gross_salary - (PAYEE + NSSF + NHDF + NHIF)


print("------ SALARY BREAKDOWN ------")
print(f"Gross Salary: {gross_salary}")
print(f"NSSF Deduction: {NSSF:.2f}")
print(f"NHDF Deduction: {NHDF:.2f}")
print(f"NHIF Deduction: {NHIF:.2f}")
print(f"PAYE: {PAYEE:.2f}")
print(f"Net Salary: {net_salary:.2f}")
