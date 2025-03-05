# Write a script that extract letters from the 26 text files and put the letters in a list

import glob

letters = []
file_list = glob.glob("letters/*.txt")

for filename in sorted(file_list):
    with open(filename,"r") as file:
        letters.append(file.read().strip("\n"))

print(letters)