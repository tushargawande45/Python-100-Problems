# Question: Create an English to Portuguese translation program.

# The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

# d = dict(weather = "clima", earth = "terra", rain = "chuva") 

# Expected output: 

# Enter word: earth
# terra


def translator(inputLang):
    print(d[f"{inputLang}"])

d = dict(weather = "clima", earth = "terra", rain = "chuva")
inputLang = input("Enter word: ")
translator(inputLang)
