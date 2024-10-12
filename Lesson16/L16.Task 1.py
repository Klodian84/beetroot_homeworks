class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Subclass of student
class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def study(self):
        return f"{self.name} is studying."

    def get_grade(self):
        return f"{self.name} is in grade {self.grade}."


# Subclass of teacher
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def teach(self):
        return f"{self.name} is teaching {self.subject}."

    def get_salary(self):
        return f"{self.name}'s salary is ${self.salary}."


# Student object
student1 = Student(name="Ana", age=20, student_id="S123", grade=9)
print(student1.introduce())  # inherited method from Person
print(student1.study())  # Student-specific method
print(student1.get_grade())  # Student-specific method

# Teacher object
teacher1 = Teacher(name="Mr. Harrison", age=40, subject="Physics", salary=50000)
print(teacher1.introduce())
print(teacher1.teach())
print(teacher1.get_salary())
