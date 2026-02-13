#Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
#Each number is the two numbers above it added together


# Function to print Pascal's Triangle
def print_pascals_triangle(n):
    for i in range(n):
        # start each row with 1
        num = 1
        # spacing for triangle shape
        print(" " * (n - i), end="")
        for j in range(i + 1):
            print(num, end=" ")
            # compute next number in row
            num = num * (i - j) // (j + 1)
        print()  # move to next line


rows = int(input("Enter number of rows: "))
print_pascals_triangle(rows)

