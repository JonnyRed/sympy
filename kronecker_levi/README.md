# Kronecker Delta Levi-Civita

$$
    \delta_{ij} =
        \begin{cases} 1 & \text{if } i = j \\
                      0 & \text{otherwise}
        \end{cases}
$$

```python
>>> import kronecker_levi.kronecker_delta as kd
>>> kd.kronecker_delta(1, 1)
1

>>> kd.kronecker_delta(1, 2)
0

>>> kd.kronecker_delta(2, 1)
0

>>> kd.kronecker_delta(0, 0)
1

>>> kd.kronecker_delta(-1, 1)
0

```

$$\delta_{ij}\delta_{jk} = \delta_{ik}$$

Ensure that the above relationship is valid for range of integers
up until $n$

```python
>>> import test_kronecker_identities as tki
>>> tki.test_kronecker_product(2)
True

>>> tki.test_kronecker_product(3)
True

```
