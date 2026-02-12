# Example: 7 days of temperatures
temps = [28, 32, 31, 26, 34, 29, 30]
# Set the counter to zero
count = 0

# Go through each temperature in the list
for x in temps:
    # If the temperature is above 30°C, add 1 to the count
    if x > 30:
        count += 1

# Show the result
print("Number of days above 30°C:", count)
