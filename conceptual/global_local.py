"""
local variables -> declared inside class or function
global variable -> declared on upper level, side of the program

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

