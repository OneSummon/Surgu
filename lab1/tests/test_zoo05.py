import package

def test_add_birds():
    package.zoo_05.zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    birds = ['rooster', 'ostrich', 'lark']
    assert package.add_birds(birds) is None
    assert package.zoo_05.zoo == ['lion', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark']

def test_add_birds_empty():
    package.zoo_05.zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    assert package.add_birds([]) is None
    assert package.zoo_05.zoo == ['lion', 'kangaroo', 'elephant', 'monkey']

def test_find_animal():
    zoo = ['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']
    assert package.find_animal(zoo, "lion") == 1
    assert package.find_animal(zoo, "lark") == 7
    assert package.find_animal(zoo, "elephant") is None

def test_find_animal_empty_zoo():
    assert package.find_animal([], "lion") is None