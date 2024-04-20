import unittest

"""
Problem 0-6. 
An increasing subarray of an integer array is any consecutive sequence of array integers whose values strictly increase.
Write Python function count long subarrays(A) which accepts Python Tuple A=(a0,a1,...,an-1) of n> 0 positive integers, 
and returns the number of longest increasing subarrays of A, i.e., the number of increasing subarrays with length at least as large as every other increasing subarray. 
For example, if A = (1,3,4,2,7,5,6,9,8), your program should return 2 since the maximum length of any increasing subarray of A is three 
and there are two increasing subarrays with that length: specifically, subarrays (1,3,4) and (5,6,9). 
"""


def count_long_subarrays(numbers: tuple) -> int:
    """
    Counts the number of longest increasing subarrays in the given tuple.
    A longest increasing subarray is defined as any consecutive sequence of integers within the tuple where the values strictly increase.
    This must take into account that there can be multiple longest increasing subarrays of the same length,
    Args:
        numbers (tuple): A tuple of numbers.

    Returns:
        int: The number of longest increasing subarrays.
    """
    if len(numbers) == 0:
        return 0
    i = 0
    # length of longest increasing subarrays in numbers[:i]
    longest_length = 0
    # number of longest increasing subarrays in numbers[:i]
    longest_subarray_count = 0
    while i < len(numbers):
        # Calculate the length of the increasing subarray starting from index i
        current_length = n_increasing_from_start(numbers, i)
        if current_length == longest_length:
            longest_subarray_count += 1
        elif current_length > longest_length:
            longest_subarray_count = 1
            longest_length = current_length
        i += 1
    return longest_subarray_count


def n_increasing_from_start(numbers: tuple, start: int) -> int:
    """
    Calculates the length of an increasing subsequence starting from the given index.
    Returns 0 if start is not a valid index.

    Args:
        numbers (tuple): A tuple of numbers.
        start (int): The starting index for calculating the length of the increasing subsequence.

    Returns:
        int: The length of the increasing subsequence starting from the given index.

    This function calculates the length of an increasing subsequence starting from the specified index in the given tuple of positive integers.
    It iterates through the tuple from the specified index and counts the consecutive elements that form an increasing subsequence.

    Example:
        If the input tuple is (1, 3, 4, 2, 7, 5, 6, 9, 8) and start is 3, the function returns 1.
        Explanation:
        - The increasing subsequence starting from index 3 is (2), which has a length of 1.
    """
    if start < 0 or start >= len(numbers):
        return 0
    n = 1
    for i in range(start + 1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            n += 1
        else:
            break
    return n


def count_long_subarrays_alt(numbers: tuple) -> int:
    """
    Counts the number of longest subarrays in the given tuple.
    Alternative solution using no subfunction.

    Args:
        numbers (tuple): A tuple of numbers.

    Returns:
        int: The number of longest increasing subarrays.

    """
    if len(numbers) == 0:
        return 0
    i = 0
    # length of longest subarray in numbers[:i+1]
    longest_length = 1
    # number of longest subarrays in numbers[:i+1]
    longest_subarray_count = 1
    # length of longest increasing subarray ending in numbers[i]
    current_length = 1
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_length += 1
        else:
            current_length = 1
        if current_length == longest_length:
            longest_subarray_count += 1
        elif current_length > longest_length:
            longest_subarray_count = 1
            longest_length = current_length
    return longest_subarray_count


tests = (
    (
        (2, 2, 4, 1, 4),
        2,
    ),
    (
        (7, 8, 5, 7, 7, 3, 2, 8),
        3,
    ),
    (
        (7, 7, 9, 1, 2, 11, 9, 6, 2, 8, 9),
        2,
    ),
    (
        (4, 18, 10, 8, 13, 16, 18, 1, 9, 6, 11, 13, 12, 5, 7, 17, 13, 3),
        1,
    ),
    (
        (
            11,
            16,
            10,
            19,
            20,
            18,
            3,
            19,
            2,
            1,
            8,
            17,
            7,
            13,
            1,
            11,
            1,
            18,
            19,
            9,
            7,
            19,
            24,
            2,
            12,
        ),
        4,
    ),
    ((3, 1, 0), 3),
)


class TestSequense(unittest.TestCase):
    pass


def test_generator(actual, expected):
    def test(self):
        self.assertEqual(actual, expected)

    return test


if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_name = f"test_{i:02}"
        numbers, expected_output = test[0], test[1]
        test = test_generator(count_long_subarrays(numbers), expected_output)
        setattr(TestSequense, test_name, test)
    res = unittest.main(verbosity=3, exit=False)
