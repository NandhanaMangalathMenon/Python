# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for easy comparison
    s = s.replace(" ", "").lower()
    
    # Check if string is same as its reverse
    return s == s[::-1]


text = input("Enter a string: ")

if is_palindrome(text):
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is not a palindrome.")

#f"..."
#It allows you to insert variable values directly inside a string.
#EXAMPLE
#name = "Nand"
#print(f"Hello, {name}!")
