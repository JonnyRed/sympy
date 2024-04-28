import itertools


def generate_tuples(n:int) -> list[tuple]:
    """
    Generate tuples of length n containing integers from 1 to n.

    Args:
        n (int): The length of each tuple.

    Returns:
        list: A list of tuples, where each inner tuple contains integers
        from 1 to n.

    Examples:
        >>> generate_tuples(2)
        [(1, 1), (1, 2), (2, 1), (2, 2)]

        >>> len(generate_tuples(2))
        4
        
        >>> generate_tuples(3) # doctest: +ELLIPSIS
        [(1, 1, 1), (1, 1, 2), (1, 1, 3), ..., (3, 3, 1), (3, 3, 2), (3, 3, 3)]

        >>> len(generate_tuples(3))
        27
        
    """

    return list(itertools.product(range(1, n + 1), repeat=n))


def filter_tuples_with_m_in_position_n(list_of_tuples, n, m):
    """
    Returns a list of tuples where the nth value equals m.

    Args:
        list_of_tuples (list): A list of tuples.
        n (int): The index of the value to check within each tuple.
        m: The value to compare against.

    Returns:
        list: A filtered list of tuples where the nth value is equal to m.

    Examples:
        >>> filter_tuples_with_m_in_position_n([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 1, 5)
        [(4, 5, 6)]
        >>> filter_tuples_with_m_in_position_n([(10, 20), (30, 40), (50, 60)], 0, 30)
        [(30, 40)]
        >>> filter_tuples_with_m_in_position_n([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 2, 9)
        [(7, 8, 9)]
        >>> filter_tuples_with_m_in_position_n([(1, 2), (3, 4), (5, 6)], 1, 7)
        []
    """
    return [t for t in list_of_tuples if t[n] == m]


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
