# Inventory dictionary
inventory = {
    "apple": {"price": 0.5, "stock": 30},
    "banana": {"price": 0.3, "stock": 50}
}

# 1. Add new item
def add_item(inventory, name, price, stock):
    inventory[name] = {"price": price, "stock": stock}

add_item(inventory, "orange", 0.4, 20)


# 2. Update stock after sale
def sell_item(inventory, name, quantity):
    inventory[name]["stock"] = inventory[name]["stock"] - quantity

sell_item(inventory, "apple", 5)


# 3. Display total inventory value
def total_inventory_value(inventory):
    total = 0
    for item in inventory:
        total = total + inventory[item]["price"] * inventory[item]["stock"]
    return total

print("Total inventory value:", total_inventory_value(inventory))

