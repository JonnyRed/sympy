import kronecker_levi.kronecker_delta as kd

def kronecker_product(n: int):
    """
    Generate pairs of Kronecker delta products and their summation.

    The function yields tuples containing the Kronecker delta of 
    `i` and `k`, and the summation of the product of Kronecker deltas 
    over `j`. The fuction yiels a tuple consisting of 
    delta_ij*delta_jk (using einstein summation convention) and
    delta_ik. For each of these:
    
    delta_ij*delta_jk = delta_ik 

    Parameters:
    n (int): The upper limit for the range of indices.

    Yields:
    tuple: A tuple containing the Kronecker delta of `i` and `k`, 
    and the summation of delta_ij*delta_jk.

   Examples:
    >>> list(kronecker_product(2))
    [(1, 1), (0, 0), (0, 0), (1, 1)]
    """
    for i in range(1, n+1):
        for k in range(1, n+1):
            delta_ik = kd.kronecker_delta(i, k)
            sigma = sum(
                kd.kronecker_delta(i, j) * kd.kronecker_delta(j, k) 
                    for j in range(1, n+1))
            yield delta_ik, sigma

def test_kronecker_product(n: int):
    """
    Test the kronecker_product function to ensure it works correctly.

    Parameters:
    n (int): The upper limit for the range of indices to test.

    Examples:
    >>> test_kronecker_product(2)
    True
    
    >>> test_kronecker_product(3)
    True
    """
    # generator = kronecker_product(n)
    return all(delta_ik == sigma for delta_ik, sigma in kronecker_product(n))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)