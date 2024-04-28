def kronecker_delta(i: int, j: int) -> int:
    """
    The Kronecker delta function returns 1 if i equals j, and 0 otherwise

    Parameters:
    i (int): The first input
    j (int): The second input

    Returns:
    int: 1 if i == j, 0 otherwise

    >>> kronecker_delta(1, 1)
    1

    >>> kronecker_delta(1, 2)
    0

    >>> kronecker_delta(2, 1)
    0

    >>> kronecker_delta(0, 0)
    1

    >>> kronecker_delta(-1, 1)
    0
    """
    return 1 if i == j else 0


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
