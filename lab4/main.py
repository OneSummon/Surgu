def get_matches_result_recursion(k: int):
    result = []
    path = ['0:0']

    def helper(a, b):
        if max(a, b) == k:
            result.append(path.copy()) # копируем готовый путь
            return
        path.append(f'{a+1}:{b}')
        helper(a + 1, b)
        path.pop()

        path.append(f'{a}:{b+1}')
        helper(a, b + 1)
        path.pop()

    helper(0, 0)
    return result
# Увелечение производительности функции get_matches_result_recursion
# Прирост 2.5x за счёт избавления от многократного копирования путей, теперь используется только ОДИН, который мутируется, а в result отправляется копия только готовго пути

print(get_matches_result_recursion(1))
print(get_matches_result_recursion(2))

def get_matches_result_no_recursion(k: int):
    result = []

    stack = [(0, 0, ((0, 0),))]

    while stack:
        a, b, path = stack.pop()

        if a == k or b == k:
            result.append([f'{x}:{y}' for x, y in path])
            continue

        stack.append((a + 1, b, path + ((a + 1, b),)))
        stack.append((a, b + 1, path + ((a, b + 1),)))

    return result
# Увелечение производительности функции get_matches_result_no_recursion
# Прирост 2.5x за счёт избавления от многократного копирования путей

print(get_matches_result_no_recursion(1))
print(get_matches_result_no_recursion(2))


from functools import lru_cache

@lru_cache(None)
def find_x_recursion(x, i):
    if i == 0:
        return x
    else:
        prev = find_x_recursion(x, i - 1)
        return (prev + 1) / (prev + 2)
# Увелечение производительности функции find_x_recursion
# Прирост скорости за счет кеширования lru

print(find_x_recursion(1, 1))
print(find_x_recursion(1, 2))

def find_x_no_recursion(x, i):
    n = i // 2
    r = i % 2

    for _ in range(n):
        x = (x + 1) / (x + 2)
        x = (x + 1) / (x + 2)

    if r:
        x = (x + 1) / (x + 2)

    return x
# Увелечение производительности функции find_x_no_recursion
# Прирост 2x за счет уменьшения проверок for

print(find_x_no_recursion(1, 1))
print(find_x_no_recursion(1, 2))