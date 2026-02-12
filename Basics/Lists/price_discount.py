prices = [500, 1200, 1500, 800, 2500, 950]

# Create a new list for updated prices
updated_prices = []

for x in prices:
    if x > 1000:
        # Apply 10% discount to price above 1000
        discounted_price = x* 0.9
        updated_prices.append(discounted_price)
    else:
        # Keep the original price if no discount
        updated_prices.append(x)

print("Updated prices after 10% discount:", updated_prices)

# Print the updated price list
print("Updated prices after 10% discount:", prices)

