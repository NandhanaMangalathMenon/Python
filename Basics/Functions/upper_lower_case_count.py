# Counts uppercase and lowercase letters in a string
def count_cases(s):
    upper = 0
    lower = 0
    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    return upper, lower   #After going through the entire string, return both the upper and lower counts as a tuple

text = "Hello World!"
up, low = count_cases(text)
print("Uppercase:", up, "Lowercase:", low)
#Calls your function count_cases(text). 
#The result is two numbers: number of uppercase letters and number of lowercase letters. It's stored in up and low.
