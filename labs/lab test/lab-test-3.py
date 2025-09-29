bill_payment_per_month = float(input("enter your bill payment per month: "))

#discount in percentage rate
if bill_payment_per_month < 50:
    discount = 0
elif bill_payment_per_month <= 100:
    discount = 5/100
else:
    discount = 20/100

#count with the actual discount
bill_amount = bill_payment_per_month - (bill_payment_per_month * discount)

print ("your bill amount is: " + str(bill_amount))