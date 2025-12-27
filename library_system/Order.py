from typing import List
from library_system.Employee import Employee
from library_system.Student import Student
from library_system.Book import Book

class Order:
    def __init__(self, employee: Employee, student: Student, books: List[Book], order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        ksiazki_str = ", ".join([f"{b.author_name} {b.author_surname}" for b in self.books])
        return (f"ZAMÓWIENIE z dnia {self.order_date}:\n"
                f"  Obsługujący: {self.employee.last_name}\n"
                f"  Zamawiający: {self.student.name}\n"
                f"  Książki: {ksiazki_str}")
