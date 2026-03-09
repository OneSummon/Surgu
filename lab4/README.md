# Вариант 11

## Условия задач

**Задача 1.** Функция, возвращающая все возможные результаты спортивных матчей с разницей в $k$.

Пример:
```
>>> get_matches_results(1)
[['0:0', '1:0'], ['0:0', '0:1']]

>>> get_matches_results(2)
[['0:0', '1:0', '2:0'], ['0:0', '1:0', '1:1', '2:1'], ['0:0', '1:0', '1:1', '1:2'], ...]
```

**Задача 2.** Функция для вычисления $x_i = \dfrac{x_{i-1}+1}{x_{i-1}+2}$, при $x_0 = 1$.

---

## Описание проделанной работы

Каждая задача реализована двумя способами: **с рекурсией** и **без рекурсии** (итеративно).

### Задача 1 - Результаты матчей

Матч начинается со счёта `0:0`, и каждый шаг один из счётчиков увеличивается на 1. Матч заканчивается, когда `max(a, b) == k`. Нужно вернуть все возможные пути от `0:0` до финального счёта.

**С рекурсией** - обход всевозможных счетов матчей через рекурсивную вспомогательную функцию `helper`:

```python
def get_matches_result_recursion(k: int):
    result = []

    def helper(a, b, path):
        if max(a, b) == k:
            result.append(path)
            return
        helper(a + 1, b, path + [f'{a + 1}:{b}'])
        helper(a, b + 1, path + [f'{a}:{b + 1}'])

    helper(0, 0, ['0:0'])
    return result
```

**Без рекурсии** - тот же обход, но через стек, созданный вручную (`stack`):

```python
def get_matches_result_no_recursion(k: int):
    result = []
    stack = [(0, 0, ['0:0'])]

    while stack:
        a, b, path = stack.pop()
        if max(a, b) == k:
            result.append(path)
        else:
            stack.append((a + 1, b, path + [f'{a + 1}:{b}']))
            stack.append((a, b + 1, path + [f'{a}:{b + 1}']))

    return result
```

### Задача 2 - Вычисление $x_i$

Последовательность задаётся формулой:

$$x_i = \frac{x_{i-1} + 1}{x_{i-1} + 2}, \quad x_0 = 1.$$

**С рекурсией** - функция вызывает себя до базового случая $i = 0$:

```python
def find_x_recursion(x, i):
    if i == 0:
        return x
    prev = find_x_recursion(x, i - 1)
    return (prev + 1) / (prev + 2)
```

**Без рекурсии** - простой цикл, обновляющий $x$ на каждом шаге:

```python
def find_x_no_recursion(x, i):
    for _ in range(i):
        x = (x + 1) / (x + 2)
    return x
```

---

## Результаты

### Задача 1

![Результаты функции get_matches_results](scrins/Screenshot%20from%202026-03-09%2018-38-03.png)

### Задача 2

![Результаты функции find_x](scrins/Screenshot%20from%202026-03-09%2018-39-21.png)

---

## Список использованных источников

1. [Python Docs - Recursion and stack frames](https://docs.python.org/3/reference/executionmodel.html)
2. [Writing mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
3. [Real Python - Recursion in Python](https://realpython.com/python-recursion/)