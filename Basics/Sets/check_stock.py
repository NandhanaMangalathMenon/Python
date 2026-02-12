# Set of items in stock
stock_items = {"apple", "banana", "orange", "mango", "grapes"}

# Ask user to enter the requested item
requested_item = input("Enter the item you want: ").lower()
#.lower() converts the input to lowercase to match the stock items format.

# Check if the requested item is in stock
if requested_item in stock_items:
    print(requested_item, "is available in stock.")
else:
    print(requested_item, "is not available in stock.")
