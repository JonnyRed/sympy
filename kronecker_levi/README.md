# Math cheat sheet notes

## Kronecker Delta Levi-Civita

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

## Levi-Civita

```python
>>> from sympy import symbols, LeviCivita
>>> i, j, k = symbols("i, j, k", integer=True)

>>> LeviCivita(1, 2, 3)
1

>>> LeviCivita(1, 3, 2)
-1

>>> LeviCivita(1, 2, 2)
0

>>> LeviCivita(i, j, k)
LeviCivita(i, j, k)

>>> LeviCivita(i, j, i)
0

```

## Einstein summation convention

The Einstein summation convention(ESC) is a convention used in mathematics
and physics for summation over repeated indices in expressions
involving vectors, matrices, and tensors. It was introduced by Albert
Einstein and simplifies expressions by implicitly summing over repeated
indices.

According to this convention, when an index variable appears twice in
a single term and is not otherwise defined, it implies summation of that
term over all the values of the index. For example, the expression
$a_{i}b_{i}$ is equivalent to the sum of
$a_{1}b_{1} + a_{2}b_{2} + ... + a_{n}b_{n}$

Here are the key points of the Einstein summation convention:

1. Summation over Repeated Indices:
    * If an index appears twice (once as a subscript and once as a
    superscript) in a term, it is implicitly summed over all
    possible values.
    *The sum is performed for each repeated index independently.
1. Dummy Indices:
    * Indices that are summed over are called "dummy indices."
    * The choice of the index name is arbitrary and doesn't affect
    the result.
1. Examples:
    * $a_i$ and $b_i$ are vectors, then the dot product can be written
    as $a_i b_i$ without explicitly writing the summation sign. Here,
    $i$ is a dummy index that is implicitly summed over.
    * For a matrix $A_{ij}$ and a vector $v_j$ , the matrix-vector
    product can be written as $(Av)_i = A_{ij} v_j$, again without
    explicitly writing the summation sign.
1. Repetition of Indices:
    * An index can be repeated more than once in an expression, and
    each repetition implies a separate summation.
1. Avoidance of Summation Sign:
    * The summation sign $(\sum)$ is often omitted to simplify notation.

   The Einstein summation convention is widely used in general relativity, electromagnetism, and other areas of theoretical physics where vector

   and tensor calculus play a central role. It provides a concise and
   convenient notation for expressing mathematical expressions
   involving summations over repeated indices.

Two interesting examples of  the Einstein summation convention
$$ \delta_{i i} = 3 \text{ and } \varepsilon_{ijk}\varepsilon_{ijk} = 6$$
