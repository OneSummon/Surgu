import package

# 1 Список
@package.memory_decorator
def list_of_squares(n: int) -> list:
    return [x ** 2 for x in range(n)]

# 2 генератор
@package.memory_decorator
def generator_of_squares(n: int):
    return list(x ** 2 for x in range(n))


# 3 Числа Фибоначчи рекурсией — память растёт из-за стека вызовов
@package.memory_decorator
def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# 4 Матричное умножение через вложенные списки
@package.memory_decorator
def matrix_multiply(size: int) -> list:
    a = [[i * j for j in range(size)] for i in range(size)]
    b = [[i + j for j in range(size)] for i in range(size)]
    result = [[sum(a[i][k] * b[k][j] for k in range(size))
               for j in range(size)] for i in range(size)]
    return result


# 5 Частоты слов — словарь растёт с текстом
@package.memory_decorator
def word_frequency(text: str) -> dict:
    freq = {}
    for word in text.split():
        freq[word] = freq.get(word, 0) + 1
    return freq