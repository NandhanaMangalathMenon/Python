# Program to find the largest and smallest elements in an array without using max() or min(),

arr = [5, 2, 9, 1, 7]

largest = arr[0]   #Assume first element is both largest and smallest
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest element:", largest)
print("Smallest element:", smallest)

#CODE TRACING

# | i (current) | largest | smallest | What happens            |
# | ----------- | ------- | -------- | ----------------------- |
# | 5           | 5       | 5        | No change               |
# | 2           | 5       | **2**    | 2 < 5 → update smallest |
# | 9           | **9**   | 2        | 9 > 5 → update largest  |
# | 1           | 9       | **1**    | 1 < 2 → update smallest |
# | 7           | 9       | 1        | No change               |

# We start with a valid element
# We check every element
# Whenever we find something bigger → update largest
# Whenever we find something smaller → update smallest