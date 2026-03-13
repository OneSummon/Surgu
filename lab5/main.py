import sys

def make_read(source, n):
    offset = 0

    def read():
        nonlocal offset
        chunk = source[offset: offset + n]
        offset += n
        return chunk
    return read

read5 = make_read("hello world", 5)

for i in range(4):
    print(read5())

def memory_decorator(func):
    def wrapper():
        print("Начало выполнения функции")
        result = func()
        print(f"Память, использованная функцией: {sys.getsizeof(result)} байт")
        return result
    return wrapper

@memory_decorator
def create():
    return [1] * 100

create()


def make_read_and_decorator(source, n):
    offset = 0

    @memory_decorator
    def read():
        nonlocal offset
        chunk = source[offset: offset + n]
        offset += n
        return chunk
    return read

read8 = make_read_and_decorator("qwertyuiopadfghjkldfhjghidfgdhgidfgidhgdhighdg", 13)

for i in range(5):
    print(read8())