from abc import ABC, abstractmethod
import math

# Exercise 1: Abstract Class and Subclasses
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Exercise 2: Static Methods
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Exercise 3: Library Management System
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    @classmethod
    def from_string(cls, book_str):
        title, author, isbn = book_str.split(", ")
        return cls(title, author, isbn)

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

    def __str__(self):
        books = ', '.join(book.title for book in self.borrowed_books)
        return f"Name: {self.name}, ID: {self.member_id}, Borrowed Books: [{books}]"

    @classmethod
    def from_string(cls, member_str):
        name, member_id = member_str.split(", ")
        return cls(name, member_id)

class Library:
    total_books = 0

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        Library.total_books += 1

    def remove_book(self, book):
        self.books.remove(book)
        Library.total_books -= 1

    def register_member(self, member):
        self.members.append(member)

    def lend_book(self, book, member):
        if book in self.books and member in self.members:
            self.books.remove(book)
            member.borrow_book(book)
        else:
            print("Book or member not found in the library.")

    def __str__(self):
        books = ', '.join(book.title for book in self.books)
        members = ', '.join(member.name for member in self.members)
        return f"Books: [{books}], Members: [{members}]"

    @classmethod
    def library_statistics(cls):
        print(f"Total number of books: {cls.total_books}")

# Exercise 4: University Management System
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def get_role(self):
        return "Student"

    def __str__(self):
        courses = ', '.join(course.course_name for course in self.courses)
        return f"{super().__str__()}, Student ID: {self.student_id}, Courses: [{courses}]"

class Professor(Person):
    def __init__(self, name, age, professor_id, department):
        super().__init__(name, age)
        self.professor_id = professor_id
        self.department = department
        self.courses = []

    def assign_to_course(self, course):
        self.courses.append(course)

    def get_role(self):
        return "Professor"

    def __str__(self):
        courses = ', '.join(course.course_name for course in self.courses)
        return f"{super().__str__()}, Professor ID: {self.professor_id}, Department: {self.department}, Courses: [{courses}]"

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
        self.professor = None

    def add_student(self, student):
        self.students.append(student)

    def set_professor(self, professor):
        self.professor = professor

    def __str__(self):
        students = ', '.join(student.name for student in self.students)
        professor = self.professor.name if self.professor else "None"
        return f"Course Name: {self.course_name}, Course Code: {self.course_code}, Professor: {professor}, Students: [{students}]"

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.courses = []
        self.professors = []

    def add_course(self, course):
        self.courses.append(course)

    def add_professor(self, professor):
        self.professors.append(professor)

    def __str__(self):
        courses = ', '.join(course.course_name for course in self.courses)
        professors = ', '.join(professor.name for professor in self.professors)
        return f"Department: {self.department_name}, Courses: [{courses}], Professors: [{professors}]"

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.students = []

    def add_department(self, department):
        self.departments.append(department)

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        departments = ', '.join(department.department_name for department in self.departments)
        students = ', '.join(student.name for student in self.students)
        return f"University: {self.name}, Departments: [{departments}], Students: [{students}]"



book1 = Book.from_string("La Divina Commedia, D. Alighieri, 999000666")
book2 = Book.from_string("1984, G. Orwell, 123456789")
member1 = Member.from_string("Alice, 001")
member2 = Member.from_string("Mario, 002")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_member(member1)
library.register_member(member2)

print("Library State Before Lending:")
print(library)

library.lend_book(book1, member1)

print("\nLibrary State After Lending:")
print(library)
print(f"Member {member1.name}'s Borrowed Books: {[str(book) for book in member1.borrowed_books]}")

department = Department("Computer Science")
course = Course("Introduction to Programming", "CS101")
professor = Professor("Professor Fabio", 45, "P001", "Computer Science")
student = Student("Alice", 20, "S001")

department.add_course(course)
department.add_professor(professor)

course.set_professor(professor)
professor.assign_to_course(course)

course.add_student(student)
student.enroll(course)

university = University("Tech University")
university.add_department(department)
university.add_student(student)

print("\nUniversity State:")
print(university)