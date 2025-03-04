# Question: Create a script that generates a text file with all letters of the English alphabet inside it, one letter per line.

import string

def writeFile(filepath):
    with open(filepath,"w") as file:
        for letter in string.ascii_lowercase:
            file.write(letter + '\n')

print(writeFile("words3.txt"))