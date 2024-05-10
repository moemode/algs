from math import factorial


def calculate_cube_configs():
    """
    Calculates an upper bound on the number of possible configurations for a 2x2x2 cube.

    Returns:
        int: The total number of possible configurations.
    """
    n_configs = factorial(7) * (3**7)
    return n_configs


print(calculate_cube_configs())
