#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

for i in range(len(sites)):
    sities_keys = list(sites.keys())
    next_i = (i + 1) % len(sites)
    
    distance = {"distance" : ((sites[sities_keys[i]][0] - sites[sities_keys[next_i]][0]) ** 2 + (sites[sities_keys[i]][1] - sites[sities_keys[next_i]][1]) ** 2) ** 0.5}
    distances[f"{sities_keys[i]} -> {sities_keys[next_i]}"] = distance

print(distances)