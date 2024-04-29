import itertools


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


def generate_tuples(n):
    """
    Generate tuples of length n containing integers from 1 to n.

    Args:
        n (int): The length of each tuple.

    Returns:
        tuple: A tuple of tuples, where each inner tuple contains integers
        from 1 to n.

    Examples:
        >>> generate_tuples(2)
        ((1, 1), (1, 2), (2, 1), (2, 2))

        >>> generate_tuples(3) #doctest: +ELLIPSIS
        ((1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), ..., (3, 3, 1), (3, 3, 2), (3, 3, 3))

    """
    return tuple(itertools.product(range(1, n + 1), repeat=n))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
