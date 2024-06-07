# Vectors tensors and fields

I found this set of lectures that provide an excellent introduction to
[vectors tensors and fields][]. The lecture are provided by John Peacock
The document is structured as a set of 11 lectures, each with a set of
notes, examples, and exercises. The notation and terminology used in
the document are standard in the field of vector and tensor calculus.
The document is well-written and clear, with many illustrative examples
and diagrams.

Overall, the document is a valuable resource for anyone interested in
learning vector and tensor calculus, as well as its applications in
physics and mathematics.

The lectures may be found locally [here][vectors-tensors]

[vectors tensors and fields]: https://www.roe.ac.uk/japwww/teaching/vtf.html
[vectors-tensors]: ../docs/Vectors-Tensors-Fields.pdf

## More on Suffix notation

```python
>>> from itertools import product
>>> from sympy import symbols, KroneckerDelta, Eijk
>>> from sympy.vector import CoordSys3D
>>> import sympy.vector as sv
>>> v_zero = sv.Vector.zero

>>> N = CoordSys3D("N", vector_names=("e_1", "e_2", "e_3"))
>>> print(N.base_vectors())
(N.e_1, N.e_2, N.e_3)

```

$$e_i \cdot e_j = \delta_{ij}$$

```python
>>> all(
... (N.base_vectors()[i-1].dot(N.base_vectors()[j-1]) == KroneckerDelta(i,j)) 
...     for i,j in product(range(1, 4), repeat=2))
True

```

$$e_i \times e_j = \epsilon_{ijk} e_k$$

```python
>>> all (
...   N.base_vectors()[i-1].cross(N.base_vectors()[j-1]) 
...     == sum( (Eijk(i, j, k)* N.base_vectors()[k-1] 
...            for k in range(1,4)), start=v_zero )
...  for i,j in product(range(1, 4), repeat=2))
True

```
