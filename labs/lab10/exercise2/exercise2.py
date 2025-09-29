age = int(input())
accident_count = int(input())

# Your code here
base_premium = 0
if age < 25 :
    base_premium = base_premium + 2400
elif age < 50:
    base_premium = base_premium + 1800
else :
    base_premium = base_premium + 2000
accident_penalty = 0 
discount = 0
if accident_count == 0:
    accident_penalty = accident_penalty + 0
    discount = discount + 1-10/100
elif accident_count <= 2:
    accident_penalty = accident_penalty + 300
    discount = discount
else :
    accident_penalty = accident_penalty + 600
    discount = discount
final_premium = accident_penalty + base_premium
discount_amount = discount * final_premium


print(base_premium)
print(final_premium)
print(discount_amount)