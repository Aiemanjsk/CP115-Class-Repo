position = input()
overtime_hours = int(input())
is_weekend = input()

# Your code here
hourly_rate = 0

if position == 'Manager':
    hourly_rate = 35 + hourly_rate
elif position == 'Supervisor':
    hourly_rate = 25 + hourly_rate
elif position == 'staff':
    hourly_rate = 18 + hourly_rate


if is_weekend == 'true':
    weekend_bonus = 5 
else:
    weekend_bonus = 0

overtime_pay = (overtime_hours * hourly_rate * 1.5) + (overtime_hours * weekend_bonus)

total_pay = overtime_pay + weekend_bonus


print(hourly_rate)
print(overtime_pay)
print(total_pay)