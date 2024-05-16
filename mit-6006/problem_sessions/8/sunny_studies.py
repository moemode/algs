"""
Module: sunny_studies

This module contains a function to help Tim the Beaver 
decide which days to study and which days to play outside
to maximize his happiness based on the weather forecast. 
The algorithm ensures that Tim never plays outside 
for more than two consecutive days, 
while maximizing the total happiness over a given number of days.
"""

from typing import List


def maximize_happiness_memo(temperatures: List[int]) -> int:
    """
    Determines the maximum happiness Tim the Beaver can achieve
    given the temperatures forecast for the next n days.
    Tim cannot play outside for more than two consecutive days.

    Parameters:
    temperatures (List[int]): A list of integers
        representing the temperature forecast for the next n days.

    Returns:
    int: The maximum achievable happiness over the n days.
    """
    # Implementation to be added by the user
    maximize_happiness_from.memo = {}
    return maximize_happiness_from(temperatures, 0)


def maximize_happiness_from(temperatures: List[int], i: int = 0) -> int:
    """
    A helper function to recursively determine the maximum happiness Tim can achieve starting from day i.

    Parameters:
    temperatures (List[int]): A list of integers representing the temperature forecast for the next n days.

    i (int): The current day index from which to start calculating the maximum happiness.

    Returns:
    int: The maximum achievable happiness from day i to the end of the list.
    """
    n = len(temperatures)
    if i == n:
        return 0
    if i in maximize_happiness_from.memo:
        return maximize_happiness_from.memo[i]
    choose_only_i = temperatures[i] + maximize_happiness_from(
        temperatures, min(n, i + 2)
    )
    next_temperature = temperatures[i + 1] if i + 1 < n else 0
    # if no next element exists, this is identical to choose_only_i
    choose_i_and_next = (
        temperatures[i]
        + next_temperature
        + maximize_happiness_from(temperatures, min(n, i + 3))
    )
    leave_i = maximize_happiness_from(temperatures, i + 1)
    ret = max(choose_only_i, choose_i_and_next, leave_i)
    maximize_happiness_from.memo[i] = ret
    return ret


def maximize_happiness_iterative(temperatures: List[int]) -> dict:
    """
    Determines the maximum happiness Tim the Beaver can achieve
    given the temperatures forecast for the next n days.
    Tim cannot play outside for more than two consecutive days.

    Parameters:
    temperatures (List[int]): A list of integers
        representing the temperature forecast for the next n days.

    Returns:
    int: The maximum achievable happiness over the n days.
    """
    # Implementation to be added by the user
    n = len(temperatures)
    happiness = {n: 0}
    for i in reversed(range(n)):
        choose_only_i = temperatures[i] + happiness[min(n, i + 2)]
        next_temperature = temperatures[i + 1] if i + 1 < n else 0
        # if no next element exists, this is identical to choose_only_i
        choose_i_and_next = (
            temperatures[i] + next_temperature + happiness[min(n, i + 3)]
        )
        leave_i = happiness[i + 1]
        happiness[i] = max(choose_only_i, choose_i_and_next, leave_i)
    return happiness[0]


if __name__ == "__main__":
    print(maximize_happiness_iterative([2, 4, -1, 3, 3, 100]))
