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

>>> def vector(N, components):
...     return sum(
...         starmap(mul, zip(components, N.base_vectors())), 
...         start=sv.Vector.zero
...     )

>>> print(vector(N, a))
a_1*N.e_1 + a_2*N.e_2 + a_3*N.e_3

>>> print(vector(N, b))
b_1*N.e_1 + b_2*N.e_2 + b_3*N.e_3

>>> print(vector(N, c))
c_1*N.e_1 + c_2*N.e_2 + c_3*N.e_3


```

## Identities

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
