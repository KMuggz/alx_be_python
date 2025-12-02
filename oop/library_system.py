class Book:
    """
    Base class for all books in the library.
    """
    def __init__(self, title, author):
        # Initialize common attributes: title and author.
        self.title = title
        self.author = author

    def __str__(self):
        # Default string representation for the base Book class.
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class for Electronic Books, inheriting from Book.
    """
    def __init__(self, title, author, file_size):
        # Call the base class constructor to initialize title and author.
        super().__init__(title, author)
        # Initialize the unique attribute for EBook.
        self.file_size = file_size

    def __str__(self):
        # Overrides the base class __str__ to include file_size.
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class for Physical Print Books, inheriting from Book.
    """
    def __init__(self, title, author, page_count):
        # Call the base class constructor.
        super().__init__(title, author)
        # Initialize the unique attribute for PrintBook.
        self.page_count = page_count

    def __str__(self):
        # Overrides the base class __str__ to include page_count.
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    A class that demonstrates Composition by managing a list of Book objects.
    """
    def __init__(self):
        # Composition: The Library 'has-a' list of books.
        self.books = []

    def add_book(self, book):
        # Adds any instance of Book (or its subclasses) to the library's collection.
        self.books.append(book)

    def list_books(self):
        # Iterates through the collection and prints details of each book.
        # Polymorphism is demonstrated here: book.__str__() calls the correct
        # __str__ method (Book, EBook, or PrintBook) for each object.
        for book in self.books:
            print(book)

