score = float(input())

# TODO: Your code here
score_count = 0
total_score = 0
average_score = 0
while score <= 100.0 and score >=0.0:
    total_score += score
    score_count +=1
    score = float(input())
    average_score = total_score / score_count

print(score_count)
print(total_score)
print(f"{average_score:.2f}")
