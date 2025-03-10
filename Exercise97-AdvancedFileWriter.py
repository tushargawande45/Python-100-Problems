# write a program that asks the user to submit text repeatedly
# the program saves the changes when user submits SAVE, but doesn't close
# the program closed when the user submits CLOSE 

file = open("user_date_save_close.txt","a+")

while True:
    line = input("write a value: ")
    if line == "SAVE":
        file.close()
        file = open("user_date_save_close.txt","a+")
    elif line == "CLOSE":
        file.close()
        break
    else:
        file.write(line + "\n") 