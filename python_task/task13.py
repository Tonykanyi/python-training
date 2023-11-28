# Write a program that takes the email and password as input from a user
# and checks if they are equal to “admin@mail.com” and password is “Admin@123” , 
# if so then print  “Login is Successful” and if not print “Invalid username or password”. 
# ONLY accept 3 tries after which it notifies you that you have been blocked.

email=input("enter your email: ")
password=input("enter your password: ")
correct_password="Admin@123"
correct_email="admin@mail.com"
max_attempts = 3
attempts_left = max_attempts

while attempts_left > 0:
    user_email = input("Enter your email: ")
    user_password = input("Enter your password: ")

    if user_email == correct_email and user_password == correct_password:
        print("Login is Successful.")
        break
    else:
        attempts_left -= 1
        print(f"Invalid username or password. {attempts_left} attempts left.")

if attempts_left == 0:
    print("You have been blocked. Too many incorrect attempts.")
