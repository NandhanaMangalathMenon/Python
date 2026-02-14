# Guests who RSVP'd for dinner
dinner_guests = {'Alice', 'Bob', 'Charlie', 'David'}

# Guests who RSVP'd for afterparty
afterparty_guests = {'Charlie', 'David', 'Eve', 'Frank'}

print("Dinner guests:", dinner_guests)
print("Afterparty guests:", afterparty_guests)

# 1. People attending both events
print("\nPeople attending both events:")
print(dinner_guests & afterparty_guests)

# 2. People attending only dinner
print("People attending only dinner:")
print(dinner_guests - afterparty_guests)

# 3. People attending only the afterparty
print("People attending only the afterparty:")
print(afterparty_guests - dinner_guests)

# 4. Total unique guests
print("Total unique guests:")
print(dinner_guests | afterparty_guests)

#| means combine both
#No duplicates (because it’s a set)
