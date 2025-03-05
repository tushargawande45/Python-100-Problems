# write a script that iterates through each of the 26 text files, check if the letter inside the text file is in string "python" and put the letter in a list if the letter is a character of "python"

import glob

letters = []
targeted_str = "python"
file_list = sorted(glob.glob("letters/*.txt"))

for filepath in file_list:
    with open(filepath,"r") as file:
        letter = file.read().strip("\n")
        if letter in targeted_str:
            letters.append(letter)

print(letters)