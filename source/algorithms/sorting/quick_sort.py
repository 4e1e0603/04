# -*- coding: utf-8 -*-


"""
Algotrithms: Sorting 

Run the tests with `python quick_sort`.
"""


from typing import Sequence


def quick_sort(*sequence: Sequence):
    """
    Sort the given sequence with *quick sort* algorithm.

    Examples:
        >>> quick_sort(5, 4, 3, 2, 1)
        (1, 2, 3, 4, 5)
    """
    result = [x for x in sequence]
    return NotImplemented


if __name__ == "__main__":
    print(quick_sort(5, 4, 3, 2, 1))
