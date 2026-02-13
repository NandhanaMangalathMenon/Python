# Returns the sum of values in the list
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

marks = [10, 20, 30, 40]
print("Sum of marks:", sum_list(marks))
