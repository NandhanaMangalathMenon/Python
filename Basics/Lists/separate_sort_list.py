# Given list with mixed numbers and strings
mixed_list = [10, "apple", 5, "banana", 2, "cherry", 15, "date"]

# Create empty lists for numbers and strings
numbers = []
strings = []

# Separate numbers and strings
for item in mixed_list:
    if type(item) == int:
        numbers.append(item)  # Add numbers to numbers list
    elif type(item) == str:
        strings.append(item)  # Add strings to strings list

# Sort numbers in ascending order
numbers.sort()

# Sort strings alphabetically
strings.sort()

# Display the sorted lists
print("Sorted numbers:", numbers)
print("Sorted strings:", strings)
