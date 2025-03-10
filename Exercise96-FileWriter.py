# write a program that asks the user to submit text repeatedly
# the program closed when the user submits CLOSE 

file = open("user_data.txt","a+") 
while True:
    line = input("Enter a value: ")
    if line == "CLOSE":
        file.close()
        break
    else:
        file.write(line + "\n") 