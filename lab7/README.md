# Отчёт. Лабораторная работа №7

## Условия задач

1. Создать пакет, содержащий 3 модуля на основе лабораторных работ №№ 4–6.
2. Написать запускающий модуль на основе [Typer](https://typer.tiangolo.com/), который позволит выбирать и настраивать параметры запуска логики из пакета.

---

## Описание проделанной работы

### Структура проекта

```
lab7/
├── README.md        # Документация
├── env              # Виртуальное окружение (Создаете сами!)
├── screens          # Скриншоты выполнения кода
├── main.py          # Точка входа, Typer-приложение
└── package/
    ├── __init__.py  # Импорт всех функций пакета
    ├── lab4.py      # get_matches_result_recursion
    ├── lab5.py      # memory_decorator
    └── lab6.py      # pi_leibniz
```
### Виртуальное окружение

- Обязательно создайте виртуальное окружение
```
python -m venv env
```
- Активируйте виртуальное окружение
```
source env/bin/activate
```
- Установите typer
```
pip install typer
```


### Пакет `package`

Пакет объединяет функции из трёх предыдущих лабораторных работ. Файл `__init__.py` экспортирует их наружу:

```python
from .lab4 import get_matches_result_recursion
from .lab5 import memory_decorator
from .lab6 import pi_leibniz
```

Это позволяет в `main.py` обращаться к любой функции через `package.<имя>`.

### Запускающий модуль `main.py`

Приложение построено на библиотеке **Typer** - каждая команда CLI соответствует одной функции из пакета:

```python
import typer
import package

app = typer.Typer()

@app.command()
def get_matches_result(k: int):
    result = package.get_matches_result_recursion(k)
    print(result)

@app.command()
def use_memory_decorator():
    @package.memory_decorator
    def example_func_create():
        return [1] * 100

    example_func_create()

@app.command()
def get_pi_numbers(iterations: int):
    gen_pi_numbers = package.pi_leibniz(iterations)

    for i in gen_pi_numbers:
        print(i)

if __name__ == "__main__":
    app()
```

### Команды CLI

| Команда | Параметр | Описание |
|---|---|---|
| `get-matches-result` | `k: int` | Все возможные результаты матча с разницей в `k` |
| `use-memory-decorator` | - | Демонстрация декоратора меморизации эксперементальной функции example_func_create|
| `get-pi-numbers` | `iterations: int` | Генерация приближений $\pi$ по формуле Лейбница |

Эксперементальная функция:
```python
def example_func_create():
        return [1] * 100
```

Запуск, например:
```bash
python main.py get-matches-result 2
python main.py get-pi-numbers 10
python main.py use-memory-decorator
```

---

## Результаты

![Код запускающего модуля main.py в VS Code](/lab7/screens/2026-03-20_12-00.png)

---

## Список использованных источников

1. [Typer - official documentation](https://typer.tiangolo.com/)
2. [Python Docs - Packages](https://docs.python.org/3/reference/simple_stmts.html#import)
3. [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
4. [Writing mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)