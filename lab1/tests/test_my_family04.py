import package

def test_height_father():
    family = ["A", "Папа", "B"]
    heights = [["A", 100], ["Папа", 180], ["B", 120]]
    assert package.height_father(family, heights) == "Рост отца - 180 см"

def test_height_father_none():
    assert package.height_father(None, None) is None

def test_height_father_not_found():
    family = ["A", "B"]
    heights = [["A", 100], ["B", 120]]
    assert package.height_father(family, heights) is None

def test_sum_height():
    family = ["A", "B"]
    heights = [["A", 100], ["B", 150]]
    assert package.sum_height(family, heights) == "Общий рост моей семьи - 250 см"

def test_sum_height_none():
    assert package.sum_height(None, None) is None

def test_sum_height_empty():
    assert package.sum_height([], []) == "Общий рост моей семьи - 0 см"