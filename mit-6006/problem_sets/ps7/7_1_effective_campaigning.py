"""
Problem 7-1. Effective Campaigning
Representative Zena Torr is facing off against Senator Kong Grossman in a heated presidential primary: 
a sequence of n head-to-head state contests, one per day for n days. Each state contest i ∈{1,...,n} 
has a known positive integer delegate count di, and a projected delegate count zi < di that Rep. Torr 
would win if she took no further action. There are D = sum(di) total delegates and Rep. Torr needs 
at least floor(D/2) +1 delegates to win. Unfortunately, Rep. Torr is projected to lose the race, since 
sum(zi) < floor(D/2) +1, so she needs to take action. Rep. Torr has a limited but effective election 
team which can campaign in at most one state per day. If the team campaigns on day i, they will win 
all di delegates in state i, but they will not be able to campaign at all for two days after day i, 
as it will take time to relocate. Describe an O(n)-time algorithm to determine whether it is possible 
for Rep. Torr to win the primary contest by campaigning effectively.
"""

from math import floor


def can_torr_win(n: int, d: list[int], z: list[int]) -> bool:
    """
    Determines if Rep. Torr can win the primary contest by campaigning effectively.

    Parameters:
    n (int): Number of state contests
    d (list of int): List containing delegate counts for each state contest
    z (list of int): List containing projected delegate counts for each state contest if no action is taken

    Returns:
    bool: True if Rep. Torr can win, False otherwise
    """
    n_votes = max_votes(n, d, z)
    D = sum(d)
    return n_votes >= floor(D / 2) + 1


def max_votes(n, d, z):
    maxv = [0] * n
    maxv[n - 1] = d[n - 1]
    for i in range(n - 2, -1, -1):
        campaign_i = d[i] + sum(z[i + 1 : i + 3]) + maxv[i + 3] if i + 3 < n else 0
        no_campaign_i = z[i] + maxv[i + 1]
        maxv[i] = max(campaign_i, no_campaign_i)
    return maxv[0]


if __name__ == "__main__":
    # example
    n = 3
    d = [3, 4, 5]
    z = [2, 2, 2]
    print(can_torr_win(n, d, z))  # True
