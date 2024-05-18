# Vector Identities

```python
>>> from sympy import KroneckerDelta
>>> import sympy.vector as sv
>>> import sv_utils as svu
>>> N =sv.CoordSys3D("N", vector_names=("e_1", "e_2", "e_3"))

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
