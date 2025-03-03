# Question: Calculate the sum of all dictionary values.

# d = {"a": 1, "b": 2, "c": 3}
# Expected output: 
#  6 

# solution1:
# d = {"a": 1, "b": 2, "c": 3}
# sum = 0
# for i in d:
#     sum = sum + d[i]
# print(sum)

# solution2:
d = {"a": 1, "b": 2, "c": 3}
print(sum(d.values()))