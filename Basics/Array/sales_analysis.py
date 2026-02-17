# This program analyzes daily sales data to calculate total sales, find the highest sales day, and compute percentage growth between consecutive days.

import array

sales = array.array('i', [100, 120, 150, 130, 180]) #Each value represents sales of each day

# Day 1 → 100
# Day 2 → 120
# Day 3 → 150
# Day 4 → 130
# Day 5 → 180

# 1. Total sales
total = 0
for s in sales:
    total = total + s

# 2. Day with highest sale
max_sale = sales[0]  #ASSUMPTION,,looping will update it
day = 1

# Assume first day has highest sale
# day = 1 because index starts from 0

for i in range(len(sales)):
    if sales[i] > max_sale:
        max_sale = sales[i]
        day = i + 1

# 3. Percentage growth between consecutive days
#Percentage growth =
#(Current day − Previous day) / Previous day × 100

print("Percentage growth between days:")
for i in range(1, len(sales)):
    # Starts from day 2
    # Because we compare with previous day

    growth = ((sales[i] - sales[i - 1]) / sales[i - 1]) * 100
    print("Day", i, "to Day", i + 1, ":", growth, "%")

print("Total sales:", total)
print("Highest sale:", max_sale)
print("Day with highest sale:", day)
