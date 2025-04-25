'''
Tests n_sum implementation.
'''

from main import n_sum

def test_n_sum_two_sum():
    arr = [1, 2, 3, 4, 5]
    k = 6
    result = n_sum(arr, 2, k)
    expected = [[0, 4], [1, 3]]
    assert result == expected

def test_n_sum_three_sum():
    arr = [1, 2, 3, 4, 5]
    k = 9
    result = n_sum(arr, 3, k)
    expected = [[0, 2, 4], [1, 2, 3]]
    assert result == expected

def test_n_sum_four_sum():
    arr = [1, 2, 3, 4, 5, 6]
    k = 15
    result = n_sum(arr, 4, k)
    expected = [[0, 2, 3, 5], [0, 1, 4, 5], [1, 2, 3, 4]]
    assert result == expected

def test_n_sum_empty():
    arr = []
    k = 5
    result = n_sum(arr, 3, k)
    assert result == []

def test_n_sum_not_possible():
    arr = [1, 1, 1]
    k = 10
    result = n_sum(arr, 3, k)
    assert result == []
