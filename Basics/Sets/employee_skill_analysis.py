# Sets of employees trained in Python and Data Science
python_trained = {"Alice", "Bob", "Charlie", "David"}
data_science_trained = {"Charlie", "Eve", "Frank", "Bob"}

# Find employees trained in exactly one skill using symmetric_difference()
exclusive_skills = python_trained.symmetric_difference(data_science_trained)
#       x = a.symmetric_difference(b)
#symmetric_difference() finds elements that are in one set or the other, but not both.

# Display the employees with exclusive skills
print("Employees trained in exactly one skill:", exclusive_skills)
