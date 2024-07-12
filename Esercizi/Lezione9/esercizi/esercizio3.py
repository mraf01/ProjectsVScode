'''
Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

Classe Book:

Attributi:
book_id: str - Identificatore di un libro.
title: str - titolo del libro.
author: str - autore del libro
is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
Metodi:
borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
return_book()- Contrassegna il libro come restituito.
Classe Member:

Attributi:
member_id: str - identificativo del membro.
name: str - il nome del membro.
borrowed_books: list[Book] - lista dei libri presi in prestito.
Metodi:
borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
return_book(book): rimuove il libro dalla lista borrowed_books.
Classe Library:

Attributi:
books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
Methodi:
add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.
'''

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        raise ValueError("Book is already borrowed")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        raise ValueError("Book is not borrowed")


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
            return True
        raise ValueError("Book is already borrowed")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        raise ValueError("Book not borrowed by this member")


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author)

    def register_member(self, member_id, name):
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError("Book not found")
        member = self.members[member_id]
        book = self.books[book_id]
        return member.borrow_book(book)

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError("Book not found")
        member = self.members[member_id]
        book = self.books[book_id]
        return member.return_book(book)

    def get_borrowed_books(self, member_id):
        if member_id in self.members:
            member = self.members[member_id]
            return [book.title for book in member.borrowed_books]
        return []


# Test

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  # Expected output: ['1984']



library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

library.return_book("M001", "B001")
library.return_book("M002", "B002")

# Check borrowed books after returning
print(library.get_borrowed_books("M001"))  # output: []
print(library.get_borrowed_books("M002"))  # output: []



library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

# Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")

library.borrow_book("M001", "B001")
try:
    library.borrow_book("M002", "B001")
except ValueError as e:
    print(e)                        # output: Book is already borrowed



library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

# Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")

# Edge case - trying to return a book that is not borrowed
try:
    library.return_book("M001", "B003")
except ValueError as e:
    print(e)                       # output: Book not borrowed by this member



library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

# Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")

# Edge case - trying to borrow a book by a non-existent member
try:
    library.borrow_book("M004", "B001")
except ValueError as e:
    print(e)                                 # output: Member not found



library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

# Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")

# Edge case - trying to borrow a non-existent book
try:
    library.borrow_book("M001", "B004")
except ValueError as e:
    print(e)                               # output: Book not found



library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

# Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")

# Complex Test Case 1: Multiple members borrow and return books
# Alice borrows "1984" and "To Kill a Mockingbird"
library.borrow_book("M001", "B002")
library.borrow_book("M001", "B003")

# Bob tries to borrow "1984" (already borrowed by Alice)
try:
    library.borrow_book("M002", "B002")
except ValueError as e:
    print(e)                          # output: Book is already borrowed