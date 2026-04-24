def cls_decorator(func): # добавляет метод в класс
    def decorator(cls):
        setattr(cls, func.__name__, func)
        return cls
    return decorator

def greet(self):
    return f"Привет, я {self.name}!"

def info(self):
    return f"{self.name}, возраст: {self.age}"


@cls_decorator(greet)
@cls_decorator(info)
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Almaz = People("Алмаз", 18)

print(Almaz.greet())
print(Almaz.info())