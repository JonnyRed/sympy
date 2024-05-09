"""
Kronecker Delta and Tuple Generation

This module provides two functions: `kronecker_delta` and `generate_tuples`.

- `kronecker_delta(i: int, j: int) -> int`:
  The Kronecker delta function returns 1 if `i` equals `j`, and 0 otherwise.

  Parameters:
      i (int): The first input.
      j (int): The second input.

  Returns:
      int: 1 if `i == j`, 0 otherwise.

  Examples:
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

- `generate_tuples(n: int) -> tuple`:
  Generate tuples of length `n` containing integers from 1 to `n`.

  Args:
      n (int): The length of each tuple.

  Returns:
      tuple: A tuple of tuples, where each inner tuple contains integers
      from 1 to `n`.

  Examples:
      >>> generate_tuples(2)
      ((1, 1), (1, 2), (2, 1), (2, 2))

      >>> generate_tuples(3)  # doctest: +ELLIPSIS
      ((1, 1, 1), (1, 1, 2), (1, 1, 3), ..., (3, 3, 1), (3, 3, 2), (3, 3, 3))

"""

import itertools
from sympy import Matrix, KroneckerDelta


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

def kronecker_delta_matrix(i, j, k, ell, m, n):
    """
    Calculates the determinant of a 3x3 matrix filled with Kronecker delta functions.

    Args:
        i (int): The first index for the Kronecker delta functions.
        j (int): The second index for the Kronecker delta functions.
        k (int): The third index for the Kronecker delta functions.
        ell (int): The fourth index for the Kronecker delta functions.
        m (int): The fifth index for the Kronecker delta functions.
        n (int): The sixth index for the Kronecker delta functions.

    Examples:

    Returns:
        int: The determinant of the matrix (always 6 for any non-zero arguments).
    """

    matrix = Matrix(
        [
            [KroneckerDelta(i, ell), KroneckerDelta(i, m), KroneckerDelta(i, n)],
            [KroneckerDelta(j, ell), KroneckerDelta(j, m), KroneckerDelta(j, n)],
            [KroneckerDelta(k, ell), KroneckerDelta(k, m), KroneckerDelta(k, n)],
        ]
    )
    return matrix.det()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
