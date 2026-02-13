# Function to check if a string is a pangram
def is_pangram(s):
    # convert to lowercase
    s = s.lower()
    
    # check for every letter from 'a' to 'z'
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        if ch not in s:
            return False
    return True


# --- Main Program ---
text = input("Enter a sentence: ")

if is_pangram(text):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")
