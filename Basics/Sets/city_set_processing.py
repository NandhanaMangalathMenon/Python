# Given set of city names
cities = {"Paris", "Rome", "Delhi", "Oslo", "Tokyo", "Berlin"}

# Create an empty set to store cities with 5 or more letters
filtered_cities = set()

# Loop through each city in the original set
for x in cities:
    # Check if the city name has 5 or more letters
    if len(x) >= 5:
        # Add the city to the filtered set
        filtered_cities.add(x)

# Print the filtered cities
print("Cities with 5 or more letters:", filtered_cities)
