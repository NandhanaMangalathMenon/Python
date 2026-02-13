# Checks if num falls between low and high (inclusive)
def in_range(num, low, high):
    return low <= num <= high
#This checks if num is greater than or equal to low AND less than or equal to high.

print("Is 7 between 5 and 10?", in_range(7, 5, 10))
print("Is 15 between 5 and 10?", in_range(15, 5, 10))
