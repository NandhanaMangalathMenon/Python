# Returns a reversed version of the string
def reverse_str(s):
    result = ''    #Empty Result String--to build up the reversed string character by character
    for char in s:  # This loop will go through every character (char) in the original string s, from left to right.
        result = char + result
    return result

word = "hello"
print("Reverse of 'hello':", reverse_str(word))

#This line defines a function named reverse_str that takes one argument (s).
#What is s? It's expected to be a string, like 'hello'

#  result = char + result
# This line takes the character from the loop (char) and puts it in front of what's already in result.

#How does this reverse the string?
#On first pass: result = 'h' + '' = 'h'
#Next: result = 'e' + 'h' = 'eh'
#Next: result = 'l' + 'eh' = 'leh'
#Continue: result = 'l' + 'leh' = 'lleh'
#Last: result = 'o' + 'lleh' = 'olleh'