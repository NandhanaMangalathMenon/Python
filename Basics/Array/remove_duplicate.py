#Program to removes all duplicate elements from an array and return a new array.

import array

arr = array.array('i', [1, 2, 2, 3, 4, 4, 5])

new_arr = array.array('i')

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print("Array after removing duplicates:", new_arr)
