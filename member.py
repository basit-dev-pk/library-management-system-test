"""Group B - Member module: manages library members."""

MAX_BORROW_LIMIT = 3


class Member:
    """A library member.

    Attributes:
        member_id (str): Unique member identifier.
        name (str): Member's full name.
        borrowed_books (list[str]): ISBNs of books currently borrowed.
    """

    def __init__(self, member_id, name):
        member_id, name = str(member_id).strip(), str(name).strip()
        if not member_id:
            raise ValueError("Member ID cannot be empty.")
        if not name:
            raise ValueError("Name cannot be empty.")
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def has_borrowed(self, isbn):
        """Return True if the member currently holds the given ISBN."""
        return isbn in self.borrowed_books

    def can_borrow(self):
        """Return True if the member is below the borrowing limit."""
        return len(self.borrowed_books) < MAX_BORROW_LIMIT

    def __str__(self):
        return f"{self.name} (ID: {self.member_id}, borrowed: {len(self.borrowed_books)})"

    def __repr__(self):
        return f"Member({self.member_id!r}, {self.name!r})"
