from typing import List
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

zoo.insert(1, "bear")
# print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль

def add_birds(birds: List[str]):
    for bird in birds:
        zoo.append(bird)

# add_birds(birds)
# print(birds)

# уберите слона
#  и выведите список на консоль

zoo.remove("elephant")
# print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

def find_animal(zoo: List[str], animal: str):
    idx_animal = zoo.index(animal)
    return idx_animal + 1

# print(find_animal(zoo, "lion"))
# print(find_animal(zoo, "lark"))