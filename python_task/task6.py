# Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. 
# If the password is correct access is granted. After you show them a message , the account is blocked.

correct_password = "admin@123"
attempts = 4

while attempts > 0:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Access granted.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong password. You have {attempts} attempts left.")
        else:
            print("You have used all your attempts. Account blocked.")
            break
