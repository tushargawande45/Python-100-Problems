# Question: The code produces an error. Please understand the error and try to fix it

# age = input("What's your age? ")
# age_last_year = age - 1
# print("Last year you were %s." % age_last_year)

# solution: we applied an int  function to the input  function. That converts user input to an integer right away.

age = int(input("What's your age? "))
age_last_year = age - 1
print("Last year you were %s." % age_last_year)
