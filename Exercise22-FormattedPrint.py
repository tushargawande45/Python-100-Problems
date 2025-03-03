# Create a dictionary of keys a,b,c where each key has as value 
# a list from 1 to 10, 11 to 20, 21 to 30 respectively and print out.

from pprint import pprint

# d = {'a': [1,2,3,4,5,6,7,8,9,10],
#      'b': [11,12,13,14,15,16,17,18,19,20],
#      'c': [21,22,23,24,25,26,27,28,29,30]}
            # or
d = {"a": list(range(1,10)), "b": list(range(11,20)), "c": list(range(21,30))}
pprint(d)