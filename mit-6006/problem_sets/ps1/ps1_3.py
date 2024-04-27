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


class BinderAPI:

    def __init__(self, elements: list[Any]):
        self.marks = {"A": None, "B": None}
        self.binder: Optional[BinderDatabase] = None
        self.elements = elements

    def a_is_left(self) -> bool:
        return self.marks["A"] <= self.marks["B"]

    def m_is_left(self, m: str):
        return (m == "A" and self.a_is_left()) or (m == "B" and not self.a_is_left())

    def left_mark(self) -> str:
        return "A" if self.a_is_left() else "B"

    def place_mark(self, i: int, m: str):
        self.marks[m] = i
        if self.marks_are_placed() and not self.binder:
            self.binder = BinderDatabase(
                self.elements,
                min(self.marks["A"], self.marks["B"]),
                max(self.marks["A"], self.marks["B"]),
            )
            self.elements = None

    def marks_are_placed(self) -> bool:
        return self.marks["A"] is not None and self.marks["B"] is not None

    def read_page(self, i: int):
        if self.marks_are_placed():
            return self.binder.read_page(i)
        else:
            return self.elements[i]

    def shift_mark(self, m: str, d: int):
        """
        a = self.marks["A"]
        b = self.marks["B"]
        new_a = self.marks["A"] + (d if m == "A" else 0)
        new_b = self.marks["B"] + (d if m == "B" else 0)
        if (a <= b) == (new_a <= new_b):
            # relative order of A, B is kept
            m_is_left = self.m_is_left(m)
            self.binder.shift(d, m_is_left)

        self.marks["A"] = new_a
        self.marks["B"] = new_b
        """
        a = self.marks["A"]
        b = self.marks["B"]
        new_a = self.marks["A"] + (d if m == "A" else 0)
        new_b = self.marks["B"] + (d if m == "B" else 0)
        left, right = min(a, b), max(a, b)
        new_left, new_right = min(new_a, new_b), max(new_a, new_b)
        print(self.binder.__str__(True))
        self.binder.shift(new_left - left, True)
        print(self.binder.__str__(True))
        self.binder.shift(new_right - right, False)
        print(self.binder.__str__(True))
        self.marks[m] += d

    def move_page(self, m: str):
        if not self.marks_are_placed():
            raise ValueError("Cannot move page unless both markers are placed.")
        from_left = self.m_is_left(m)
        if from_left:
            self.marks[self.left_mark()] -= 1
            self.binder.move_page_left_to_right()
        else:
            self.marks[self.left_mark()] += 1
            self.binder.move_page_right_to_left()


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

    def shift(self, d: int, left: bool):
        is_negative = d < 0
        for i in range(abs(d)):
            if left:
                if is_negative:
                    self.dec_left()
                else:
                    self.inc_left()
            else:
                if is_negative:
                    self.dec_right()
                else:
                    self.inc_right()

    def inc_left(self):
        if self.left >= self.right:
            raise IndexError("Cannot move left past right")
        # self.left < self.right
        move_to = self.before_left + 1
        move_from = self.between_start
        self.binder[move_to] = self.binder[move_from]
        self.binder[move_from] = None
        self.before_left += 1
        self.between_start += 1
        self.left += 1

    def inc_right(self):
        if self.right + 1 >= self.N:
            raise IndexError("Right marker is already behind last page.")
        # self.right < self.N - 1
        move_to = self.between_end + 1
        move_from = self.after_right
        self.binder[move_to] = self.binder[move_from]
        self.binder[move_from] = None
        self.between_end += 1
        self.after_right += 1
        self.right += 1

    def dec_left(self):
        if self.left - 1 < -1:
            raise IndexError("Left marker is already before first page.")
        move_to = self.between_start - 1
        move_from = self.before_left
        self.binder[move_to] = self.binder[move_from]
        self.binder[move_from] = None
        self.before_left -= 1
        self.between_start -= 1
        self.left -= 1

    def dec_right(self):
        if self.right <= self.left:
            raise IndexError("Can move right marker past left")
        move_to = self.after_right - 1
        move_from = self.between_end
        self.binder[move_to] = self.binder[move_from]
        self.binder[move_from] = None
        self.between_end -= 1
        self.after_right -= 1
        self.right -= 1

    def __str__(self, show_pointers=False):
        # visualize self.binder and the pointers, render None as X
        # render the four pointers in the line above
        pointers = [" "] * (len(self.binder) + 2)
        pointers[self.before_left + 1] = "A"
        pointers[self.between_start + 1] = "B"
        pointers[self.between_end + 1] = "C"
        pointers[self.after_right + 1] = "D"
        pointer_line = "-".join(pointers) + "\n" + "  "
        prefix = pointer_line if show_pointers else ""
        return prefix + "-".join([str(x) if x else "X" for x in self.binder])

    def move_page_left_to_right(self) -> None:
        """
        Take the page currently in front of bookmark left, and move it
        in front of the other bookmark in O(1) time.
        """
        if self.left == self.right:
            return
        if self.left == -1:
            raise IndexError("No page before left.")
        to = self.between_end + 1
        move_from = self.before_left
        self.binder[to] = self.binder[move_from]
        self.binder[move_from] = None
        self.before_left -= 1
        self.between_end += 1
        self.left -= 1

    def move_page_right_to_left(self) -> None:
        """
        Take the page currently in front of bookmark left, and move it
        in front of the other bookmark in O(1) time.
        """
        if self.left == self.right:
            return
        if self.left == -1:
            raise IndexError("No page before left.")
        to = self.before_left + 1
        move_from = self.between_end
        self.binder[to] = self.binder[move_from]
        self.binder[move_from] = None
        self.before_left += 1
        self.between_end -= 1
        self.left += 1


def binderdb_test():
    b = BinderDatabase([1, 2, 3, 4, 5, 6, 7], 2, 5)
    for i in range(7):
        print(b.read_page(i))
    print(b)
    b.inc_left()
    print(b)
    b.inc_right()
    print(b)
    try:
        b.inc_right()
    except:
        pass
    b.dec_left()
    print(b)
    b.dec_right()
    print(b)
    b.move_page_left_to_right()
    print(b.__str__(True))
    b.move_page_right_to_left()
    print(b.__str__(True))


if __name__ == "__main__":
    b = BinderAPI([1, 2, 3, 4, 5, 6, 7])
    b.place_mark(5, "A")
    b.place_mark(-1, "B")
    b.shift_mark("B", 7)
    print(b.binder.__str__(True))
    b.move_page("B")
    print(b.binder.__str__(True))

    """
    b.place_mark(5, "A")
    b.place_mark(2, "B")
    print(b.marks)
    b.move_page("A")
    print(b.marks)
    print(b.binder.__str__(True))
    b.shift_mark("B", -4)
    print(b.binder.__str__(True))
    b.shift_mark("B", 8)
    print(b.binder.__str__(True))
    """
