correct_password = "python123"

# TODO: Your code here
login_successful = ''
attempts_used = 0
while attempts_used >= 3:
    attempts_used += 1
    if correct_password == "python123":
        login_successful = True

print(login_successful)
print(attempts_used)
