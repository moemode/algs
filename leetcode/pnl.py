from heapq import heappush, heappop
from typing import List


def func(pnl: List[int]) -> int:
    acc, neg = 0, []
    for i, num in enumerate(pnl):
        if acc > num:  # acc >= num, if acc can be 0 (non-negative)
            # greedy
            acc -= num
            heappush(neg, (-num, i))
        elif neg and -neg[0][0] > num:
            # worth replacing
            acc -= 2 * heappop(neg)[0]
            acc -= num
            heappush(neg, (-num, i))
        else:
            # positive case
            acc += num

    res = pnl[:]
    for _, i in neg:
        res[i] = -res[i]
    print(res)

    return len(neg)


"""
Maximize the number of negative entries in pnl,
such that all cumulative sums are still positive.
For a pnl of length l, there are l cumulative sums.
The i-th cumulative sum is the sum of elements up to and including i.
"""


def max_negative_entries(pnl: List[int]) -> int:
    # current cumulative sum
    acc = 0
    # contains all negative numbers we have added so far
    # both numbers which are negative in the original pnl and positive numbers we were able to negate
    neg = []
    for i, num in enumerate(pnl):
        d = -num if num > 0 else num  # <= 0
        if acc + d > 0:  # use >= if acc can be 0
            # greedy
            acc += d
            heappush(neg, (d, i))
        elif neg and neg[0][0] < d:
            # worth replacing
            acc -= 2 * heappop(neg)[0]
            acc += d
            heappush(neg, (d, i))
        else:
            # add positive number or negated negative number because necessary
            acc -= d
    res = [abs(n) for n in pnl]
    for _, i in neg:
        res[i] = -res[i]
    return sum(1 for val in res if val < 0)


# Table-based tests
test_cases = [
    {
        "name": "Mixed positives with one negative",
        "pnl": [5, -3, 1, 1, 1, 1],
        "expected": 4,
    },
    {"name": "Simple case", "pnl": [1, -2], "expected": 0},
    {"name": "All positives", "pnl": [5, 4, 1, 1, 1, 1, 1], "expected": 5},
    {
        "name": "More negatives than positives",
        "pnl": [7, -3, -2, -1, -1, -1],
        "expected": 4,
    },
    {"name": "Mixed case", "pnl": [5, -3, 1, -2], "expected": 2},
]

# Run all tests
print("Running tests for max_negative_entries:")
print("-" * 90)
print(f"{'Test Case':<30} {'Input':<20} {'Result':<10} {'Expected':<10} {'Pass?':<5}")
print("-" * 90)


for test in test_cases:
    result = func(test["pnl"])
    passed = result == test["expected"]
    status = "✓" if passed else "✗"
    print(
        f"{test['name']:<30} {str(test['pnl']):<20} {result:<10} {test['expected']:<10} {status}"
    )

print("-" * 90)
