# Question: Create an English to Portuguese translation program.

# The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. In addition, try to return the message, "We couldn't find that word!" when the user enters a word that is not in the dictionary.

# d = dict(weather = "clima", earth = "terra", rain = "chuva") 

# Expected output: 

# Enter word: hello
# That word doesn't exist!

# def translator(inputLang):
#     if inputLang in d:
#         print(d[inputLang])
#     else:
#         print("That word doesn't exist!")
    

# d = dict(weather = "clima", earth = "terra", rain = "chuva")
# inputLang = input("Enter word: ")
# translator(inputLang)

def translator(inputLang):
    try:
        return d[inputLang]
    except KeyError:
        return "That word doesn't exist!"

    else:
        print("That word doesn't exist!")
    

d = dict(weather = "clima", earth = "terra", rain = "chuva")
inputLang = input("Enter word: ")
print(translator(inputLang))