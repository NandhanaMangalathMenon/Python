#Variable-Length Arguments:


# Function to calculate average of any number of scores
def average(*scores):
    total = sum(scores)           # Sum all scores
    count = len(scores)           # Count number of scores
    return total / count if count > 0 else 0   # Calculate and return average; avoid division by zero

# Calling the function with 3 arguments
avg1 = average(70, 85, 90)

# Calling the function with 5 arguments
avg2 = average(80, 75, 90, 85, 100)

# Calling the function with 7 arguments
avg3 = average(60, 70, 80, 90, 100, 85, 75)

# Printing the results
print("Average of 3 scores:", avg1)
print("Average of 5 scores:", avg2)
print("Average of 7 scores:", avg3)
