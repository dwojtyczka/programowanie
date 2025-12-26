class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        average = sum(self.marks) / len(self.marks)
        return average > 50


student_zaliczył = Student("Adam", [60, 70, 55])
student_nie_zaliczył = Student("Ewa", [30, 40, 50])

print(f"{student_zaliczył.name} passed: {student_zaliczył.is_passed()}")
print(f"{student_nie_zaliczył.name} passed: {student_nie_zaliczył.is_passed()}")
