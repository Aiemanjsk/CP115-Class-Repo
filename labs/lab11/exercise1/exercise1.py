num_rounds = int(input())

# TODO: Your code here
# Use input() inside the loop to get each round's score
final_score = 0
rounds_processed = 0
for rounds_processed in range (0,num_rounds-1):
    points = float(input())
    bonus = 20/100
    if points > 100:
        points = (points * bonus) + points
    else:
        points = points

    final_score += points

print(f"{final_score:.1f}")
print(rounds_processed)