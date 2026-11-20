"""Group C - Library module: manages the book collection and members."""

from book import Book
from member import Member


class Library:
    """Holds the book collection (keyed by ISBN) and registered members."""

    def __init__(self):
        self.books = {}
        self.members = {}

    # ---- books ----
    def add_book(self, book):
        """Add a book. If the ISBN already exists, its copies are increased."""
        if not isinstance(book, Book):
            raise TypeError("add_book expects a Book instance.")
        if book.isbn in self.books:
            self.books[book.isbn].copies += book.copies
        else:
            self.books[book.isbn] = book

    def remove_book(self, isbn):
        """Remove a book. Returns False if not found.

        Raises ValueError if any member still has the book borrowed.
        """
        if isbn not in self.books:
            return False
        if any(isbn in m.borrowed_books for m in self.members.values()):
            raise ValueError("Cannot remove a book that is currently borrowed.")
        del self.books[isbn]
        return True

    def get_book(self, isbn):
        """Return the Book with this ISBN, or None."""
        return self.books.get(isbn)

    def list_books(self):
        """Return all books sorted by title."""
        return sorted(self.books.values(), key=lambda b: b.title.lower())

    # ---- members ----
    def add_member(self, member):
        """Register a member. Raises ValueError on duplicate ID."""
        if not isinstance(member, Member):
            raise TypeError("add_member expects a Member instance.")
        if member.member_id in self.members:
            raise ValueError(f"Member ID '{member.member_id}' already exists.")
        self.members[member.member_id] = member

    def get_member(self, member_id):
        """Return the Member with this ID, or None."""
        return self.members.get(member_id)

    def list_members(self):
        """Return all members sorted by ID."""
        return sorted(self.members.values(), key=lambda m: m.member_id)
