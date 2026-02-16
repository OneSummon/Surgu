#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'карамель': [
        # TODO тут с клавиатуры введите магазины и цены (можно копипастить ;)
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'пятерочка', 'price': 46.99},
        {'shop': 'магнит', 'price': 41.99},
    ],
    # TODO тут с клавиатуры введите другую сладость и далее словарь магазинов
    'пирожное': [
        {'shop': 'ашан', 'price': 67.99},
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ],
}
# Указать надо только по 2 магазина с минимальными ценами
for sweet in sweets:
    print(f"{sweet}")
    caramel_price = []
    for i in range(len(sweets[f"{sweet}"])):
        caramel_price.append(sweets[f"{sweet}"][i]["price"])
    min_sum_caramel = min(caramel_price)

    for i in range(len(sweets[f"{sweet}"])):
        if sweets[f"{sweet}"][i]["price"] == min_sum_caramel:
            print(sweets[f"{sweet}"][i])
            caramel_price.remove(sweets[f"{sweet}"][i]["price"])

    min_sum_caramel = min(caramel_price)

    for i in range(len(sweets[f"{sweet}"])):
        if sweets[f"{sweet}"][i]["price"] == min_sum_caramel:
            print(sweets[f"{sweet}"][i])