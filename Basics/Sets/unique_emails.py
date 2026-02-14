# List of emails (with duplicates)
emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com",
    "b@gmail.com"
]

print("Original email list:")
print(emails)

# Convert list to set to remove duplicates
unique_emails = set(emails)

#set() removes duplicate items automatically
#Sets never allow duplicates

print("\nUnique email addresses:")
print(unique_emails)
