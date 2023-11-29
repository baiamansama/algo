# variable assigning
a = [1, 2, 3, 4]
print(id(a))
b = a
print(id(b))
b.append(5)
print(a)
print(b)


"""
    Decorators: Декоратор — это функция, которая позволяет обернуть другую функцию для 
    расширения её функциональности без непосредственного изменения её кода.

"""
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
user = User("simple_user", "user")
admin = User("root", "admin")

current_user = admin

def check_access(func):
    def wrapper(*args, **kwargs):
        if current_user.role != "admin":
            raise Exception("Доспут запрешен!")
        return func(*args, **kwargs)
    return wrapper

@check_access
def do_admin_work(input):
    print(f"Делаем что-то доспутное только админу {input}")

do_admin_work("Baiaman")


"""
local variables -> declared inside class or function
global variable -> declared on upper level,side of the program

LEGB ->
* local
* enclosing
* global
* built-in
"""
# local
name = "Ivan"

def greet_local():
    name = "Sasha"
    print(f"Hi {name}")

greet_local()

# enclosing -> taking parent's

def greet_enclosing():
    name = "Sasha"
    def hello():
        print(f"Hi {name}")
    hello()

greet_enclosing()

# global

def greet_global():
    print(f"Hi {name}")
greet_global()


def greet_global_bad():
    global name # takes in global variable "name"
    name = "Petya"  # changes global variable
    print(f"Hi {name}")

greet_global_bad()
print(name)

#built-in

print(__name__)
__name__ = "test" # program may behave strangely
print(__name__)

print(id(name))

def id(var):
    print(123)

id(name) #instead of addres we get 123, which is not expected

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