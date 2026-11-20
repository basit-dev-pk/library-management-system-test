# Library Management System

A modular, object-oriented Library Management System in Python with a Tkinter GUI.
Built collaboratively by Groups A–H using GitHub.

## Modules
| Group | File | Purpose |
|---|---|---|
| A | `book.py` | `Book` class (isbn, title, author, copies) |
| B | `member.py` | `Member` class, borrow limit |
| C | `library.py` | `Library`: add/remove/list books and members |
| D | `issue_return.py` | `issue_book`, `return_book` |
| E | `search.py` | Search by title / author / ISBN, availability |
| F | `auth_system.py` | Login with hashed passwords, roles |
| G | `library_management_system.py` | Tkinter GUI |
| H | `test_library.py` | Unit tests |

## Run
```bash
python library_management_system.py      # GUI (needs Python 3.8+ with tkinter)
python -m unittest -v                    # tests
```
Demo logins: `admin / admin123` (librarian), `alice / alice123` (member M001).

## GitHub Workflow
1. Repo `library-management-system` with branch protection on `main`.
2. Work only on your branch: `group-a-book`, `group-b-member`, ...
3. Open a PR to `main` using the PR template.
4. Review, request changes if needed, merge only after review and passing tests.
5. Interface changes must be reported to Group G immediately.

## Conventions
Use `isbn`, `title`, `author`, `copies`, `member_id`; docstrings on every class/function.
