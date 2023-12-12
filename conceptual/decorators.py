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
