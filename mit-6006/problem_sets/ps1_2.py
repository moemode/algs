"""Problem Set 1 Problem 2
Given a data structure D that supports Sequence operations:
• D.build(X) in O(n) time, and
• D.insert at(i, x) and D.delete at(i), each in O(log n) time,
where n is the number of items stored in D at the time of the operation, 
describe algorithms to implement the following higher-level operations
 in terms of the provided lower-level operations. 
Each operation below should run in O(k log n) time. 
Recall, delete at returns the deleted item.
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


def move(elements: list[Any], fro: int, k: int, to: int):
    """Move the k items in D starting at index i, in order,
    to be in front of the item at index j.
    Assume that expression i ≤ j< i + k is false.

    Args:
        elements (list): The list of elements to modify.
        i (int): The starting index of the sublist to move.
        k (int): The number of items to move.
        j (int): The index of the item in front of which the sublist should be moved.

    Returns:
        None: This function modifies the input list in-place.

    Raises:
        IndexError: If the indices i, j, or i + k are out of range for the input list.
    """
    if fro < to:
        for _ in range(k):
            e = elements.pop(fro)
            elements.insert(to, e)
    elif to < fro:
        for i in range(k):
            e = elements.pop(fro + i)
            elements.insert(to + i, e)


if __name__ == "__main__":
    D1 = ["h", "a", "l", "o"]
    D2 = ["h", "a", "l", "o"]
    reverse(D1, 1, 3)
    print(D1)
    reverse(D2, 1, 3)
    print(D2)

    D3 = ["a", "b", "c", "d", "q", "q", "q"]
    move(D3, 2, 2, 5)
    print(D3)
    D4 = ["q", "q", "q", "a", "b", "c", "d"]
    move(D4, 4, 3, 2)
    print(D4)
