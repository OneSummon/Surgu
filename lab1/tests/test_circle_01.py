import package


def test_square():
    assert package.square(42) == 5541.7693
    assert package.square(1) == 3.1416
    assert package.square(2) == 12.5664

def test_square_zero():
    assert package.square(0) == 0

def test_square_negative():
    assert package.square(-5) is None


def test_incircle_inside():
    assert package.inCircle((1, 2), 5) is True


def test_incircle_outside():
    assert package.inCircle((10, 10), 5) is False


def test_incircle_border():
    assert package.inCircle((3, 4), 5) is False


def test_incircle_center():
    assert package.inCircle((0, 0), 5) is True


def test_incircle_zero_radius():
    assert package.inCircle((0, 0), 0) is False


def test_incircle_negative_radius():
    assert package.inCircle((1, 1), -5) is None