def h(i: int) -> int:
    return (11 * i + 4) % 9


if __name__ == "__main__":
    A = [67, 13, 49, 24, 40, 33, 58]
    print([h(i) for i in A])
