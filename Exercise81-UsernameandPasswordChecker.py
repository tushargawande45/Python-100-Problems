# Create a program that asks the user to enter a new password and check that the submitted password should contain :
# at least one number, 
# one uppercase letter,
# and at least 5 characters.
# If the conditions are met, print out the reason why pointing to the specific condition/s that has not been satisfied.
# Before asking for Password, ask for username.

while True:
    usr = input("Enter username: ")
    with open("users.txt","r") as file:
        users = file.readlines()
        users = [i.strip("\n") for i in users]
        if usr in users:
            print("username exists")
            continue
        else:
            print("username is fine")
            break
    
while True:
    password = input("Enter a password: ")

    has_digit = any(i.isdigit() for i in password)
    has_upper = any(i.isupper() for i in password)
    is_long_enough = len(password) >= 5

    if has_digit and has_upper and is_long_enough:
        print("Password is fine")
        break

    print("Password must:")
    if not has_digit:
        print("- Contain at least one digit")
    if not has_upper:
        print("- Contain at least one uppercase letter")
    if not is_long_enough:
        print("- Be at least 5 characters long")

        
