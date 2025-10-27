grade = float(input())

# TODO: Your code here\
valid_count = 1
while grade >= 0 and grade <= 100:
    valid_count += 1
    grade = float(input())
    total_grade += grade
    
average = total_grade / valid_count
print(valid_count)
print(f"{average:.2f}")
