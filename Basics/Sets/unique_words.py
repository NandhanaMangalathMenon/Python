# Given list of words
words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']

# Find unique words using set
unique_words = list(set(words))

# set(words) removes duplicates → {‘Red’, ‘Green’, ‘Blue’}
# Convert to list → ['Red', 'Green', 'Blue'] (order may vary)
#When you convert a list to a set using set(list_name), all duplicate elements are automatically removed.

# Count frequency of each word
freq = {} #empty set
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Unique Words:", unique_words)
print("Frequency of occurrence:", freq)
