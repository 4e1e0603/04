# -*- coding: utf-8 -*-


"""
Bubble Sort si algotrithm for sorting. 

Run the tests with `python bubble_sort`.
"""


import doctest as dt
from typing import Sequence, Tuple, TypeVar


__all__ = ("bubble_sort",)


Comparable = TypeVar("Comparable")


def bubble_sort(*sequence: Sequence[Comparable]) -> Tuple[Comparable]:
    """
    Sort the given sequence of items with *bubble sort* algorithm.
    
    Time complexity is O(n^2).
    
    The sequence items must be comparable with `<` operator.

    Examples:
        >>> bubble_sort(1, 2, 3, 4, 5)
        (1, 2, 3, 4, 5)
        >>> bubble_sort(5, 4, 3, 2, 1)
        (1, 2, 3, 4, 5)
        >>> bubble_sort(4, 2, 1, 3, 5)
        (1, 2, 3, 4, 5)
    """
    length = len(sequence)
    result = [x for x in sequence]

    # Sort the sequence (in-place) only when there is  more the one item.
    if length > 1:
        for i in range(length - 1):
            for j in range(length - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]

    return tuple(result)


if __name__ == "__main__":
    print(dt.testmod(verbose=True))
