
"""class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0.0
        self.address = ""

    def get_input(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def print_info(self):
        print(f"Name: {self.name} | Age: {self.age} | Salary: {self.salary} | Address: {self.address}")

class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = ""

    def get_input(self):
        super().get_input()
        self.department = input("Enter Department: ")

    def print_info(self):
        super().print_info()
        print(f"Department: {self.department}")

# Processing information for 10 managers
managers = []
for i in range(1, 11):
    print(f"\n--- Enter Details for Manager {i} ---")
    m = Manager()
    m.get_input()
    managers.append(m)

print("\n--- Displaying Information of 10 Managers ---")
for m in managers:
    m.print_info()
    print("-" * 30)
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_lent = False

class Member:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully.")

    def lend_book(self, book_title, member_name):
        for book in self.books:
            if book.title == book_title and not book.is_lent:
                book.is_lent = True
                print(f"Book '{book_title}' lent to {member_name}.")
                return
        print("Book not available or already lent.")

    def return_book(self, book_title):
        for book in self.books:
            if book.title == book_title and book.is_lent:
                book.is_lent = False
                print(f"Book '{book_title}' returned.")
                return
        print("Invalid return request.")

    def display_books(self):
        print("\nLibrary Inventory:")
        for book in self.books:
            status = "Lent" if book.is_lent else "Available"
            print(f"Title: {book.title} | Author: {book.author} | Status: {status}")

# Menu-Driven Interface
def main():
    my_library = Library()
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book\n2. Lend Book\n3. Return Book\n4. Display Books\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            t = input("Enter Title: ")
            a = input("Enter Author: ")
            my_library.add_book(t, a)
        elif choice == '2':
            t = input("Book Title to lend: ")
            m = input("Member Name: ")
            my_library.lend_book(t, m)
        elif choice == '3':
            t = input("Book Title to return: ")
            my_library.return_book(t)
        elif choice == '4':
            my_library.display_books()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
