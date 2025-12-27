from library_system.Library import Library
from library_system.Employee import Employee
from library_system.Student import Student
from library_system.Book import Book
from library_system.Order import Order

if __name__ == '__main__':
    lib_warszawa = Library("Warszawa", "Koszykowa 1", "00-001", "8:00-20:00", "111-222-333")
    lib_krakow = Library("Kraków", "Rajska 1", "31-124", "9:00-19:00", "444-555-666")

    emp_anna = Employee("Anna", "Kowalska", "2020-01-01", "1990-05-12", "Warszawa", "Polna", "00-100", "123456789")
    emp_jan = Employee("Jan", "Nowak", "2018-03-15", "1985-11-20", "Kraków", "Długa", "31-000", "987654321")

    student_1 = Student("Tomek", [30, 40, 50])
    student_2 = Student("Kasia", [90, 100, 95])

    b1 = Book(lib_warszawa, "2001", "J.K.", "Rowling", 300)
    b2 = Book(lib_warszawa, "1954", "J.R.R.", "Tolkien", 500)
    b3 = Book(lib_krakow, "1986", "Stephen", "King", 800)
    b5 = Book(lib_warszawa, "1925", "F.", "Fitzgerald", 180)

    order1 = Order(emp_anna, student_2, [b1, b2, b5], "2023-10-12")
    order2 = Order(emp_jan, student_1, [b3], "2023-10-13")

    print(order1)
    print("-" * 30)
    print(order2)
