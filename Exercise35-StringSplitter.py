# Question: Create a function that takes any string as input and returns the number of words for that string.

# def fun(str):
#     for letter in str:

def fun(str):
    a = str.split()
    words = len(a)
    return words

print(fun("Tushar is a Software Engineer"))


