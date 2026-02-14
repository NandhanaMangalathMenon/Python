# Set of forbidden characters
forbidden_chars = {' ', '!', '@', '#', '$'}

# Password entered by user
password = "my@pass word"

print("Password:", password)
print("Forbidden characters:", forbidden_chars)

# Convert password string into a set of characters
password_chars = set(password)

#Breaks password into individual characters
#Removes duplicates automatically
#"my@pass word" → {'m', 'y', '@', ' ', 'p', 'a', 's', 'w', 'o', 'r', 'd'}


# 1. Check if password contains any forbidden characters
if password_chars & forbidden_chars:
    print("\nPassword contains forbidden characters")

    #   &---- finds common characters
    #If result is not empty, password is invalid

    # 2. Display which characters are invalid
    print("Invalid characters found:")
    print(password_chars & forbidden_chars)
else:
    print("\nPassword does not contain any forbidden characters")
