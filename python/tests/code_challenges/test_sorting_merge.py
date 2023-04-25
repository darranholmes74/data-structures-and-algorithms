import pytest
from code_challenges.sorting.merge import mergesort


def test_1():
    arr1 = [8, 4, 23, 42, 16, 15]
    mergesort(arr1)
    assert arr1 == [4, 8, 15, 16, 23, 42]


def test_2():
    arr2 = [20, 18, 12, 8, 5, -2]
    mergesort(arr2)
    assert arr2 == [-2, 5, 8, 12, 18, 20]


def test_3():
    arr3 = [5, 12, 7, 5, 5, 7]
    mergesort(arr3)
    assert arr3 == [5, 5, 5, 7, 7, 12]


def test_4():
    arr4 = [2, 3, 5, 7, 13, 11]
    mergesort(arr4)
    assert arr4 == [2, 3, 5, 7, 11, 13]


