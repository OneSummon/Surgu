import math
import pytest
from main import pi_leibniz


def test_length():
    result = list(pi_leibniz(5))
    assert len(result) == 5


def test_first_values():
    result = list(pi_leibniz(3))
    assert result[0] == 4.0
    assert result[1] == 4.0 - 4.0/3
    assert result[2] == 4.0 - 4.0/3 + 4.0/5


def test_convergence():
    result = list(pi_leibniz(10000))
    assert abs(result[-1] - math.pi) < 0.01


def test_generator_type():
    gen = pi_leibniz(5)
    assert hasattr(gen, '__iter__')
    assert hasattr(gen, '__next__')


def test_zero_iterations():
    result = list(pi_leibniz(0))
    assert result == []


def test_negative_iterations():
    result = list(pi_leibniz(-5))
    assert result == []