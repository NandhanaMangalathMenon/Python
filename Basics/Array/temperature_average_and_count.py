# This program calculates the average temperature and counts how many days had temperatures above the average.

import array

temps = array.array('i', [30, 32, 31, 29, 35, 28, 34])

total = 0
count = len(temps)

for t in temps:
    total = total + t

average = total / count

above_avg_days = 0

for t in temps:
    if t > average:
        above_avg_days = above_avg_days + 1

print("Average temperature:", average)
print("Days above average:", above_avg_days)
