#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# TODO здесь ваш код
all_time_songs = 0
for i in range(len(violator_songs_list)):
    if violator_songs_list[i][0] in ['Halo', 'Enjoy the Silence', 'Clean']:
        all_time_songs += violator_songs_list[i][1]

print(f"Три песни звучат {round(all_time_songs, 2)} минут")


# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# TODO здесь ваш код
vsd_name = list(violator_songs_dict.keys())
vsd_values = list(violator_songs_dict.values())
time_3_songs = 0
other_times = 0

for i in range(len(violator_songs_dict)):
    if vsd_name[i] in ['Sweetest Perfection', 'Policy of Truth','Blue Dress']:
        time_3_songs += vsd_values[i]
    else:
        other_times += vsd_values[i]

print(round(time_3_songs, 2))
print(f"А другие три песни звучат {round(other_times, 2)} минут")