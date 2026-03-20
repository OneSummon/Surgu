import sys

def memory_decorator(func):
    def wrapper():
        print("Начало выполнения функции")
        result = func()
        print(f"Память, использованная функцией: {sys.getsizeof(result)} байт")
        return result
    return wrapper