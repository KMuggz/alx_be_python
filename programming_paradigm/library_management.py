class Book:
    def __init__(self, title, author):
        """Initialize a book with title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Find a book by title and check it out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return 
        print(f"Sorry, {title} is either not in the library or already checked out.")

    def return_book(self, title):
        """Find a book by title and return it."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book titled '{title}' not found in library records.")

    def list_available_books(self):
        """Print details of all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")