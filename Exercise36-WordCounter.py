# Question: Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input and returns the number of words contained in the text file.

# Expected output:

# 10 

f = open("words1.txt", "r")

def count_words(filepath):
    with open(filepath,'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)
    
print(count_words("words1.txt"))
