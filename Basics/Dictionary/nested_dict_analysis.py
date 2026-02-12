# Nested dictionary: student -> {subject: marks}
students = {
    "Alice": {"Math": 85, "Science": 90, "English": 78},
    "Bob": {"Math": 80, "Science": 85, "English": 88},
    "Charlie": {"Math": 92, "Science": 88, "English": 95}
}

# Initialize variables to track the top student and highest average
top_student = None
highest_avg = 0

# Loop through each student and their marks
for student, marks in students.items():
    # Calculate average marks for the student
    average = sum(marks.values()) / len(marks)
    
    # Update top student if current average is higher
    if average > highest_avg:
        highest_avg = average
        top_student = student

# Print the student with the highest average
print("Student with highest average marks:", top_student)

#marks is a dictionary, for example: {"Math": 85, "Science": 90, "English": 78}.
#marks.values() returns a view of all the values in the dictionary (i.e., [85, 90, 78])
#So sum(marks.values()) adds up all the marks in the dictionary to produce the total

#if average > highest_avg: checks if the current student's average is greater than the highest average seen before.
#If true:
#highest_avg = average updates the highest average to the current student's average.
#top_student = student updates the top student to the current student.