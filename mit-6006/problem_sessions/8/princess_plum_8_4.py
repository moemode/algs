"""
Problem 8-4. Princess Plum

Princess Plum is a video game character collecting mushrooms in a digital haunted forest.
The forest is an n × n square grid where each grid square contains either a tree, mushroom, 
or is empty. Princess Plum can move from one grid square to another if the two squares share 
an edge, but she cannot enter a grid square containing a tree. 

Princess Plum starts in the upper left grid square and wants to reach her home in the 
bottom right grid square. The haunted forest is scary, so she wants to reach home via a 
quick path: a route from start to home that goes through at most 2n − 1 grid squares 
(including start and home). 

If Princess Plum enters a square with a mushroom, she will pick it up. Let k be the maximum 
number of mushrooms she could pick up along any quick path, and let a quick path be optimal 
if she could pick up k mushrooms along that path.

This script defines the solution for finding such an optimal path.
"""

from math import inf
from operator import is_


def max_mushrooms(F):
    n = len(F)
    memo = {}

    def max_mushrooms_from(F, i=0, j=0):

        if (i, j) in memo:
            return memo[(i, j)]
        if F[i][j] == "t":
            r = -inf
        if i == n - 1 and j == n - 1:
            r = 1 if F[i][j] == "m" else 0
        else:
            # not tree, not goal
            is_mushroom = 1 if F[i][j] == "m" else 0
            down = max_mushrooms_from(F, i + 1, j) if i + 1 < n else -inf
            right = max_mushrooms_from(F, i, j + 1) if j + 1 < n else -inf
            r = is_mushroom + max(down, right)
        memo[(i, j)] = r
        return r

    return max_mushrooms_from(F), memo


def count_paths(F):
    """
    Count the number of distinct optimal paths in F starting from (0,0) and ending at (n-1,n-1).

    Args:
    F (list): A size-n direct access array of size-n direct access arrays.
             Each F[i][j] is either 't', 'm', or 'x' for tree, mushroom, or empty respectively.

    Returns:
    int: The number of distinct optimal paths in F.

    Examples:
    >>> F = [['x', 't', 'x'], ['x', 'm', 'x'], ['x', 'x', 'x']]
    >>> count_paths(F)
    2

    >>> F = [['x', 't', 'x'], ['x', 'm', 'x'], ['x', 't', 'x']]
    >>> count_paths(F)
    0
    """
    max_count, max_from = max_mushrooms(F)
    if max_count == -inf:
        return 0
    memo = {}

    def count_paths_from(F, i, j):
        if i == j and j == 0:
            return 1
        max_here = max_from[(i, j)]
        incoming_paths = 0
        if (i, j) in memo:
            return memo[(i, j)]
        if i >= 1:
            max_above = max_from[(i - 1, j)]
            is_connected = (max_here == max_above and F[i - 1][j] == "x") or (
                max_here + 1 == max_above and F[i - 1][j] == "m"
            )
            if is_connected:
                incoming_paths += count_paths_from(F, i - 1, j)
        if j >= 1:
            max_left = max_from[(i, j - 1)]
            is_connected = (max_here == max_left and F[i][j - 1] == "x") or (
                max_here + 1 == max_left and F[i][j - 1] == "m"
            )
            if is_connected:
                incoming_paths += count_paths_from(F, i, j - 1)
        memo[(i, j)] = incoming_paths
        return incoming_paths

    n = len(F)
    return count_paths_from(F, n - 1, n - 1)


if __name__ == "__main__":
    F = [["x", "t", "x"], ["x", "m", "x"], ["x", "x", "x"]]
    F2 = [["x", "m", "x"], ["m", "x", "x"], ["x", "x", "x"]]
    F3 = [["x", "t", "x"], ["t", "x", "x"], ["x", "x", "x"]]
    print(max_mushrooms(F))
    print(max_mushrooms(F2))
    print(max_mushrooms(F3))
    print(count_paths(F2))
