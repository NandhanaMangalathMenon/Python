#Finding the position of number 7 in the sorted list [1, 3, 5, 7, 9]
#BINARY SEARCHING

nums = [1, 3, 5, 7, 9]  #nums → this is a sorted list of numbers
target = 7

left = 0  #left → starting index of the list (0)
right = 4  #right → last index of the list (4)

while left <= right:
    mid = (left + right) // 2  #// means integer division

    if nums[mid] == target:  #Check if the middle element is the number we want
        print("Found at index", mid)
        break   #break stops the loop because search is complete
    elif nums[mid] < target:
        left = mid + 1
        #If middle number is smaller than target,The target must be on the right side
    else:
        right = mid - 1
#WHY WE USE WHILE LOOP
#Because we don’t know in advance how many times we need to check the middle.

#nums = [1, 3, 5, 7, 9]
#index:  0  1  2  3  4

#3 is at index 1
#5 is at index 2
#Since 1 < 2
# 3 is to the left of 5

# while left <= right:
# left = 0
# right = 4

# mid = (0 + 4) // 2 = 2 → nums[2] = 5
# 7 > 5 → go right

#UPDATE
# left = 3
# right = 4
# NOW RANGE--[7, 9]
# mid = (3 + 4) // 2 = 3 → nums[3] = 7

#Square brackets [] are used to access an element in a list by index.
# nums[mid]
#nums = [10, 20, 30]
#nums[0]  → 10
#nums[1]  → 20




