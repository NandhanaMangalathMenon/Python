#From an array of integers, searching for a given number using Linear Search.

arr = [5, 8, 12, 20]
key = 12

found = False #A flag variable,Initially set to False (not found).

for i in range(len(arr)): #Loop runs from index 0 to 3
    if arr[i] == key:
        print("Found at position", i)
        found = True
        break

if not found:
    print("Not Found")
