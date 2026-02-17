#program to reverse the order of the items in the array using loops only.

import array

arr = array.array('i', [1, 2, 3, 4, 5])

n = len(arr)

for i in range(n // 2):
  # Loop runs only half the array
  # Why?
  # First element swaps with last
  # Second swaps with second last
  # Middle element stays same (if any)
  # n // 2 ensures no extra swapping

  #Iteration 1 (i = 0)
  #Swap arr[0] and arr[4]------[5, 2, 3, 4, 1]

#   Iteration 2 (i = 1)
#   Swap arr[1] and arr[3]------[5, 4, 3, 2, 1]

#Loop stops (middle element 3 stays same)




    temp = arr[i]
    # Stores the left element temporarily
    # Needed because value will be overwritten

    #WHY TEMP??
    #Because Python cannot swap two values directly without losing one
    #So we use a temporary variable (temp) as a safe box.

    arr[i] = arr[n - i - 1] #Copies right element to left position
    arr[n - i - 1] = temp

print("Reversed array:", arr)
