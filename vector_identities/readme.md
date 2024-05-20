# Vector Identities

```python
>>> from sympy import symbols, KroneckerDelta, Eijk
>>> import sympy.vector as sv
>>> import sv_utils as svu

>>> N =sv.CoordSys3D("N", vector_names=("e_1", "e_2", "e_3"))
>>> print(list(v for v in N))
[N.e_1, N.e_2, N.e_3]

>>> print(N.base_vectors())
(N.e_1, N.e_2, N.e_3)

>>> a = symbols("a_1:4", real=True)
>>> print(a)
(a_1, a_2, a_3)

>>> b = symbols("b_1:4", real=True)
>>> print(b)
(b_1, b_2, b_3)

```

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
\mathbf{e_i} \times \mathbf{e_j} = \epsilon_{ijk} \mathbf{e_k}
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
