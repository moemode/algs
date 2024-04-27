"""
Sisa Limpson is a very organized second grade student who keeps 
all of her course notes on individual pages stored in a three-ring binder. 
If she has n pages of notes in her binder, the first page is at index 0 and 
the last page is at index n − 1. While studying, 
Sisa often reorders pages of her notes. 
To help her reorganize, she has two bookmarks, A and B, 
which help her keep track of locations in the binder.
Describe a database to keep track of pages in Sisa’s binder, 
supporting the following operations, 
where n is the number of pages in the binder at the time of the operation. 
Assume that both bookmarks will be placed in the binder 
before any shift or move operation can occur,
and that bookmark A will always be at a lower index than B. 
For each operation, state whether your running time is worst-case or amortized.
"""

from typing import Optional, Any
from collections import deque


class BinderDatabase:
    def __init__(self, elements: list[Any], left: int, right: int):
        # marker is between index left, left+1, legal values -1,.., N-1
        N = len(elements)
        self.N = N
        self.binder = [None] * 3 * self.N
        self.left = left
        self.right = right
        # index of last element before left in self.binder
        before_left = left
        # index of first element between left and right in self.binder
        between_start = left + (N + 1)
        # index of last element between left and right in self.binder
        between_end = between_start + (right - left - 1)
        # index of first element after right self.binder
        after_right = between_end + (N + 1)
        self.binder[: before_left + 1] = elements[: left + 1]
        self.binder[between_start : between_end + 1] = elements[
            left + 1 : left + 1 + (right - left)
        ]
        self.binder[after_right:] = elements[right + 1 :]
        self.before_left = before_left
        self.between_start = between_start
        self.between_end = between_end
        self.after_right = after_right

    def n_in_between(self):
        return self.between_end - self.between_start + 1

    def read_page(self, i: int):
        """Return the page at index i in O(1) time."""
        if i < 0 or i >= self.N:
            raise IndexError("Page does not exist.")
        if i <= self.before_left:
            return self.binder[i]
        i = i - (self.before_left + 1)
        if i < self.n_in_between():
            return self.binder[self.between_start + i]
        i -= self.n_in_between()
        return self.binder[self.after_right + i]

    def __str__(self):
        # visualize self.binder and the pointers
        return "-".join([str(x) for x in self.binder])

    def shift_mark(self, m: str, d: int) -> None:
        """
        Take the bookmark m ∈ {A,B}, currently in front of the page at index i,
        and move it in front of the page at index i + d for d ∈ {−1, 1} in O(1) time.
        """
        pass

    def move_page(self, m: str) -> None:
        """
        Take the page currently in front of bookmark m ∈ {A,B}, and move it
        in front of the other bookmark in O(1) time.
        """
        pass


if __name__ == "__main__":
    b = BinderDatabase([1, 2, 3, 4, 5, 6, 7], 2, 5)
    for i in range(7):
        print(b.read_page(i))
    print(b)
