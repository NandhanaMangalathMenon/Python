# Given tuple of daily profits for 7 days
profits = (200, 300, 250, 400, 150, 100, 350)

# Calculate total profit using sum()
total_profit = sum(profits)

# Calculate average profit
average_profit = total_profit / len(profits)

# Create a list to store days with below average profit
below_average_days = []

# Loop through the tuple using index to find below average days
#Since you want to find days by index when profit is below average, you need the index numbers.
#Range is always a number, so we give len(profits) which is 7
for i in range(len(profits)):
    if profits[i] < average_profit:
        below_average_days.append(i)

# Print the total profit
print("Total profit:", total_profit)

# Print the average profit
print("Average profit:", average_profit)

# Print the days (indexes) with below average profit
print("Days with below average profit:", below_average_days)

#With for i in range(len(profits)): → i is an index, so profits[i] is the value.
#You must write if profits[i] < average_profit: to compare the profit value.
#Writing if i < average_profit: compares the index i (0, 1, 2...) with average profit, which is wrong.