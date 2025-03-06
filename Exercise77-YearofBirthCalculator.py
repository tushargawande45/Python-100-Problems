# Question: Create a script that asks the user to enter their age, and the script calculates the user's year of birth and prints it out in a string like in the expected output. Please make sure you generate the current year dynamically.

# Expected output: 

# We think you were born back in 1988

from datetime import datetime
age = int(input("Enter your age: "))
# currentYear = int(datetime.now().strftime("%Y"))
currentYear = datetime.now().year
bornYear = currentYear - age 
print(f"We think your were born back in {bornYear}")