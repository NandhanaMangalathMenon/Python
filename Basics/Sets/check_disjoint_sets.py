# Original sets
x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}

print("Original set elements:")
print("x =", x)
print("y =", y)
print("z =", z)

# Check if two sets have no elements in common
print("Confirm two given sets have no element(s) in common:")

print("Compare x and y:")
print(x.isdisjoint(y))  # False, because 4 is common

print("Compare x and z:")
print(x.isdisjoint(z))  # True, no common elements

print("Compare y and z:")
print(y.isdisjoint(z))  # True, no common elements


# set1.isdisjoint(set2) returns:

# True → if no elements are common
# False → if there is at least one common element