# Library dictionary
library = {
    "1984": {"author": "George Orwell", "available": True},
    "Dune": {"author": "Frank Herbert", "available": False}
}

# 1. Add a new book
def add_book(library, title, author):
    library[title] = {"author": author, "available": True}
    print("Book added")

add_book(library, "The Hobbit", "Tolkien") #calling the function

#Let’s examine what is needed to add a book:

# | What do we need? | Why                    |
# | ---------------- | ---------------------- |
# | `library`        | Where to add the book  |
# | `title`          | Name of the book (key) |
# | `author`         | Author name (value)    |



# 2. Borrow a book
def borrow_book(library, title):  #We do NOT need the author to borrow a book
    if title in library and library[title]["available"]:
        #This checks two conditions:
        #Book exists
        #Book is available
        library[title]["available"] = False #Marks book as borrowed
        print("Book borrowed")
    else:
        print("Book not available")

borrow_book(library, "1984")

# This code defines a function to borrow a book from the library. 
# The function borrow_book takes the library dictionary and the book title as arguments because, 
# to borrow a book, the program needs to know where the books are stored and which specific book is being requested.
# Inside the function, it checks whether the given book title exists in the library and whether its "available" value is True.
# If "available" is True, it means the book has not been borrowed yet and is currently present in the library,
# so the program marks the book as borrowed by setting "available" to False and prints a confirmation message. 
# If the book does not exist in the library or its "available" value is already False,
# it means the book is either unavailable or already borrowed, and the program prints an appropriate message. 
# Finally, calling borrow_book(library, "1984") applies this logic to attempt borrowing the book titled 1984 from the library.

# 3. Return a book
def return_book(library, title):
    if title in library:
        library[title]["available"] = True
        print("Book returned")

return_book(library, "Dune")


# 4. Show all available books
def show_available_books(library):
    print("Available books:")
    for title, info in library.items():
        if info["available"]:
            print(title, "-", info["author"])

show_available_books(library)
