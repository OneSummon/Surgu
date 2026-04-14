import package

def test_all_types():
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
    expected = {'ромашка', 'роза', 'одуванчик', 'гладиолус', 'подсолнух', 'клевер', 'мак'}
    assert package.all_types(garden, meadow) == expected

def test_all_types_empty_garden():
    assert package.all_types((), ('клевер',)) is None

def test_grow_everywhere():
    garden = ('ромашка', 'роза', 'одуванчик', 'гладиолус')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'мак')
    assert package.grow_everywhere(garden, meadow) == {'ромашка', 'одуванчик'}

def test_only_garden():
    garden = ('ромашка', 'роза', 'одуванчик', 'гладиолус')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'мак')
    assert package.only_garden(garden, meadow) == {'роза', 'гладиолус'}

def test_only_meadow():
    garden = ('ромашка', 'роза', 'одуванчик', 'гладиолус')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'мак')
    assert package.only_meadow(garden, meadow) == {'клевер', 'мак'}