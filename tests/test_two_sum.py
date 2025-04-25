'''
Tests two_sum implementation.
'''

from main import two_sum

def test_two_sum_basic():
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 9
    result = two_sum(arr, 0, k)
    expected = [(1, 6), (2, 5), (3, 4)]
    assert result == expected

def test_two_sum_empty():
    arr = []
    k = 5
    result = two_sum(arr, 0, k)
    assert result == []

def test_two_sum_no_pairs():
    arr = [1, 2, 3]
    k = 10
    result = two_sum(arr, 0, k)
    assert result == []
