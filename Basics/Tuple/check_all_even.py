# Given tuple of 10 integers
numbers = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

# Assume all numbers are even at the start
all_even = True

# Loop through each number in the tuple
for num in numbers:
    # Check if the number is NOT even
    if num % 2 != 0:
        all_even = False  # Found an odd number
        break             # No need to check further

# Print the result
if all_even:
    print("All numbers are even.")
else:
    print("Not all numbers are even.")
