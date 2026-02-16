#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo.insert(1, "bear")
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
for bird in birds:
    zoo.append(bird)
print(zoo)

# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
zoo.remove("elephant")
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
idx_lion = zoo.index("lion")
idx_lark = zoo.index('lark')
print(idx_lion + 1)
print(idx_lark + 1)