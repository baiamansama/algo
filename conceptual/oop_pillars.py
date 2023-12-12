"""
    Pillars of OOP: Inheritance, Encapsulation, Polymorphism and Abstraction
"""
#inheritance - inheritance of child classes from parent class
class Person:
    name = "Ivan"
    age = 10

    def set(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    course = 1
class KAIST_student(Person):
    def __init__(self, stress, name, age):
        super(KAIST_student, self).set(name, age)
        self.stress = stress
igor = Student()
igor.set("Igor", 19)
igor.course = 2
print(f"Information about student {igor.name} {igor.age} {igor.course}")

kevin = KAIST_student(True, "Kevin", 22)


#encapsulation - limiting access to certain fields, functions
class Person:
    _name = "Ivan" # note to programmer to not modify it
    age = 10

    def __set(self, name, age):  # it's protected, but not full. see below
        self.name = name
        self.age = age

class Student(Person):
    course = 1
class KAIST_student(Person):
    a_bit_stress = "issoyo"
igor = Student()
# igor.set("Igor", 19)  --> AttributeError: 'Student' object has no attribute 'set'
igor._Person__set("Igor", 19)
print(f"Information about student {igor.name} {igor.age} {igor.course}")


# Polymorphism - reuse of certain functions from parent class to 
# get different results. example len() in python.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        print(f"name: {self.name} and age: {self.age}")

class Student(Person):
    course = 1
    def get_info(self):
        super().get_info()
        print(f"taking this course number: {self.course}")


student = Student("Artur", 12)
student.get_info()


# absraction -> similar to encapsulation. abstract certain functions out of 
# accessibility