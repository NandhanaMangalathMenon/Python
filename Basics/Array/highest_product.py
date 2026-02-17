# Program to find a pair with the highest product from a given array of integers.

import array

arr = array.array('i', [1, 10, -5, 1, -100])

# Creates an integer array
# 'i' → integer type

max_product = arr[0] * arr[1]

# Take first two elements
# Assume their product is the largest
# Here: 1 × 10 = 10
# This is just an initial assumption

pair1 = arr[0]   #Store the numbers that made the product
pair2 = arr[1]

for i in range(len(arr)):   #len(arr) → number of elements---i points to first number of pair
    for j in range(i + 1, len(arr)):
       # j points to second number of pair
       # Starts from i + 1 to avoid:
       # Repeating pairs
       # Same element multiplied by itself
       # Together, these two loops check ALL possible pairs
        
        product = arr[i] * arr[j]
        if product > max_product:
            max_product = product
            pair1 = arr[i]
            pair2 = arr[j]

print("Pair with highest product:", pair1, "and", pair2)
print("Highest product:", max_product)
