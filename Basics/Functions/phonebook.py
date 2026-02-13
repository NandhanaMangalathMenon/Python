# Phonebook program using dict and functions
phonebook = {}      #Creates an empty dictionary
                    #You will use names as keys and phone numbers as values.

def add_contact(name, phone):
    phonebook[name] = phone     #In Python, dictionaries are collections of key-value pairs. 
                                #To access or set the value for a specific key, 
                                #python uses square bracket notation with the key inside the brackets.
    #Defines a function add_contact that takes two arguments: name and phone.
#It sets phonebook[name] = phone, meaning it stores the phone number under the person's name.
#If the name already exists, it updates the number.

def search_contact(name):
    return phonebook.get(name, "Not found")
#Defines search_contact to find a phone number for a given name.
# .get() returns the phone number for that name if found; otherwise, it returns the string 'Not found'.

def delete_contact(name):
    if name in phonebook:           #Checks if name exists in phonebook..If not found, does nothing
        del phonebook[name]

def display_contacts():
    for name, phone in phonebook.items():
        print(name, ":", phone)

# Examples:
add_contact("Alice", "1234")
add_contact("Bob", "5678")
print(search_contact("Alice"))  # 1234
delete_contact("Bob")
display_contacts()
