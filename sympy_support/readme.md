# Sympy Vector Tools

This module provides a set of tools for working with vectors and reference frames in three-dimensional space. It leverages the Sympy physics vector module, which offers a comprehensive set of functionalities for vector operations.

## Features

The functions in this module include:

- `reference_frame(frame, x=r"\imath", y="\\jmath", z="\\mathbf k")`: Creates a reference frame in Sympy, serving as a coordinate system to define vectors.
- `vector(frame, rx, ry, rz=0)`: Creates a vector in a specified reference frame with components defined along the x, y, and z axes.
- `vector_cos(frame, magnitude, theta, phi, psi=sp.pi / 2)`: Creates a vector with components defined by cosine values in a specified reference frame.
- `vector_to_list(frame, v)`: Converts a vector in a reference frame to a list of components.
- `vector_line(start, finish)`: Calculates the vector difference between
two points, representing a line segment.
- `vector_line_eqn(start, finish, lamda)`: Calculates a vector equation
for a line segment in a specified reference frame.
- `angle_between_vectors(a, b)`: Calculates the angle in radians between
two vectors.
- `create_3d_components(*args)`: Creates 3D components for given symbols.
- `create_vectors(frame, *args)`: Creates a list of vectors in a specified
reference frame.
- `print_aligned_latex_equations(*args)`: Prints aligned LaTeX equations
using IPython display.

## Usage

### Example Usage

```python
import sympy as sp
import sympy.physics.vector as spv

# Create a reference frame
N = spv.ReferenceFrame('N')

# Create a vector in the reference frame
v = vector(N, 3, 4, 5)

# Convert the vector to a list of components
components = vector_to_list(N, v)

# Calculate the angle between two vectors
a = vector(N, 3, 4, 0)
b = vector(N, 2, 0, 1)
angle = angle_between_vectors(a, b)

# Print the angle
print(angle)

# Create vectors and print aligned LaTeX equations
vectors = create_vectors(N, "a", "b")
print_aligned_latex_equations(*vectors)
```

## critical_points_2d.py

This Python module provides functions for finding and classif(y)ing critical
points of functions in two dimensions. The module uses the sympy library
to perform symbolic calculations.

### Functions

- `find_critical_points(fx, fy, x, y)`
Finds the critical points of a function $f(x, y)$ by solving the system of
equations $fx = 0$ and $fy = 0$, where $fx$ and $fy$ are the partial derivatives
of $f$ with respect to $x$ and $y$, respectively.

Parameters
fx: A sympy expression representing the partial derivative of f with respect to x.
fy: A sympy expression representing the partial derivative of f with respect to y.
x: A sympy symbol representing the variable x.
y: A sympy symbol representing the variable y.
Returns
A list of tuples, where each tuple contains the coordinates of a critical point.

classif(y)_critical_point(f, x, y, point)
Classifies a critical point of a function f(x, y) as a local minimum,
local maximum, or saddle point.

Parameters
f: A sympy expression representing the function f(x, y).
x: A sympy symbol representing the variable x.
y: A sympy symbol representing the variable y.
point: A tuple containing the coordinates of the critical point.
Returns
A string indicating the type of critical point: 'local minimum', 'local maximum', or 'saddle point'.
