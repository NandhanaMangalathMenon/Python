# Expense dictionary
expenses = {
    "2025-10-30": {"food": 12.5, "transport": 5.0},
    "2025-10-31": {"food": 20.0, "entertainment": 15.0},
    "2025-11-01": {"transport": 10.0, "shopping": 50.0}
}

# 1. Add an expense
def add_expense(expenses, date, category, amount):
    if date not in expenses:
        expenses[date] = {} #empty dictionary #Creates a new date if it doesn’t exist
    expenses[date][category] = amount
    print("Expense added")
#REASON FOR 4 ARGUMENTS

# | Argument | Why needed           |
# | -------- | -------------------- |
# | expenses | where data is stored |
# | date     | which day            |
# | category | what type of expense |
# | amount   | how much spent       |

#IF A PARTICULAR DAT EI SNOT NOT THERE, THEN THAT MUST BE ADDED
#expenses["2025-11-02"]====== expenses[date] = {}
#WHEN EMPTY DICTIONARY FOR THE NEW DATE IS CREATED
#expenses = {
#   "2025-11-02": {}
# }
#expenses[date][category] = amount-----MEANS WE ALREADY CREATED AN EMPTY DICTIONARY...
#NOW WE ARE GOING INSIDE THE EMPTY DATE DICTIONARY CREATED
#So [date][category] means:
#dictionary → date → category → amount



add_expense(expenses, "2025-11-02", "food", 18.0)


# 2. Get total expenses for a day
def total_for_day(expenses, date):
    if date in expenses:
        return sum(expenses[date].values())
    return 0       #If the date is not present in expenses
                   # That means no money spent that day
                   # So total = 0

print("Total on 2025-10-30:", total_for_day(expenses, "2025-10-30")) #function call

# .values()----It extracts only the values, not keys.
#{"food": 12.5, "transport": 5.0}
#gives--[12.5, 5.0]

# 3. Get total expenses by category
def total_by_category(expenses, category):
    total = 0    #We are going to add amounts step by step
    for day in expenses:
        if category in expenses[day]: #“Did we spend money on this category on this day?”
            total += expenses[day][category] 
    return total

print("Total food expense:", total_by_category(expenses, "food"))
