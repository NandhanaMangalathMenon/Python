import array

# Create your integer array
arr = array.array('i', [10, 20, 10, 30, 40, 20, 50, 30])

# Create a new array to store unique elements
unique_arr = array.array('i')

# Go through each element in the original array
for num in arr:
    if num not in unique_arr:
        unique_arr.append(num)   # Add only if not already present

print("Array with duplicates removed:", unique_arr)
