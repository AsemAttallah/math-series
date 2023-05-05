import pytest
from series.series import fibonacci
from series.series import lucas

def test_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected
   
def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_ten():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected



def test_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected
   
def test_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_ten():
    actual = lucas(10)
    expected = 123
    assert actual == expected
