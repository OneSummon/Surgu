import functools

def log(func=None, *, prefix="LOG"):

    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"[{prefix}] вызов {fn.__name__}{args}")

            result = fn(*args, **kwargs)

            print(f"[{prefix}] результат --> {result}")

            return result
        return wrapper
    
    if func is not None:
        return decorator(func)
    
    return decorator

# пример 1, просто @log
@log
def simple_func_multiply(a: int | float, b: int | float):
    print(a * b)

simple_func_multiply(4, 6)


#пример 2, @log(prefix="MATH")
@log(prefix="MATH")
def simple_func_sum(a: int | float, b: int | float):
    print(a + b)

simple_func_sum(60, 34)


#пример 3 с рекурсивной функцией и кастомным префиксом
@log(prefix="FIB_LOG")
def simple_func_fib(n: int):
    if n <= 1:
        return n
    raw = simple_func_fib.__wrapped__ # вызов без декоратора внутри для того, чтобы декоратор не срабатывал на каждом шаге рекурсии
    res = raw(n - 1) + raw(n - 2)
    print(res)
    
    return res

simple_func_fib(10)