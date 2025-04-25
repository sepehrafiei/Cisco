'''
Tests three_sum implementation.
'''

from main import three_sum

def test_three_sum_basic():
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 12
    result = three_sum(arr, k)
    expected = [(0, 4, 6), (1, 3, 6), (1, 4, 5), (2, 3, 5)]
    assert result == expected

def test_three_sum_empty():
    arr = []
    k = 10
    result = three_sum(arr, k)
    assert result == []

def test_three_sum_no_triplets():
    arr = [1, 2, 4]
    k = 20
    result = three_sum(arr, k)
    assert result == []
