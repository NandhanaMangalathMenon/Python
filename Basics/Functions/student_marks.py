# Student marks using dict and functions
students = {}         #Key: student name (string). Value: list of marks (numbers).


def add_student(name):
    students[name] = []  #Adds the name as a key in the dictionary, with an empty list as the value.

def add_mark(name, mark):
    if name in students:  #Checks if the student's name exists in the dictionary.
        students[name].append(mark)    #f yes, adds the new mark to their list using .append().

def avg_marks(name):  #It takes one argument, name—the student's name you want the average for.

    if name in students and students[name]:
        #First, name in students checks if that student's name is present in the dictionary
        #Second, students[name] is tested in a Boolean context:
        #If the list of marks is not empty, it evaluates to True (non-empty lists are truthy).
        #If the list is empty, it evaluates to False.
        #So, this condition is only True if the student exists and has at least one mark recorded.
        return sum(students[name]) / len(students[name])
#If the above condition is True, this line is run.
#students[name] is the list of marks for the student, e.g. [95][85][80].
#sum(students[name]) adds up all their marks: 95 + 85 + 80 = 260.
#len(students[name]) counts how many marks there are: 3.
#Divides the total by the number of marks: 260 / 3 = 86.666...
#The result is the average mark (mean value). This is returned by the function.

    else:
        return 0
    #If the student name is not in the dictionary or they have no marks (empty list), the function returns 0.

def assign_grades(name):
    grades = []
    for m in students.get(name, []):
        if m >= 90:
            grades.append('A')
        elif m >= 75:
            grades.append('B')
        else:
            grades.append('C')
    return grades

add_student("Ravi")
add_mark("Ravi", 95)
add_mark("Ravi", 85)
print("Average:", avg_marks("Ravi")) # 90.0
print("Grades:", assign_grades("Ravi")) # ['A', 'B']
