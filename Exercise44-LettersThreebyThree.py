# Question: Create a script that generates a file where all letters of the English alphabet are listed three in each line. The inside of the text file would look like:

# abc
# def
# ghi

# and so on.

import string
with open("words5.txt","w") as file:
    for letter1,letter2,letter3 in zip(string.ascii_lowercase[0::3],string.ascii_lowercase[1::3],string.ascii_letters[2::3]):
        file.write(letter1 + letter2 + letter3 + "\n")