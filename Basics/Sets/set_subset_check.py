# Define the sets
x = {'mango', 'apple'}
y = {'mango', 'orange'}
z = {'mango'}

print("x:", x)
print("y:", y)
print("z:", z)

# Check if x is subset of y
print("\nIf x is subset of y")
print(x <= y)    #Using comparison operator (<=)----Reads as: Is x a subset of y?
print(x.issubset(y))

# Check if y is subset of x
print("If y is subset of x")
print(y <= x)
print(y.issubset(x))

# Check if y is subset of z
print("If y is subset of z")
print(y <= z)
print(y.issubset(z))

# Check if z is subset of y
print("If z is subset of y")
print(z <= y)
print(z.issubset(y))
