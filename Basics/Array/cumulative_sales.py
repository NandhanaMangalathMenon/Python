import array

# Example sales amounts for several days
sales = array.array('i', [100, 200, 150, 300, 250])

# Create a new array for cumulative totals
cumulative_sales = array.array('i')
#creates an empty integer array using Python’s array module

# Variable to keep track of running total
total = 0

# Loop through each day's sales
for amount in sales:
    total += amount        # Add today's sales to running total
    cumulative_sales.append(total)  # Store the cumulative total for today

print("Cumulative sales array:", cumulative_sales)
