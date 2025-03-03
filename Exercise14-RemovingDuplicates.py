# Question: Complete the script so that it removes duplicate items from the list a .

# a = ["1", 1, "1", 2]
# Expected output: 

#   ['1', 2, 1]

# solution1:
# a = ["1", 1, "1", 2]
# b = set(a)
# print(list(b))

# solution2: preserved the order 
# from collections import OrderedDict
# a = ["1", 1, "1", 2]
# a = list(OrderedDict.fromkeys(a))
# print(a)

# solution3:
a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
