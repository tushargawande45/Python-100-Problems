# Question: Filter the dictionary by removing all items with a value of greater than 1.

# d = {"a": 1, "b": 2, "c": 3}
# Expected output: 
# {'a': 1}  

d = {"a": 1, "b": 2, "c": 3}
keys_to_remove = [key for key in d if d[key]>1]

for key in keys_to_remove:
        d.pop(key)
print(d)