# Books currently checked out
checked_out = {"Book A", "Book B", "Book C"}

# Books that are reserved
reserved = {"Book C", "Book D", "Book E"}

print("Checked out books:", checked_out)
print("Reserved books:", reserved)

# 1. Currently unavailable books (checked out OR reserved)
print("\nCurrently unavailable books:")
print(checked_out | reserved)

# | = union
# Combines both sets
# Means: either checked out or reserved

# 2. Only reserved but not checked out
print("Only reserved but not checked out:")
print(reserved - checked_out)

# 3. Checked out by multiple members
member1 = {"Book A", "Book B"}
member2 = {"Book B", "Book C"}

print("Books checked out by multiple members:")
print(member1 & member2)
