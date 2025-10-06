age_input = input()

# TODO: Your code here
total_age = 0
age_count = 0
average_age = 0
while age_input != 'done':
    age = str(input())
    total_age += age
    age_count += 1
    average_age = total_age / age_count


print(age_count)
print(total_age)
print(f"{average_age:.2f}")
