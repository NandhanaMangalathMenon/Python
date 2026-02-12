# Dictionary with names as keys and ages as values
people = {
    "Alice": 30,
    "Bob": 22,
    "Charlie": 27,
    "David": 24,
    "Eve": 29
}

# Loop through the dictionary items
for name, age in people.items():
    # Check if the person is older than 25
    if age > 25:
        print(name, "is older than 25")

#people.items() gives both name and age for each person.
#The loop goes through each name and age.
