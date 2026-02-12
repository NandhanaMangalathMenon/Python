# Create an empty list to keep the marks
marks = []

# Use a loop to get marks for 5 students
for i in range(5):
    # Ask the user to enter a student's marks, and convert it to a number
    mark = int(input("Enter the marks of student " + str(i+1) + ": "))
    # Add the entered mark to the list
    marks.append(mark)

# Find the highest mark using the max() function
highest = max(marks)
# Find the lowest mark using the min() function
lowest = min(marks)

# Show the list of all marks
print("Marks entered: ", marks)
# Show the highest mark
print("Highest mark is:", highest)
# Show the lowest mark
print("Lowest mark is:", lowest)

#So if i = 0, the user sees:
#Enter the marks of student 1:
#If i = 1, they see:
#Enter the marks of student 2:
#So str(i+1) helps the program show the student number as text. 
#The str() function is needed because you can only join (add) text to other text; numbers need to be converted to strings to do this.
#i+1 just adds 1 to i. This is often done to make a count start from 1 (for humans), not 0 (which computers like).
