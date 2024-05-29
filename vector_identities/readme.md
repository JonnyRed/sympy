# Vector Identities

## Preamble for identities

```python
>>> from itertools import starmap
>>> from operator import mul
>>> from sympy import symbols, KroneckerDelta, Eijk
>>> import sympy.vector as sv
>>> import sv_utils as svu

>>> v_zero = sv.Vector.zero
>>> print(type(v_zero))
<class 'sympy.vector.vector.VectorZero'>

>>> print(v_zero)
0

>>> N =sv.CoordSys3D("N", vector_names=("e_1", "e_2", "e_3"))
>>> print(list(v for v in N))
[N.e_1, N.e_2, N.e_3]

>>> print(list(enumerate(N))) 
[(0, N.e_1), (1, N.e_2), (2, N.e_3)]

>>> print(N.base_vectors())
(N.e_1, N.e_2, N.e_3)

>>> a = symbols("a_1:4", real=True)
>>> print(a)
(a_1, a_2, a_3)

>>> b = symbols("b_1:4", real=True)
>>> print(b)
(b_1, b_2, b_3)

>>> c = symbols("c_1:4", real=True)
>>> print(c)
(c_1, c_2, c_3)

>>> d = symbols("d_1:4", real=True)
>>> print(d)
(d_1, d_2, d_3)

>>> def vector(N, components):
...     return sum(
...         starmap(mul, zip(components, N.base_vectors())), 
...         start=sv.Vector.zero
...     )

>>> vector_a = vector(N, a)
>>> print(vector_a)
a_1*N.e_1 + a_2*N.e_2 + a_3*N.e_3

>>> vector_b = vector(N, b)
>>> print(vector_b)
b_1*N.e_1 + b_2*N.e_2 + b_3*N.e_3

>>> vector_c = vector(N, c)
>>> print(vector_c)
c_1*N.e_1 + c_2*N.e_2 + c_3*N.e_3

>>> vector_d = vector(N, d)
>>> print(vector_d)
d_1*N.e_1 + d_2*N.e_2 + d_3*N.e_3


```

## Identities

$$ [\mathbf A]_i \; \text {is  component of A} $$

$$
\mathbf{e_i}\cdot\mathbf{e_j} = \delta_{ij}
$$

```python
>>> all(
...    u.dot(v) == KroneckerDelta(i+1, j+1) 
...        for i, u in enumerate(N) for j, v in enumerate(N)
... ) 
True

```

$$
\delta_{ij}\mathbf{b_j} =   \mathbf{b_i}
$$

```python

>>> all(
...     sum(KroneckerDelta(i,j)*b[j-1] for j in range(1,4)) 
...     == b[i-1] for i in range(1,4)
... )
True

```

$$
\mathbf A = a_i \mathbf e_i
$$

```python
>>> print(
...    sum( 
...       (component*N.base_vectors()[ix] for ix, component in enumerate(a)),
...       start=sv.Vector.zero
...    )
... )
a_1*N.e_1 + a_2*N.e_2 + a_3*N.e_3

```

$$
a_i b_j (\mathbf e_i \cdot \mathbf e_j) = a_i b_i
$$

```python
>>> sum(a[i-1]*b[j-1]*(N.base_vectors()[i-1].dot(N.base_vectors()[j-1]))
...    for i in range(1,4)
...    for j in range(1,4)
... ) == sum(a[i-1]*b[i-1] for i in range(1,4))
True

```

$$
\mathbf{e_i} \times \mathbf{e_j} = \epsilon_{ijk} \mathbf{e_i}
$$
$$
\mathbf{e_j} \times \mathbf{e_k} = \mathbf{e_i} \epsilon_{ijk}
$$

```python
>>> all(  
...    N.base_vectors()[i-1].cross(N.base_vectors()[j-1]) 
...        == 
...    sum(
...        (Eijk(i,j,k)*N.base_vectors()[k-1] for k in range(1,4)), 
...            start=sv.Vector.zero
...    )
...    for i in range(1,4) 
...    for j in range(1,4)
... )
True

```

$$
\mathbf{A} \times \mathbf{B} = \epsilon_{ijk} a_i b_j \mathbf{e_k}
$$

$$
\mathbf{A} \times \mathbf{B} = \mathbf{e_i} \epsilon_{ijk} a_j b_k
$$

```python

>>> def vector_product(N, a, b, i, j, k):
...     return Eijk(i, j, k)*a[i-1]*b[j-1]*N.base_vectors()[k-1]

>>> ( 
... vector(N, a).cross(vector(N,b)) 
...    ==
... sum((
...    (sum(
...        (sum((vector_product(N, a, b, i, j, k) for k in range(1,4)), start=v_zero)
...            for j in range(1,4)), start=v_zero)) 
...    for i in range(1,4)), start=v_zero
... ))  
True

```

### Scalar Triple Product

$$\mathbf A \cdot ( \mathbf B \times \mathbf C ) = \mathbf C \cdot ( \mathbf A \times \mathbf B ) = \mathbf B \cdot ( \mathbf C \times \mathbf A )
$$

$$
a_i \; [ \mathbf B \times \mathbf C ]_i
    = a_i \epsilon_{ijk} b_j c_k = c_k \epsilon_{kij} a_i b_j = c_k [\mathbf A \times \mathbf B]_k
$$

```python
>>> (vector_a.dot(vector_b.cross(vector_c)).expand()
...    == vector_c.dot(vector_a.cross(vector_b)).expand())
True

>>> (vector_c.dot(vector_a.cross(vector_b)).expand()
...    == vector_b.dot(vector_c.cross(vector_a)).expand())
True

```

### Vector Triple Product

$$\mathbf A \times ( \mathbf B \times \mathbf C ) =
(\mathbf A \cdot \mathbf C) \mathbf B - (\mathbf A \cdot B) \mathbf C
$$

```python
>>> ((vector_a.cross(vector_b.cross(vector_c))).expand()
...    ==
... (vector_a.dot(vector_c)*vector_b - vector_a.dot(vector_b)*vector_c).expand())
True

```

### Scalar quadruple product

$$
( \mathbf A \times  \mathbf B) \cdot ( \mathbf C \times  \mathbf D)
  = (\mathbf A \cdot  \mathbf C) (\mathbf B \cdot  \mathbf D)
  - (\mathbf A \cdot  \mathbf D) (\mathbf B \cdot  \mathbf C)

$$

```python
>>> ((vector_a.cross(vector_b)).dot(vector_c.cross(vector_d)).expand()
...    == (vector_a.dot(vector_c)*vector_b.dot(vector_d) 
...        - vector_a.dot(vector_d)*vector_b.dot(vector_c)).expand())
True

```

### Jacobi Identity

$$
\mathbf A \times ( \mathbf B \times \mathbf C )
+ \mathbf B \times ( \mathbf C \times \mathbf A )
+ \mathbf C \times ( \mathbf A \times \mathbf B )
= 0
$$

```python
>>> ((vector_a.cross(vector_b.cross(vector_c))
...    + vector_b.cross(vector_c.cross(vector_a))
...    + vector_c.cross(vector_a.cross(vector_b))).expand()
...    == v_zero)
True

```

### Lagrange’s identity

$$
|\mathbf A \times \mathbf B |^2
 =  |\mathbf A|^2 |\mathbf B|^2
 - (\mathbf A \cdot \mathbf B  )^2
$$

```python
>>> (((vector_a.cross(vector_b)).magnitude()**2).expand()
...    == (vector_a.magnitude()**2*vector_b.magnitude()**2
...        - vector_a.dot(vector_b)**2).expand()) # doctest: +NORMALIZE_WHITESPACE
True

```
