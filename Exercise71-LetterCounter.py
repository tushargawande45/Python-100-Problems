# Question: Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt

# Expected output: 

# 265


import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt")
print(response.text.count("a"))
