# Vector Identities

## Preamble for identities

```python
>>> from itertools import starmap, product
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

$$\epsilon_{ijk} = \epsilon_{jki} = \epsilon_{kij} $$

```python
>>> all(
...    Eijk(i, j, k) == Eijk(j, k, i) == Eijk(k, i, j)
...       for i, j, k in product(range(1, 4), repeat=3)
... )
True

```

$$ \epsilon_{ijk} = -\epsilon_{jik} $$

```python
>>> all(
...    (Eijk(i, j, k) == -Eijk(k, j, i))
...    and (Eijk(i, j, k) == -Eijk(i, k, j))
...    and (Eijk(i, j, k) == -Eijk(j, i, k))
...       for i, j, k in product(range(1, 4), repeat=3)
... )
True

```

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
\epsilon_{ijk} \epsilon_{imn} = \delta_{jm} \delta_{kn} - \delta_{jn} \delta_{km}
$$

```python

>>> def delta_func(j, k, m, n):
...    return (
...        KroneckerDelta(j,m)*KroneckerDelta(k,n) 
...        - KroneckerDelta(j,n)*KroneckerDelta(k,m)
...    )

>>> all(sum(Eijk(i,j,k)*Eijk(i,m,n) for i in range(1,4)) 
...    == delta_func(j, k, m, n) 
...        for j, k, m, n in product(range(1,4), repeat=4))
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

$$
[\mathbf{A} \times \mathbf{B}]_i = \epsilon_{ijk} a_j b_k
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

### Jacobi's Identities

$$
\mathbf A \times (\mathbf B \times \mathbf C)
+ \mathbf C \times (\mathbf A \times \mathbf B)
+ \mathbf B \times (\mathbf C \times \mathbf A)
= 0
$$

```python
>>> def vector_triple_produce(a, b, c):
...    return c.dot(a) * b - (b.dot(a) * c)

>>> a, b, c, d = [symbols(f"{ch}_1:4") for ch in "abcd"]
>>> vec_a, vec_b, vec_c, vec_d = [vector(N, sy) for sy in [a, b, c, d]]
>>> assert (
...    vector_triple_produce(vec_a, vec_b, vec_c)
...    + vector_triple_produce(vec_b, vec_c, vec_a)
...    + vector_triple_produce(vec_c, vec_a, vec_b)
... ) == v_zero

```

### Scalar quadruple product

$$
(\mathbf A \times \mathbf B) \cdot (\mathbf C \times \mathbf D) = (A \cdot \mathbf C)(\mathbf B \cdot \mathbf D) - (\mathbf A \cdot \mathbf D)(\mathbf B \cdot \mathbf C)
$$

```python
>>> (((vec_a.cross(vec_b)).dot(vec_c.cross(vec_d))).expand()
... == 
... ((vec_a.dot(vec_c))*(vec_b.dot(vec_d))-(vec_a.dot(vec_d))
...    *(vec_b.dot(vec_c))).expand())
True

```

### Lagrange's identity

$$
| (\mathbf A \times \mathbf B)|^2 = |\mathbf A|^2 |\mathbf B|^2 - (\mathbf A \cdot \mathbf B)^2
$$

```python
>>> (
...    (vec_a.cross(vec_b).magnitude()**2).expand()
...    == (vec_a.magnitude()**2 * vec_b.magnitude()**2 - (vec_a.dot(vec_b))**2).expand()
... )
True

```

### Vector quadruple product

$$
(\mathbf A \times \mathbf B) \times (\mathbf C \times \mathbf D)
= ((\mathbf A \times \mathbf B) \cdot \mathbf D) \mathbf C
    - ((\mathbf A \times \mathbf B)\cdot \mathbf C) \mathbf D
$$

```python
>>> (((vec_a.cross(vec_b)).cross(vec_c.cross(vec_d))).expand()
... == (
...     ((vec_a.cross(vec_b)).dot(vec_d)*vec_c 
...         - (vec_a.cross(vec_b).dot(vec_c)*vec_d)).expand()
... ))
True

```
