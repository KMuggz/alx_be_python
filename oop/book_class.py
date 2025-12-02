class Book:
    """
    A class to represent a Book, demonstrating Python's magic methods.
    """
    def __init__(self, title, author, year):
        # The constructor: Initializes a Book instance with title, author, and year.
        self.title = title
        self.author = author
        self.year = year
        # Optional: Print a message to show when an object is created.
        # print(f"Book '{self.title}' created.")

    def __str__(self):
        # String Representation (__str__): Called by print() and str().
        # Returns a user-friendly string for the object.
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official Representation (__repr__): Called by repr().
        # Returns a string that can be used to recreate the object.
        # This is useful for debugging and logging.
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        # Destructor (__del__): Called when the object is about to be destroyed/garbage collected.
        # Note: __del__ is not guaranteed to be called immediately when 'del' is used,
        # but in simple scripts like this, it usually is.
        print(f"Deleting {self.title}")

