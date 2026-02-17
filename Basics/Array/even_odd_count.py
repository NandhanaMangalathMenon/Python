#Program to count the number of even and odd from a given array of integers

import array

arr = array.array('i', [1, 2, 3, 4, 5, 6])

even_count = 0
odd_count = 0

for i in arr:
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
