garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
def all_types(garden: tuple[str], meadow: tuple[str]):
    if not garden or not meadow:
        return None
    
    return set(garden + meadow)

# print(all_types(garden, meadow))

# выведите на консоль те, которые растут и там и там
def grow_everywhere(garden: tuple[str], meadow: tuple[str]):
    if not garden or not meadow:
        return None
    
    garden_set = set(garden)
    meadow_set = set(meadow)
    return garden_set & meadow_set

# print(grow_everywhere(garden, meadow))

# выведите на консоль те, которые растут в саду, но не растут на лугу
def only_garden(garden: tuple[str], meadow: tuple[str]):
    if not garden or not meadow:
        return None
    
    garden_set = set(garden)
    meadow_set = set(meadow)
    return garden_set - meadow_set

# print(only_garden(garden, meadow))

# выведите на консоль те, которые растут на лугу, но не растут в саду
def only_meadow(garden: tuple[str], meadow: tuple[str]):
    if not garden or not meadow:
        return None
    
    garden_set = set(garden)
    meadow_set = set(meadow)
    return meadow_set - garden_set

# print(only_meadow(garden, meadow))