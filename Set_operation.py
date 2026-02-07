#Given two sets of student roll numbers, those who attended the morning session and those who attended the afternoon, 
#find and display students who attended both sessions

# Sets of student roll numbers
morning_session = {101, 102, 103, 104, 105}
afternoon_session = {104, 105, 106, 107}

# Find students who attended both sessions using set intersection
attended_both = morning_session.intersection(afternoon_session)

# Display the result
print("Students who attended both sessions:", attended_both)
