def subarray_sum_iterative(numbers: list[int]):
    """
    Compute all subarray sums of a list of integers
    and find the maximum subarray sum.

    This function computes the sums of all possible subarrays of the input list
    in O(n^2) time complexity. It returns a nested dictionary where the keys
    are the starting indices of the subarrays, and the values are dictionaries
    mapping the ending indices to the corresponding subarray sums. Additionally,
    it returns the maximum subarray sum found.

    Args:
        numbers (list[int]): A list of integers for which subarray sums are to be computed.

    Returns:
        tuple: A tuple containing:
            - dict[int, dict[int, int]]: A nested dictionary where the outer dictionary's keys are
              starting indices of subarrays, and the inner dictionaries map ending indices
              to the sums of the subarrays.
            - int: The maximum subarray sum.

        For example, if `numbers` is [1, 2, 3], the returned values would be:
        (
            {
                0: {0: 1, 1: 3, 2: 6},
                1: {1: 2, 2: 5},
                2: {2: 3}
            },
            6
        )
    """
    n = len(numbers)
    subsums = {i: dict() for i in range(n)}
    for i in range(n):
        subsums[i][i - 1] = 0
    max_sum = float("-inf")
    for i in range(n):
        for d in range(n):
            j = i + d
            if j > n - 1:
                break
            subsums[i][j] = subsums[i][j - 1] + numbers[j]
            if subsums[i][j] > max_sum:
                max_sum = subsums[i][j]

    return subsums, max_sum


def max_subarray_sum(numbers: list[int]):
    """
    Find the largest sum of any non-empty subarray in the given array.
    A subarray is defined as a contiguous sequence of elements within the array.

    Parameters:
    arr (list of int): The input array of integers.

    Returns:
    int: The largest sum of any non-empty subarray.

    Example:
    >>> max_subarray_sum([-9, 1, -5, 4, 3, -6, 7, 8, -2])
    16
    """
    _, max_subsum = subarray_sum_iterative(numbers)
    return max_subsum


if __name__ == "__main__":
    print(max_subarray_sum([-9, 1, -5, 4, 3, -6, 7, 8, -2]))
    print(subarray_sum_iterative([]))
