from typing import Union

Numeric = Union[int, float]


def max_sum_pair(A: list[Numeric], target: Numeric) -> tuple[int, int]:
    if len(A) < 2:
        raise ValueError(f"A must have at least 2 elements.")
    l = 0
    curr_max = -1
    sum_indices = (-1, -1)
    for r in range(len(A) - 1, -1, -1):
        while l < r and A[l] + A[r] <= target:
            s = A[l] + A[r]
            if s > curr_max:
                curr_max = s
                sum_indices = (l, r)
            l += 1
        if l == r:
            return sum_indices


def max_sum_pair2(A: list[Numeric], target: Numeric) -> tuple[int, int]:
    if len(A) < 2:
        raise ValueError("A must have at least 2 elements.")
    l, r = 0, len(A) - 1
    best_sum = float("-inf")
    best_indices = (-1, -1)
    while l < r:
        current_sum = A[l] + A[r]
        if current_sum == target:
            return (l, r)
        if current_sum < target:
            if current_sum > best_sum:
                best_sum = current_sum
                best_indices = (l, r)
            l += 1
        else:
            r -= 1
    return best_indices


if __name__ == "__main__":
    A = [3, 4, 9, 17, 18, 23]
    print(max_sum_pair2(A, 36))
    print(max_sum_pair2(A, 100))
