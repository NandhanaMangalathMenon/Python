import array

# Example sorted arrays for two branches (integer type array: 'i')
arr1 = array.array('i', [2, 4, 7, 10])
arr2 = array.array('i', [2, 3, 8, 13])

# New array for merged result
merged = array.array('i')

i = 0   # Pointer for arr1
j = 0   # Pointer for arr2

# Merge using two-pointer technique
while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:    # If arr1 value is less or equal, add it
        merged.append(arr1[i])
        i += 1
        #increment i to move to the next element of arr1.
    else:                    # Otherwise, add from arr2
        merged.append(arr2[j])
        j += 1
        # increment j to move to the next element of arr2

# Add any remaining elements from arr1
while i < len(arr1):
    merged.append(arr1[i])
    i += 1

# Add any remaining elements from arr2
while j < len(arr2):
    merged.append(arr2[j])
    j += 1

print("Merged sorted array:", merged)
