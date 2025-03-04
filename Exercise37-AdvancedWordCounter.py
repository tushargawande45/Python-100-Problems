# Question: Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that a comma can separate some words with no space. For example, "Hi, it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment.

def count_words(filepath):
    with open(filepath,'r') as file:
        strng = file.readline()
        text = strng.replace(","," ")
        strng_words = text.split(" ")
        return len(strng_words)
    
print(count_words("words2.txt"))