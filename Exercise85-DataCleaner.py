# create a script that cleans the countries_raw.txt files from unnecessary lines and leaves countries only.

with open("countries_raw.txt", "r") as file:
    content = file.readlines()
print(content)

content = [i.strip("\n") for i in content if "\n" in i]
content = [i for i in content if i != ""]
content = [i for i in content if i != "Top of Page"]
content = [i for i in content if len(i) != 1]

with open("countries_clean.txt", "w") as file:
    for i in content:
        file.write(i + "\n")