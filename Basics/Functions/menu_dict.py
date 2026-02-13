# Menu dictionary
menu = {
    "burger": 5.99,
    "pizza": 8.99,
    "salad": 4.99
}

# 1. Show menu
def show_menu(menu):
    print("Menu:")
    for item, price in menu.items():           #.items() gives both key and value togeth
                                               #It returns pairs
                                               #for key, value in dictionary.items():

        print(item, ":", price)

        # burger : 5.99
        # pizza : 8.99
        # salad : 4.99


show_menu(menu)


# 2. Take order
def take_order():
    order = []
    n = int(input("How many items do you want to order? "))
    for i in range(n):
        item = input("Enter item name: ")
        order.append(item)
    return order

order = take_order()

# take_order is a function that takes input from the user
# It returns a list containing the items the user orders


# 3. Compute total bill
def compute_total(order, menu):
    total = 0
    for item in order:
        if item in menu:
            total += menu[item]
    return total

total = compute_total(order, menu)
print("Total bill:", total)

# Which items the customer ordered? → order
# How much each item costs? → menu
# SO 2 ARGUMENTS ARE TAKEN

# 4. Apply discount
def apply_discount(total):
    if total > 20:
        total = total * 0.9   # 10% discount
    return total

final_amount = apply_discount(total)
print("Final bill after discount:", final_amount)

