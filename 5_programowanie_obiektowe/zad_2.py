from typing import List


class Student:
    def __init__(self, name: str, marks: List[int]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return (sum(self.marks) / len(self.marks)) > 50

    def __str__(self) -> str:
        return f"Student: {self.name}"


class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f"Biblioteka: {self.city}, ul. {self.street} ({self.open_hours})"


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str,
                 zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f"Pracownik: {self.first_name} {self.last_name} (Zatrudniony: {self.hire_date})"


class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str,
                 number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"'{self.author_name} {self.author_surname}' (Dostępna w: {self.library.city})"


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


lib_warszawa = Library("Warszawa", "Koszykowa 1", "00-001", "8:00-20:00", "111-222-333")
lib_krakow = Library("Kraków", "Rajska 1", "31-124", "9:00-19:00", "444-555-666")

emp_anna = Employee("Anna", "Kowalska", "2020-01-01", "1990-05-12", "Warszawa", "Polna", "00-100", "123456789")
emp_jan = Employee("Jan", "Nowak", "2018-03-15", "1985-11-20", "Kraków", "Długa", "31-000", "987654321")
emp_piotr = Employee("Piotr", "Wiśniewski", "2021-06-01", "1992-02-28", "Warszawa", "Złota", "00-200", "555666777")

student_1 = Student("Tomek", [30, 40, 50])
student_2 = Student("Kasia", [90, 100, 95])
student_3 = Student("Michał", [60, 65, 70])

b1 = Book(lib_warszawa, "2001", "J.K.", "Rowling", 300)
b2 = Book(lib_warszawa, "1954", "J.R.R.", "Tolkien", 500)
b3 = Book(lib_krakow, "1986", "Stephen", "King", 800)
b4 = Book(lib_krakow, "1949", "George", "Orwell", 250)
b5 = Book(lib_warszawa, "1925", "F.", "Fitzgerald", 180)

order1 = Order(emp_anna, student_2, [b1, b2, b5], "2023-10-12")
order2 = Order(emp_jan, student_1, [b3], "2023-10-13")

print(order1)
print("-" * 30)
print(order2)
