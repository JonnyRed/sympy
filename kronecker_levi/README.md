# kronecker delta notes

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

This expresses the orthogonality of the Kronecker delta. It equals 1 when $i = k$ and $0$ otherwise.

Ensure that the above relationship is valid for range of integers up until $n$

```python
>>> from sympy import KroneckerDelta
>>> KroneckerDelta(1, 1)
1

>>> KroneckerDelta(1, 2)
0

>>> KroneckerDelta(2, 1)
0

>>> KroneckerDelta(0, 0)
1

>>> KroneckerDelta(-1, 1)
0

```

**Kronecker Delta Summation Property**:

$$
\delta_{ij}\delta_{jk} = \delta_{ik}
$$

`summation property` will ensure the above identity is valid for a range of small indices.

```python
>>> all( 
...   sum( KroneckerDelta(i,j)*KroneckerDelta(j,k) for j in range(1,4) )
...      == KroneckerDelta(i,k) for i in range(1,4) for k in range(1,4) 
... )
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

$$\epsilon_{ijk} = \frac{1}{2} (i-j)(j-k)(k-i)$$

```python
>>> from kronecker_levi.kronecker_delta import generate_tuples
>>> from sympy import LeviCivita
>>> all ( 
...   (LeviCivita(i, j, k)==(i-j)*(j-k)*(k-i)/2)
...    for i, j, k in generate_tuples(3)
... )
True

```

$$\varepsilon_{ijk} = \varepsilon_{jki} = \varepsilon_{kij}$$

```python
>>> from sympy import LeviCivita
>>> all ( 
...   (LeviCivita(i, j, k)==LeviCivita(j, k, i)==LeviCivita(k, i, j))
...    for i, j, k in generate_tuples(3)
... )
True

```

$$\epsilon_{ijk} = -\epsilon_{jik}, \;
    \epsilon_{ijk} = -\epsilon_{ikj},  \;
    \epsilon_{ijk} = -\epsilon_{kji}$$

```python
>>> from sympy import LeviCivita
>>> all ( 
... LeviCivita(i, j, k) == -LeviCivita(j, i, k) == -LeviCivita(k, j, i) 
...    for i, j, k in generate_tuples(3)
... )
True

```

$$\epsilon_{ijk}\epsilon_{imn} =  \delta_{jm} \delta_{kn} - \delta_{jn} \delta_{km}$$

```python
>>> from itertools import product
>>> from sympy import Eijk, KroneckerDelta
>>> all(
...    sum(Eijk(i, j, k) * Eijk(i, m, n) for i in range(1, 4))
...    == KroneckerDelta(j, m) * KroneckerDelta(k, n)
...    - KroneckerDelta(j, n) * KroneckerDelta(k, m)
...    for (_, j, k), (_, m, n) in product(generate_tuples(3), repeat=2)
... )
True

```

"""

$$\epsilon_{ijk} \epsilon_{ijn} = 2 \delta_{kn}$$

```python
>>> from sympy import Eijk, KroneckerDelta, summation
>>> all(
...    (
...     summation(Eijk(i, j, k)*Eijk(i, j, n), (i, 1, 3), (j, 1, 3))
...        == 2*KroneckerDelta(k,n) 
...    ) for k, n in product(range(1,4), repeat=2)
... )
True

```

$$\epsilon_{ijk}\epsilon_{ijk} = 6$$

```python
>>> from sympy import Eijk, summation
>>> summation(Eijk(i, j, k)*Eijk(i, j, k), (i, 1, 3), (j, 1, 3), (k, 1, 3))
6

```

$$
\epsilon_{ijk}\epsilon_{lmn}  =
      \begin{vmatrix}
         \delta_{il} & \delta_{im} & \delta_{in}\\
         \delta_{jl} & \delta_{jm} & \delta_{jn}\\
         \delta_{kl} & \delta_{km} & \delta_{kn}
      \end{vmatrix}
$$

```python

>>> from kronecker_levi.kronecker_delta import generate_tuples, kronecker_delta_matrix
>>> all([
...    (Eijk(*a)*Eijk(*b) == kronecker_delta_matrix(*a, *b))
...    for a in generate_tuples(3)
...    for b in generate_tuples(3)
... ])
True

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

### Identities

$$a_{ij} (x_j + y_j) \equiv a_{ij} x_j + a_{ij}y_j$$

```python
>>> from sympy import Matrix
>>> n = 3
>>> a = symbols(f"a1:{n+1}(1:{n+1})", real=True)
>>> x = symbols(f"x1:{n+1}", real=True)
>>> y = symbols(f"y1:{n+1}", real=True)
>>> A = Matrix(3, 3, a)

>>> (
... list(sum(A[i,j]*(x[j] + y[j]) for j in range(0,n)).expand() 
...         for i in range(0, n)
... )
... 
...   == 
... 
... list(sum(A[i,j]*x[j] for j in range(0, n)) 
...            + sum(A[i,j]*y[j] for j in range(0, n))
...                for i in range(0,n)
... ))
True

```

 $$a_{ij} x_i y_j \equiv a_{ij} y_j x_i$$

```python
>>> (sum(A[i,j]*(x[i]*y[j])  
...    for j in range(0,n) 
...    for i in range(0,n)
... )
...
...   == 
...
... sum(A[i,j]*(y[j]*x[i])  
...    for j in range(0,n) 
...    for i in range(0,n)
... ) 
... )
True

```

$$a_{ij} x_i y_j \equiv a_{ji} y_i x_j$$

```python
>>> (sum(A[i,j]*(x[i]*y[j])  
...    for j in range(0,n) 
...    for i in range(0,n)
... )
...
...   == 
...
... sum(A[j,i]*(y[i]*x[j])  
...    for j in range(0,n) 
...    for i in range(0,n)
... ) 
... )
True

```
