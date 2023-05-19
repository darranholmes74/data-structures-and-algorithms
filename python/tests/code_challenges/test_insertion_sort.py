from code_challenges.insertion_sort import insertion_sort


def test_insertion_sort():
    # Test sorting an empty list
    assert insertion_sort([]) == []


def test_one_element():
    # Test sorting a list with one element
    assert insertion_sort([1]) == [1]


def test_two_elements():

    # Test sorting a list with two elements
    assert insertion_sort([2, 1]) == [1, 2]


def test_repeated_elements():
    # Test sorting a list with repeated elements
    assert insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]


def test_negative_elements():
    # Test sorting a list with negative elements
    assert insertion_sort([-3, 1, 4, -1, 5, -9, 2, 6, 5]) == [-9, -3, -1, 1, 2, 4, 5, 5, 6]


def test_fully_sorted():
    # Test sorting a list with all elements already sorted
    assert insertion_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_reverse_order():
    # Test sorting a list with elements in reverse order
    assert insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_all_same():
    # Test sorting a list with elements that are all the same
    assert insertion_sort([2, 2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2, 2]
