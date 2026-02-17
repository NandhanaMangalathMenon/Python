# This program cleans sensor readings by replacing invalid values (less than 0 or greater than 100) with nearby valid averages.

import array

readings = array.array('i', [10, 20, 150, 30, -5, 50, 70])

# Make a copy to store modified readings
cleaned = array.array('i', readings)

for i in range(len(readings)):
    if readings[i] < 0 or readings[i] > 100:
        if i == 0:
            # First element, only use next neighbor
            cleaned[i] = readings[i + 1]
        elif i == len(readings) - 1:
            # Last element, only use previous neighbor
            cleaned[i] = readings[i - 1]
        else:
            # Use average of previous and next elements
            cleaned[i] = (readings[i - 1] + readings[i + 1]) // 2

print("Original readings:", readings)
print("Cleaned readings: ", cleaned)
