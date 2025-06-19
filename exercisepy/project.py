class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author):
        # Check if book_id already exists
        for book in self.books:
            if book.book_id == book_id:
                print("Book with this ID already exists!")
                return
        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully.")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"Book '{book.title}' issued successfully.")
                    return
                else:
                    print("Book is already issued.")
                    return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print(f"Book '{book.title}' returned successfully.")
                    return
                else:
                    print("Book was not issued.")
                    return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Library Books:")
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(f"ID: {book.book_id} | Title: {book.title} | Author: {book.author} | Status: {status}")

def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(book_id, title, author)
        elif choice == '2':
            book_id = input("Enter book ID to issue: ")
            library.issue_book(book_id)
        elif choice == '3':
            book_id = input("Enter book ID to return: ")
            library.return_book(book_id)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
