"""Group A - Book module: defines the structure of a book."""


class Book:
    """A book in the library.

    Attributes:
        isbn (str): Unique book identifier.
        title (str): Title of the book.
        author (str): Author of the book.
        copies (int): Number of copies currently available.
    """

    def __init__(self, isbn, title, author, copies):
        isbn, title, author = str(isbn).strip(), str(title).strip(), str(author).strip()
        if not isbn:
            raise ValueError("ISBN cannot be empty.")
        if not title:
            raise ValueError("Title cannot be empty.")
        if not author:
            raise ValueError("Author cannot be empty.")
        if isinstance(copies, bool) or not isinstance(copies, int) or copies < 0:
            raise ValueError("Copies must be a non-negative integer.")
        self.isbn = isbn
        self.title = title
        self.author = author
        self.copies = copies

    def is_available(self):
        """Return True if at least one copy is available."""
        return self.copies > 0

    def to_dict(self):
        """Return the book as a plain dictionary."""
        return {"isbn": self.isbn, "title": self.title,
                "author": self.author, "copies": self.copies}

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, copies: {self.copies})"

    def __repr__(self):
        return f"Book({self.isbn!r}, {self.title!r}, {self.author!r}, {self.copies!r})"
