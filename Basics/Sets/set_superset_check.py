# Check if a set is superset of itself
nums = {40, 10, 50, 20, 30}
print("Original set:", nums)
print("If nums is superset of itself?")
print(nums.issuperset(nums))  # Every set is always a superset of itself
#Returns True

# Check superset between two different sets
num1 = {1, 2, 3, 4, 5, 7}
num2 = {2, 4}
num3 = {2, 4}

print("num1 =", num1)
print("num2 =", num2)
print("num3 =", num3)

print("If num1 is superset of num2:")
print(num1.issuperset(num2))  # True

print("If num2 is superset of num3:")
print(num2.issuperset(num3))  # True, actually since sets are equal

print("If num3 is superset of num2:")
print(num3.issuperset(num2))  # True, actually since sets are equal
