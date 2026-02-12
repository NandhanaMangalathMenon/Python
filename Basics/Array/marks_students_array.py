import array

# Create an integer array for marks of students
#array.array('i', [...]) creates an array of integers ('i' means integer type)
marks = array.array('i', [85, 90, 78, 88, 92])

# Calculate the sum of marks
total = 0
for x in marks:
    total += x
    #After the loop finishes, total holds the sum of all marks

# Calculate average
average = total / len(marks)

print("Average marks:", average)
