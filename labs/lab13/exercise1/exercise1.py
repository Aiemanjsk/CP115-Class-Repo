correct_password = "python123"

# TODO: Your code here
attempts_used = 0
while attempts_used >= 3:
    attempts_used += 1
    if correct_password == "python123":
        login_successful = "you have succesfull entered"

print(login_successful)
print(attempts_used)
