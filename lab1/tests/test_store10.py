import package

def test_table_cost():
    goods = {'Лампа': '12345', 'Стол': '23456', 'Диван': '34567', 'Стул': '45678'}
    store = {
        '12345': [{'quantity': 27, 'price': 42}],
        '23456': [{'quantity': 22, 'price': 510}, {'quantity': 32, 'price': 520}],
        '34567': [{'quantity': 2, 'price': 1200}, {'quantity': 1, 'price': 1150}],
        '45678': [{'quantity': 50, 'price': 100}, {'quantity': 12, 'price': 95}, {'quantity': 43, 'price': 97}],
    }
    assert package.table_cost(store, goods) == "Стол - 54 шт, стоимость 27860 руб"

def test_sofa_cost():
    goods = {'Стол': '23456', 'Диван': '34567', 'Стул': '45678'}
    store = {
        '34567': [{'quantity': 2, 'price': 1200}, {'quantity': 1, 'price': 1150}],
    }
    assert package.sofa_cost(store, goods) == "Диван - 3 шт, стоимость 3550 руб"

def test_chair_cost():
    goods = {'Стул': '45678'}
    store = {
        '45678': [{'quantity': 50, 'price': 100}, {'quantity': 12, 'price': 95}, {'quantity': 43, 'price': 97}],
    }
    assert package.chair_cost(store, goods) == "Стул - 105 шт, стоимость 10311 руб"

def test_costs_with_empty_input():
    assert package.table_cost({}, {}) is None
    assert package.sofa_cost(None, {}) is None
    assert package.chair_cost({}, None) is None