# Question: Please download the file in the attachment and use Python to print out its content.

# Expected output: 

# {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
#                {'firstName': 'Anna', 'lastName': 'Smith'},
#                {'firstName': 'Peter', 'lastName': 'Jones'}],
#  'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#             {'firstName': 'Jessy', 'lastName': 'Petter'}]}
from pprint import pprint
import json

with open("company1.jason","r") as file:
    d = json.loads(file.read())
    
    
pprint(d)

