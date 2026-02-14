# Original sets
set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 4, 5, 6, 7, 8}

# Missing in set2 compared to set1
missing_in_set2 = set1 - set2

# Missing in set1 compared to set2
missing_in_set1 = set2 - set1

print("Original sets:")
print(set1)
print(set2)
print("Missing numbers in the second set as compared to the first:")
print(missing_in_set2)
print("Missing numbers in the first set as compared to the second:")
print(missing_in_set1)
