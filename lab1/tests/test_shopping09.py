import package
from io import StringIO
from contextlib import redirect_stdout

def test_store_2_with_min_prices(capsys):
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
    captured = capsys.readouterr()
    assert "карамель" in captured.out
    assert "магнит" in captured.out
    assert "ашан" in captured.out
    assert "пирожное" in captured.out
    assert "пятерочка" in captured.out
    assert "магнит" in captured.out

def test_store_2_with_min_prices_empty():
    assert package.store_2_with_min_prices({}) is None