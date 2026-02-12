# Given list of city names
cities = ["Chicago", "Boston", "Cairo", "Calcutta", "Delhi", "Chennai", "Canberra"]

# Create an empty list to store cities starting with 'C' and longer than 5 characters
c_cities = []

# Loop through each city in the list
for x in cities:
    # Check if city starts with 'C' and length is greater than 5
    if x.startswith("C") and len(x) > 5:
        # Add city to the new list
        c_cities.append(x)

# Print the new list of cities
print("Cities starting with 'C' and longer than 5 characters:", c_cities)
