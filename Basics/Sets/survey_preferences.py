# Sets of respondents who like Tea, Coffee, and Juice
tea_lovers = {"Alice", "Bob", "Charlie", "David"}
coffee_lovers = {"Bob", "Charlie", "Eve", "Frank"}
juice_lovers = {"Charlie", "David", "Eve", "Grace"}

# Respondents who like all three drinks (intersection)
all_three = tea_lovers.intersection(coffee_lovers, juice_lovers)

# Respondents who like only one drink (exclusive to one set)
only_tea = tea_lovers - coffee_lovers - juice_lovers
only_coffee = coffee_lovers - tea_lovers - juice_lovers
only_juice = juice_lovers - tea_lovers - coffee_lovers
only_one = only_tea.union(only_coffee).union(only_juice)

# Respondents who like at least two drinks
tea_coffee = tea_lovers.intersection(coffee_lovers)
coffee_juice = coffee_lovers.intersection(juice_lovers)
tea_juice = tea_lovers.intersection(juice_lovers)
at_least_two = tea_coffee.union(coffee_juice).union(tea_juice)

# Print results
print("Respondents who like all three drinks:", all_three)
print("Respondents who like only one drink:", only_one)
print("Respondents who like at least two drinks:", at_least_two)
