# Initial data
employees = {
    "Engineering": {
        "Alice": "Senior Engineer",
        "Bob": "Junior Engineer"
    },
    "HR": {
        "Carol": "Manager",
        "David": "Recruiter"
    }
}

#1. ADD A NEW DEPARTMENT 
def add_department(employees, dept_name):
    if dept_name not in employees:
        employees[dept_name] = {}
        print("Department added")
    else:
        print("Department already exists")

add_department(employees, "Finance")


# 2. ADD AN EMPLOYEE 
def add_employee(employees, dept_name, emp_name, role):
    if dept_name in employees:
        employees[dept_name][emp_name] = role
        print("Employee added")
    else:
        print("Department not found")

add_employee(employees, "Engineering", "Eve", "Intern")


# 3. REMOVE AN EMPLOYEE 
def remove_employee(employees, dept_name, emp_name):
    if dept_name in employees and emp_name in employees[dept_name]:
        del employees[dept_name][emp_name]
        print("Employee removed")
    else:
        print("Employee or department not found")

remove_employee(employees, "HR", "David")


# 4. LIST EMPLOYEES IN A DEPARTMENT 
def list_employees(employees, dept_name):
    if dept_name in employees:
        for name, role in employees[dept_name].items():
            # .items()--This gives both key and value together as pairs.
            #("Alice", "Senior Engineer")


            print(name, "-", role)
    else:
        print("Department not found")

print("\nEmployees in Engineering:")
list_employees(employees, "Engineering")
