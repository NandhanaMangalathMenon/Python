# Students enrolled in Python course
python_students = {"Alice", "Bob", "Charlie", "David"}

# Students enrolled in Java course
java_students = {"Charlie", "David", "Eve"}

print("Python students:", python_students)
print("Java students:", java_students)

# 1. Students enrolled in both courses
print("\nStudents enrolled in both courses:")
print(python_students & java_students)

# 2. Students who took only Python
print("Students who took only Python:")
print(python_students - java_students)

# 3. Total number of unique students
all_students = python_students | java_students
print("Total number of unique students:")
print(len(all_students))

# 4. Check if all Python students are also Java students
print("Are all Python students also Java students?")
print(python_students <= java_students)

#Is set A a subset of set B?
# “Are python_students a subset of java_students?”