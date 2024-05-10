"""
This module provides functions to solve a Pocket Cube puzzle 
using a bidirectional BFS strategy.

The Pocket Cube configurations are represented by length 24 strings, 
where each character represents the color of a small cube face. 
The faces are laid out in the reading order of a Latin cross unfolding of the cube.

The main function in this module is `solve(config)`, 
which takes an initial configuration as input 
and returns a sequence of moves to solve the configuration using a bidirectional BFS strategy. 
If the configuration is unsolvable, it returns `None`.

Other functions in this module include:
- `scramble(config, n)`: Returns a new configuration by applying `n` random moves to the input configuration.
- `check(config, moves, verbose=False)`: Checks whether applying the given moves to the input configuration results in the solved configuration.
- `test(config)`: Solves the given configuration and prints the path to the solved state.

Note: The code below the "READ, BUT DO NOT MODIFY CODE BELOW HERE" comment should not be modified.
"""

from typing import Optional
from random import randint


def basic_solve(config):
    # Return a sequence of moves to solve config, or None if not possible
    # Fully explore graph using BFS
    parent, frontier = {config: None}, [config]
    while len(frontier) != 0:
        frontier = explore_frontier(frontier, parent, True)
    print(f"Searched {len(parent)} reachable configurations")
    # Check whether solved state visited and reconstruct path
    if SOLVED in parent:
        path = path_to_config(SOLVED, parent)
        return moves_from_path(path)
    return None


def solve(config: str) -> Optional[list[tuple[int, int]]]:
    """
    Solve the given configuration using a bidirectional BFS strategy.

    Args:
        config (str): The initial configuration to solve.

    Returns:
        list or None: A sequence of moves to solve the configuration, or None if it's unsolvable.
    """
    # Explore graph using BFS from the query configuration
    forward = bfs(config)  # BFS from the query configuration
    # Explore graph using BFS from the solved configuration
    backward = bfs(SOLVED)  # BFS from the solved configuration
    curr = forward
    other_parent = dict()
    while True:
        try:
            parent = next(curr)  # Get the next level of configurations from BFS
        except StopIteration:
            break
        common_configs = (
            parent.keys() & other_parent.keys()
        )  # Find configurations explored by both BFSs
        if common_configs:
            break
        curr = (
            backward if curr == forward else forward
        )  # Alternate between forward and backward BFS
        other_parent = parent  # Store parent pointers of the current BFS for comparison
    print(f"Searched {len(parent) + len(other_parent)} reachable configurations")
    if not common_configs:
        return None
    meet_config = common_configs.pop()  # Get the overlapping configuration
    fpath = path_to_config(
        meet_config, parent if curr is forward else other_parent
    )  # Path from query to overlap
    bpath = path_to_config(
        meet_config, other_parent if curr is forward else parent
    )  # Path from overlap to solved
    bpath.pop()  # Remove the overlap configuration from the backward path
    bpath.reverse()  # Reverse the backward path to get correct order
    return moves_from_path(fpath + bpath)  # Combine paths and convert to moves


def bfs(config):
    parent, frontier = {config: None}, [config]
    while len(frontier) != 0:
        yield parent
        frontier = explore_frontier(frontier, parent, True)


# --------------------------------------- #
# READ, BUT DO NOT MODIFY CODE BELOW HERE #
# --------------------------------------- #
# Pocket Cube configurations are represented by length 24 strings
# Each character repesents the color of a small cube face
# Faces are laid out in reading order of a Latin cross unfolding of the cube

SOLVED = "000011223344112233445555"


def config_str(config):
    # Return config string representation as a Latin cross unfolding
    return """
             %s%s
             %s%s
           %s%s%s%s%s%s%s%s
           %s%s%s%s%s%s%s%s
             %s%s
             %s%s
           """ % tuple(
        config
    )


def shift(A, d, ps):
    # Circularly shift values at indices ps in list A by d positions
    values = [A[p] for p in ps]
    k = len(ps)
    for i in range(k):
        A[ps[i]] = values[(i - d) % k]


def rotate(config, face, sgn):
    # Returns new config by rotating input face of input config
    # Rotation is clockwise if sgn == 1, counterclockwise if sgn == -1
    assert face in (0, 1, 2)
    assert sgn in (-1, 1)
    if face is None:
        return config
    new_config = list(config)
    if face == 0:
        shift(new_config, 1 * sgn, [0, 1, 3, 2])
        shift(new_config, 2 * sgn, [11, 10, 9, 8, 7, 6, 5, 4])
    elif face == 1:
        shift(new_config, 1 * sgn, [4, 5, 13, 12])
        shift(new_config, 2 * sgn, [0, 2, 6, 14, 20, 22, 19, 11])
    elif face == 2:
        shift(new_config, 1 * sgn, [6, 7, 15, 14])
        shift(new_config, 2 * sgn, [2, 3, 8, 16, 21, 20, 13, 5])
    return "".join(new_config)


def neighbors(config):
    # Return neighbors of config
    ns = []
    for face in (0, 1, 2):
        for sgn in (-1, 1):
            ns.append(rotate(config, face, sgn))
    return ns


def explore_frontier(frontier, parent, verbose=False):
    # Explore frontier, adding new configs to parent and new_frontier
    # Prints size of frontier if verbose is True
    if verbose:
        print(f"Exploring next frontier containing # configs: {len(frontier)}")
    new_frontier = []
    for f in frontier:
        for config in neighbors(f):
            if config not in parent:
                parent[config] = f
                new_frontier.append(config)
    return new_frontier


def path_to_config(config, parent):
    # Return path of configurations from root of parent tree to config
    path = [config]
    while path[-1] is not None:
        path.append(parent[path[-1]])
    path.pop()
    path.reverse()
    return path


def moves_from_path(path: list[str]) -> Optional[list[tuple[int, int]]]:
    # Given path of configurations, return list of moves relating them
    # Returns None if any adjacent configs on path are not related by a move
    moves = []
    for i in range(1, len(path)):
        move = None
        for face in (0, 1, 2):
            for sgn in (-1, 1):
                if rotate(path[i - 1], face, sgn) == path[i]:
                    move = (face, sgn)
                    moves.append(move)
        if move is None:
            return None
    return moves


def path_from_moves(config, moves):
    # Return the path of configurations from input config applying input moves
    path = [config]
    for move in moves:
        face, sgn = move
        config = rotate(config, face, sgn)
        path.append(config)
    return path


def scramble(config, n):
    # Returns new configuration by appling n random moves to config

    for _ in range(n):
        ns = neighbors(config)
        i = randint(0, 2)
        config = ns[i]
    return config


def check(config, moves, verbose=False):
    # Checks whether applying moves to config results in the solved config
    if verbose:
        print(f"Making {len(moves)} moves from starting configuration:")
    path = path_from_moves(config, moves)
    if verbose:
        print(config_str(config))
    for i in range(1, len(path)):
        face, sgn = moves[i - 1]
        direction = "clockwise"
        if sgn == -1:
            direction = "counterclockwise"
        if verbose:
            print(f"Rotating face {face} {direction}:")
            print(config_str(path[i]))
    return path[-1] == SOLVED


def test(config):
    print("Solving configuration:")
    print(config_str(config))
    moves = solve(config)
    if moves is None:
        print("Path to solved state not found... :(")
        return
    print("Path to solved state found!")
    if check(config, moves):
        print("Move sequence terminated at solved state!")
    else:
        print("Move sequence did not terminate at solved state... :(")


if __name__ == "__main__":
    scrambled_config = scramble(SOLVED, 100)
    test(scrambled_config)
