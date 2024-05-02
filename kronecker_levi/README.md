# Kronecker Delta Levi-Civita

The abbreviation ESC means Einstein Summation Convention.
When not used and there is ambiguity then:

* $\text{ESC}$  means use Einstein Summation Convention
* $\sim \text{ESC}$  means do not use Einstein Summation Convention

1. **Kronecker definition**

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

**Kronecker Delta Summation Property**:

$$
\delta_{ij}\delta_{jk} = \delta_{ik}$$

This expresses the orthogonality of the Kronecker delta. It equals 1 when $i = k$ and $0$ otherwise.

Ensure that the above relationship is valid for range of integers up until $n$

`test_kronecker_product` will ensure the above identity is valid for a range of small indices.

```python
>>> import test_kronecker_identities as tki
>>> tki.test_kronecker_product(2)
True

>>> tki.test_kronecker_product(3)
True

```

**Kronecker Contraction Property**

Sum of a product of a Kronecker delta and a scalar:

$$ \delta_{ij} a_j = a_i $$

This formula states that the sum of a product of a scalar and a Kronecker delta is equal to the scalar if i = j, and 0 otherwise.

using Einstein summation convention this means

$$
\sum_{j \in \mathbb Z} \delta_{ij} a_j = a_i
$$

This is clearly true

**Kronecker Delta Symmetric Property**:

$$\delta_{ij} = \delta_{ji}$$

This property states that the Kronecker delta is symmetric under index transposition.
