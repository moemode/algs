"""Problem Set 1 Problem 2
"""

from typing import Any


def reverse(elements: list[Any], i: int, k: int):
    """Reverse in D the order of the k items starting
    at index i (up to index i + k - 1).
    Recursive approach.

    Args:
        elements (list): The list of elements to reverse.
        i (int): The starting index of the sublist to reverse.
        k (int): The number of items to reverse.
    """
    if k > 0:
        e = elements.pop(i)
        elements.insert(i + k - 1, e)
        reverse(elements, i, k - 1)


def reverse_iter(elements: list[Any], i: int, k: int):
    """Reverse in D the order of the k items starting
    at index i (up to index i + k - 1).
    Loop approach.

    Args:
        elements (list): The list of elements to reverse.
        i (int): The starting index of the sublist to reverse.
        k (int): The number of items to reverse.
    """
    for j in range(k):
        e = elements.pop(i)
        elements.insert(i + k - 1 - j, e)


if __name__ == "__main__":
    D1 = ["h", "a", "l", "o"]
    D2 = ["h", "a", "l", "o"]
    reverse(D1, 1, 3)
    print(D1)
    reverse(D2, 1, 3)
    print(D2)
