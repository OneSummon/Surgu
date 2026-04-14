import package

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

print(package.distance(sites))

radius = 42
print(package.square(radius))

point = (23, 34)
print(package.inCircle(point, radius))


my_family = ["Алмаз", "Мама", "Папа", "Злата", "Юля", "Бабушка", "Дедушка", "Симон(мопс)"]

my_family_height = [
    ["Алмаз", 177],
    ["Мама", 158],
    ["Папа", 160],
    ["Злата", 140],
    ["Юля", 120],
    ["Бабушка", 150],
    ["Дедушка", 173],
    ["Симон(мопс)", 30],
]
print(package.height_father(my_family, my_family_height))
print(package.sum_height(my_family, my_family_height))


zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
birds = ['rooster', 'ostrich', 'lark', ]
package.add_birds(birds)
print(birds)

print(package.find_animal(zoo, "lion"))
print(package.find_animal(zoo, "monkey"))


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

print(package.sum_3_songs_list(violator_songs_list, 'Halo', 'Enjoy the Silence', 'Clean'))
print(package.sum_3_songs_dict(violator_songs_dict, 'Sweetest Perfection', 'Policy of Truth', 'Blue Dress'))


secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
print(package.decode(secret_message))


garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
print(package.all_types(garden, meadow))
print(package.grow_everywhere(garden, meadow))
print(package.only_garden(garden, meadow))
print(package.only_meadow(garden, meadow))


sweets = {
    'карамель': [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'пятерочка', 'price': 46.99},
        {'shop': 'магнит', 'price': 41.99},
    ],
    'пирожное': [
        {'shop': 'ашан', 'price': 67.99},
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ],
}
package.store_2_with_min_prices(sweets)



goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
print(package.table_cost(store, goods))
print(package.sofa_cost(store, goods))
print(package.chair_cost(store, goods))