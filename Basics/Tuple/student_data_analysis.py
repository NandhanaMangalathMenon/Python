# Tuple of nested tuples: (name, age, marks)
students = (
    ("Alice", 19, 85),
    ("Bob", 21, 78),
    ("Charlie", 18, 92),
    ("David", 20, 81),
    ("Eve", 17, 75)
)

# Loop through each student tuple
for x in students:
    name, age, marks = x # Unpack the nested tuple

    # Check if marks are above 80 and age is less than 20
    if marks > 80 and age < 20:
        print(name)
