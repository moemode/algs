"""Problem 1-4. Brick Blowing
Porkland is a community of pigs who live in n houses lined up along one side of a long, 
straight street running east to west. 
Every house in Porkland was built from straw and bricks, 
but some houses were built with more bricks than others. 
One day, a wolf arrives in Porkland and all the pigs run inside their homes to hide. 
Unfortunately for the pigs, this wolf is extremely skilled at blowing down pig houses, 
aided by a strong wind already blowing from west to east. 
If the wolf blows in an easterly direction on a house containing b bricks, that house will fall down, 
along with every house east of it containing strictly fewer than b bricks. 
For every house in Porkland, the wolf wants to know its damage, 
i.e., the number of houses that would fall were he to blow on it in an easterly direction.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Element:
    """
    Represents an element in a list.

    Attributes:
        position (int): The position of the element in the list.
        n_smaller (int): The count of smaller numbers to the right of this element.
        number (int): The value of the element.
    """

    position: int
    n_smaller: int
    number: int


def build_elements(A: list[int]) -> list[Element]:
    """
    Build a list of elements based on the given input list.

    Args:
        A (list[int]): The input list of integers.

    Returns:
        list[Element]: A list of elements, where each element is created
        using the position and number from the input list.
    """
    return [Element(pos, 1, number) for pos, number in enumerate(A)]


def extract_n_smaller(A: list[Element]) -> list[int]:
    """
    Extracts the number of smaller elements for each element in the given list.

    Args:
        A (list[Element]): The input list of elements.

    Returns:
        list[int]: A list of integers representing the number of smaller elements for each element in A.
    """
    D = [1 for _ in A]
    for h in A:
        D[h.position] = h.n_smaller
    return D


def merge_sort(A: list[Element], a: int = 0, b: Optional[int] = None):
    """
    Sorts the elements in the list A[a:b] using the merge sort algorithm.

    Parameters:
        A (list[Element]): The list to be sorted.
        a (int): The starting index of the sublist to be sorted (inclusive).
        b (int): The ending index of the sublist to be sorted (exclusive).

    Returns:
        None: The function sorts the list in-place.
    """
    if b is None:
        b = len(A)
    if 1 < b - a:
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:c], A[c:b]
        merge(L, R, A, len(L), len(R), a, b)


def merge(
    L: list[Element],
    R: list[Element],
    A: list[Element],
    i: int,
    j: int,
    a: int,
    b: int,
):
    """
    Merge sorted L[:i] and R[:j] into A[a:b], update n_smaller for elements in left half

    Parameters:
    - L: A list of elements representing the left half of the merge
    - R: A list of elements representing the right half of the merge
    - A: A list of elements representing the merged result
    - i: An integer representing the index of the last element in L to be merged
    - j: An integer representing the index of the last element in R to be merged
    - a: An integer representing the starting index in A for the merged result
    - b: An integer representing the ending index in A for the merged result

    Returns:
    - None: A is modified
    """
    if a < b:
        if (j <= 0) or (i > 0 and L[i - 1].number > R[j - 1].number):
            A[b - 1] = L[i - 1]
            A[b - 1].n_smaller += j
            i = i - 1
        else:
            A[b - 1] = R[j - 1]
            j = j - 1
        merge(L, R, A, i, j, a, b - 1)


def smaller_to_right(A: list[int]):
    """
    For every number in A, calculate the number of smaller numbers to the right of it.

    Args:
        A (list[int]): The input list of integers.

    Returns:
        int: The number of smaller numbers to the right of each element in A.
    """
    H = build_elements(A)
    merge_sort(H)
    return extract_n_smaller(H)


get_damages = smaller_to_right


if __name__ == "__main__":
    A = [34, 57, 70, 19, 48, 2]
    print(get_damages(A))
