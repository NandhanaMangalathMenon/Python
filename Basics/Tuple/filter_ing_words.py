# Given tuple of words
words = ("running", "jump", "swimming", "dance", "singing", "walk")

# Create an empty list to store words with 'ing'
ing_words = []

# Loop through each word in the tuple
for x in words:
    if "ing" in x:  # Check if 'ing' is in the word
        ing_words.append(x)  # Add word to list

# Convert the list back to a tuple
new_tuple = tuple(ing_words)

# Print the new tuple
print("Words containing 'ing':", new_tuple)
