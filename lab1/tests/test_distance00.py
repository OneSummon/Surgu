import package

def test_distance_empty():
    assert package.distance({}) is None

def test_distance_two_points():
    sites = {
        "A": (0, 0),
        "B": (3, 4)
    }
    result = package.distance(sites)
    assert result["A -> B"]["distance"] == 5
    assert result["B -> A"]["distance"] == 5

def test_distance_three_points():
    sites = {
        "A": (0, 0),
        "B": (3, 4),
        "C": (6, 8)
    }
    result = package.distance(sites)
    assert result["A -> B"]["distance"] == 5
    assert result["B -> C"]["distance"] == 5
    assert result["C -> A"]["distance"] == 10

def test_distance_one_point():
    sites = {
        "A": (2, 3)
    }
    result = package.distance(sites)
    assert result["A -> A"]["distance"] == 0