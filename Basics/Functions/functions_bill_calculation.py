#Default and KeywordArguments:


# Define the function with default values for tax and discount
def calculate_bill(amount, tax=5, discount=0):
    taxed_amount = amount + (amount * tax / 100)  # Add tax percentage to amount
    final_amount = taxed_amount - discount        # Subtract discount
    return final_amount

# Function calls using positional arguments
bill1 = calculate_bill(1000)               # Only amount, uses default tax (5%) and discount (0)
bill2 = calculate_bill(1000, 10, 50)       # All values provided

# Function calls using keyword arguments
bill3 = calculate_bill(amount=5000, discount=250, tax=8)
bill4 = calculate_bill(amount=2500, discount=100)  # Uses default tax
bill5 = calculate_bill(tax=15, amount=1200)        # Arguments out of order using keywords

# Print results
print("Bill 1:", bill1)
print("Bill 2:", bill2)
print("Bill 3:", bill3)
print("Bill 4:", bill4)
print("Bill 5:", bill5)
