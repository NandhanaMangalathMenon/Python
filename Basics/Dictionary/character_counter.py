# Given word
word = "banana"

# Create an empty dictionary to store character counts
frequency = {}

# Loop through each character in the word
for char in word:
    if char in frequency:
        frequency[char] += 1  # If char already in dictionary, increment count
    else:
        frequency[char] = 1   # If char not in dictionary, add with count 1

# Print the frequency dictionary
print("Character frequency:", frequency)
