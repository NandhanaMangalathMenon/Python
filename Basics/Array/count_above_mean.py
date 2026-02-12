import array

# Create an integer array
marks = array.array('i', [85, 90, 78, 88, 92])

# Calculate the mean
mean = sum(marks) / len(marks)

# Count how many elements are greater than the mean
count = 0
for mark in marks:
    if mark > mean:
        count += 1

print("Number of elements greater than mean:", count)

#arr = [10, 20, 30, 40, 50]
#mean_val = sum(arr) / len(arr)
#count = 0
#for num in arr:
   # if num > mean_val:
       # count += 1
#print("Number of elements greater than the mean:", count)
