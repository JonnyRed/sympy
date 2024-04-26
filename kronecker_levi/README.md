# Kronecker Delta Levi-Civita

$
    \delta_{ij} =
        \begin{cases} 1 & \text{if } i = j \\
                      0 & \text{otherwise}
        \end{cases}
$

```python
>>> import kronecker_levi.kronecker_delta as kd
>>> kd.kronecker_delta(1, 1)
1

>>> import kronecker_levi.kronecker_delta as kd
>>> kd.kronecker_delta(1, 2)
0

>>> import kronecker_levi.kronecker_delta as kd
>>> kd.kronecker_delta(2, 1)
0

>>> import kronecker_levi.kronecker_delta as kd
>>> kd.kronecker_delta(0, 0)
1

>>> import kronecker_levi.kronecker_delta as kd
>>> kd.kronecker_delta(-1, 1)
0

```
