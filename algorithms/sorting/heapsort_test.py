import random

from algorithms.sorting.heapsort import sort


def test_heapsort():
    A = [random.randint(1, 100) for _ in range(20)]
    assert sort(A) == sorted(A)
