import pytest
from series.series import fibonacci
from series.series import lucas
from series.series import sum_series

def test_zero_fab():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected
   
def test_one_fab():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_two_fab():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_three_fab():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_ten_fab():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected



def test_zero_luc():
    actual = lucas(0)
    expected = 2
    assert actual == expected
   
def test_one_luc():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_two_luc():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_three_luc():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_ten_luc():
    actual = lucas(10)
    expected = 123
    assert actual == expected



def test_zero_sum():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_one_sum():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_four_sum():
    actual = sum_series(4)
    expected = 3
    assert actual == expected


def test_zero_sum_2():
    actual = sum_series(0,1,0)
    expected = 1
    assert actual == expected

def test_one_sum_2():
    actual = sum_series(1,1,0)
    expected = 0
    assert actual == expected

def test_four_sum_2():
    actual = sum_series(4,1,0)
    expected = 2
    assert actual == expected

def test_two_sum_2():
    actual = sum_series(2,3,4)
    expected = 7
    assert actual == expected

def test_two_sum_3():
    actual = sum_series(2,1,1)
    expected = 2
    assert actual == expected

def test_two_sum_4():
    actual = sum_series(5,5,5)
    expected = 40
    assert actual == expected
