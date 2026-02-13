# Returns a new list with only unique elements in order
def distinct_list(lst):
    unique = []
    for x in lst:
        if x not in unique:
            unique.append(x)
    return unique

nums = [1, 2, 2, 3, 1, 4]
print("Distinct elements:", distinct_list(nums))
