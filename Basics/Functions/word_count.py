# Returns a dictionary of word frequencies in a string
def word_count(text):
    words = text.split()
    counts = {}  #Create an Empty Dictionary
    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return counts

sentence = "cat bat cat dog bat cat"
print("Word counts:", word_count(sentence))

#words = text.split()
#This line uses the .split() method to break the input string into a list of words.
# The default .split() method cuts wherever there's whitespace (spaces, tabs, etc.).
#For example, 'cat bat cat dog bat cat' becomes ["cat", "bat", "cat", "dog", "bat", "cat"].