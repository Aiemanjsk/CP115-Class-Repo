employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
total_income = base_salary * overtime_hours
if(tax_status = single) and (total_income >= 5000):
    tax_rate = 22/100
elif(tax_status = single) and (total_income < 5000):
    tax_rate = 18/100
elif(tax_rate = married) and (total_income >= 6000):
    tax_rate = 20/100
net_salary = tax_rate * (total_income - (0.115 * total_income))
print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")