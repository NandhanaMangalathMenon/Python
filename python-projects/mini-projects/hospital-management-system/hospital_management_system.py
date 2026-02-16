"""
HOSPITAL MANAGEMENT SYSTEM

This is a console-based Hospital Management System written in Python.

Features:
- Load patient and doctor data from a text file
- Admit new patients
- Discharge patients
- Track admitted patients using a set
- Generate disease-wise report
- Calculate total hospital revenue
- Save disease report to a file

Concepts Used:
- Dictionaries
- Sets
- File Handling
- Functions
- Loops
- Conditional Statements
"""


# FUNCTION: Load hospital data from file

def load_hospital(filename):
    """
    Reads hospital.txt and loads:
    - patients (dictionary)
    - doctors (dictionary)
    - admitted_patients (set)
    """

    patients = {}           # Stores full patient information
    doctors = {}            # Stores doctor details
    admitted_patients = set()  # Stores only admitted patient IDs

    try:
        # Using 'with open' for safe file handling
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found!")
        return patients, doctors, admitted_patients

    for line in lines:
        line = line.strip()     # Remove extra spaces
        if line == "":
            continue            # Skip empty lines

        parts = line.split(",")

       
        # PATIENT RECORD
        # Format:
        # Patient001,Ram,25,Fever,Admitted,Bill:5000
      
        if parts[0].startswith("Patient"):
            pid = parts[0]
            name = parts[1]
            age = parts[2]
            disease = parts[3]
            status = parts[4]
            bill = parts[5].replace("Bill:", "")  # Remove "Bill:" text

            # Store details inside dictionary
            patients[pid] = [name, age, disease, status, bill]

            # If patient is admitted, add to set
            if status == "Admitted":
                admitted_patients.add(pid)

        # DOCTOR RECORD
        # Format:
        # Doctor101,Dr.Amit,Cardiology
       
        elif parts[0].startswith("Doctor"):
            did = parts[0]
            name = parts[1]
            specialty = parts[2]

            doctors[did] = [name, specialty]

    return patients, doctors, admitted_patients



# FUNCTION: Admit a new patient

def admit_patient(pid, did, patients, doctors, admitted_patients):

    if pid in patients:
        return "Patient already exists"

    if did not in doctors:
        return "Doctor not found"

    # Take user input for new patient
    name = input("Enter name: ")
    age = input("Enter age: ")
    disease = input("Enter disease: ")
    bill = input("Enter bill amount: ")

    # Add patient to dictionary
    patients[pid] = [name, age, disease, "Admitted", bill]

    # Add patient ID to admitted set
    admitted_patients.add(pid)

    return "Patient admitted successfully"



# FUNCTION: Discharge a patient

def discharge_patient(pid, patients, admitted_patients):

    if pid not in patients:
        return "Patient not found"

    if pid not in admitted_patients:
        return "Patient not admitted"

    # Update status in dictionary (index 3 = status)
    patients[pid][3] = "Discharged"

    # Remove from admitted set
    admitted_patients.remove(pid)

    return "Patient discharged successfully"



# FUNCTION: Calculate total revenue

def total_revenue(patients):

    total = 0

    # Loop through all patients
    for info in patients.values():
        bill = int(info[4])  # Bill is stored as string
        total += bill

    return total


# FUNCTION: Generate disease report

def disease_report(patients):

    disease_count = {}

    # Count how many patients per disease
    for info in patients.values():
        disease = info[2]  # Index 2 = disease

        if disease in disease_count:
            disease_count[disease] += 1
        else:
            disease_count[disease] = 1

    return disease_count


# FUNCTION: Save disease report to file

def save_report(report, filename):

    with open(filename, "w") as f:
        f.write("DISEASE REPORT\n")
        f.write("=" * 20 + "\n")

        for disease, count in report.items():
            f.write(f"{disease}: {count} patients\n")



# MAIN PROGRAM


# Load initial data from hospital.txt
patients, doctors, admitted_patients = load_hospital("hospital.txt")

while True:

    print("\nHOSPITAL SYSTEM")
    print("1. Show all data")
    print("2. Admit patient")
    print("3. Discharge patient")
    print("4. Disease report")
    print("5. Total revenue")
    print("6. Exit")

    choice = input("Choice (1-6): ")

    if choice == "1":
        print("PATIENTS:", patients)
        print("DOCTORS:", doctors)
        print("ADMITTED:", admitted_patients)

    elif choice == "2":
        pid = input("Patient ID: ")
        did = input("Doctor ID: ")
        print(admit_patient(pid, did, patients, doctors, admitted_patients))

    elif choice == "3":
        pid = input("Patient ID: ")
        print(discharge_patient(pid, patients, admitted_patients))

    elif choice == "4":
        report = disease_report(patients)
        print("Disease report:", report)
        save_report(report, "report.txt")
        print("Report saved to report.txt")

    elif choice == "5":
        revenue = total_revenue(patients)
        print("Total revenue: Rs.", revenue)

    elif choice == "6":
        print("System closed")
        break

    else:
      print("Invalid Choice!")
        print("Invalid choice!")
