# Question: Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt. Each file should contain a letter reflecting its filename. So, a.txt will contain letter a, b.txt will contain letter b, and so on.

import string

def func(filename):
    with open(f"letters/{filename}.txt","w") as file:
        file.write(f"{filename}")
        file.close()

for letter in string.ascii_lowercase:
    func(letter)
    

