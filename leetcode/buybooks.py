from typing import List

# There is a O(n) solution where one looks at the most expensive 2 * K elements.
# Can be implemented with a heap.


# The following is a O(n^2*k) solution to practice dynamic programming.
def getMinimumCost(books: List[int], paircost: int, K: int) -> int:
    """
    Calculate the minimum cost to buy all books with special purchasing rules.

    There are n books ordered sequentially as costs from 1,2...n, where the ith book
    has a cost of books[i]. A customer wants to purchase all the books, and there
    is a scheme to minimize the cost as follows:

    1. Let i = start of the array. The customer can buy the leftmost book at any moment
        for books[i], this book is then removed from the array.
    2. Let j = end of the array, the customer can buy the rightmost book at any moment
        for books[j], this book is then removed from the array.
    3. The customer can buy both the book at the start and the book at the end together
        for a special amount called "paircost", then both the book at the start and the
        book at the end of the array are removed. Option 3 can be used up to K times.

    Args:
        books (List[int]): Array of costs for each book
        paircost (int): Cost to buy both leftmost and rightmost books together
        K (int): Maximum number of times option 3 can be used

    Returns:
        int: The minimum possible cost to buy all the books
    """
    minCost = [
        [[0 for k in range(K + 1)] for j in range(len(books) + 1)]
        for i in range(len(books) + 1)
    ]
    for slen in range(1, len(books) + 1):
        for i in range(len(books) - slen + 1):
            j = i + slen
            for k in range(K + 1):
                options = set()
                if k > 0 and i + 2 >= j:
                    options.add(minCost[i + 1][j - 1][k - 1] + paircost)
                options.add(minCost[i + 1][j][k] + books[i])
                options.add(minCost[i][j - 1][k] + books[j - 1])
                minCost[i][j][k] = min(options)
    return minCost[0][len(books)][K]


print(getMinimumCost([4, 5, 6], 3, 3))
