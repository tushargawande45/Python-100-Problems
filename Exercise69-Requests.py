# Question: Please create an empty file (manually as you normally create Python files) and name it requests.py . Make sure the file has that name exactly.

# Then paste the following code into the file:

# import requests
 
# headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
# r = requests.get("http://www.pythonhow.com", headers = headers)
# print(r.text[:100])
# Executing the script will throw an error. Please fix something to make the program print out the expected output. You should not modify the code itself, but something else.

# Expected output: 

# <!DOCTYPE html>
# <!--[if IE 7]>
# <html class="ie ie7" lang="en-US" prefix="og: http://ogp.me/ns#">


import requests
 
headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pythonhow.com", headers = headers)
print(r.text[:100])



# Answer: 
# Rename the file name from requests.py  to something else.

# Explanation:
# In the code, Python is actually referring to the script name, which is requests  And it doesn't find a get attribute for that name. 
# Script names load in the current namespace. T
# hey are actually stored in the __name__  variable. 
# You could try to print that variable out, and you would see that it prints your script name. 
# Therefore you should not name your scripts under library names. 