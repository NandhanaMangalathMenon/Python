# This program checks customer orders against available stock and separates fulfillable and out-of-stock orders.

import array

# Product IDs ordered
orders = array.array('i', [101, 102, 103, 104, 105])

# Product IDs in stock
stock = array.array('i', [102, 104, 106, 101])

# List to store fulfillable orders
fulfillable = array.array('i')

# Check each order
for order in orders:
    if order in stock:
        fulfillable.append(order)

# Orders that cannot be fulfilled
out_of_stock = array.array('i')
for order in orders:
    if order not in stock:
        out_of_stock.append(order)

print("Fulfillable orders:", fulfillable)
print("Out of stock orders:", out_of_stock)
