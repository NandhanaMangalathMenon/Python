# Dictionary with employee salaries
salaries = {
    "Alice": 28000,
    "Bob": 32000,
    "Charlie": 25000,
    "David": 40000,
    "Eve": 29000
}

# Loop through dictionary keys to update salaries
for employee in salaries:
    if salaries[employee] < 30000:
        # Increase salary by 10%
        salaries[employee] = salaries[employee] * 1.10

# Print the updated salaries
print("Updated salaries:", salaries)
