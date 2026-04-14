goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

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

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
# print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')


def table_cost(store: dict, goods: dict):
    if not store or not goods:
        return None
    
    table_cost_1 = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
    table_cost_2 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
    return f"Стол - {store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']} шт, стоимость {table_cost_1 + table_cost_2} руб"

# print(table_cost(store, goods))

def sofa_cost(store: dict, goods: dict):
    if not store or not goods:
        return None
    
    sofa_cost_1 = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
    sofa_cost_2 = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
    return f"Диван - {store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']} шт, стоимость {sofa_cost_1 + sofa_cost_2} руб"

# print(sofa_cost(store, goods))

def chair_cost(store: dict, goods: dict):
    if not store or not goods:
        return None
    
    chair_cost_1 = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
    chair_cost_2 = store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
    chair_cost_3 = store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
    return f"Стул - {store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] + store[goods['Стул']][2]['quantity']} шт, стоимость {chair_cost_1 + chair_cost_2 + chair_cost_3} руб"

# print(chair_cost(store, goods))