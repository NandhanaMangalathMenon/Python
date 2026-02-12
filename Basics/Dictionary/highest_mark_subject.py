# Dictionary of subject marks
marks = {
    "Math": 85,
    "Science": 90,
    "English": 78,
    "History": 88,
    "Geography": 92
}

# Find the subject with the highest score using max() and key argument
top_subject = max(marks, key=marks.get)

# Print the subject with the highest score
print("Subject with the highest score:", top_subject)


#top_subject = max(marks, key=marks.get)
# marks.get("Math") returns 85
# marks.get("Science") returns 90

#We write marks after max because:
#max() needs an iterable (something to check for max value).
#When you write max(marks, key=marks.get), you are passing the dictionary marks as the iterable.
#Iterating over a dictionary means iterating over its keys.
#max() compares those keys, but since we want to find the key with the maximum value, we use key=marks.get.
#marks.get tells max() to use the values (scores) for comparison, not the keys themselves.
#So, marks here is the source of the keys, and key=marks.get tells how to compare those keys.