# Sympy Vector Tools

This module provides a set of tools for working with vectors and reference frames in three-dimensional space. It leverages the Sympy physics vector module, which offers a comprehensive set of functionalities for vector operations.

## Features

The functions in this module include:

- `reference_frame(frame, x=r"\imath", y="\\jmath", z="\\mathbf k")`: Creates a reference frame in Sympy, serving as a coordinate system to define vectors.
- `vector(frame, rx, ry, rz=0)`: Creates a vector in a specified reference frame with components defined along the x, y, and z axes.
- `vector_cos(frame, magnitude, theta, phi, psi=sp.pi / 2)`: Creates a vector with components defined by cosine values in a specified reference frame.
- `vector_to_list(frame, v)`: Converts a vector in a reference frame to a list of components.
- `vector_line(start, finish)`: Calculates the vector difference between two points, representing a line segment.
- `vector_line_eqn(start, finish, lamda)`: Calculates a vector equation for a line segment in a specified reference frame.
- `angle_between_vectors(a, b)`: Calculates the angle in radians between two vectors.
- `create_3d_components(*args)`: Creates 3D components for given symbols.
- `create_vectors(frame, *args)`: Creates a list of vectors in a specified reference frame.
- `print_aligned_latex_equations(*args)`: Prints aligned LaTeX equations using IPython display.

## Usage

### Installation

Before using the module, ensure you have the required dependencies installed. You can install them via conda and environment.yml

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

### Testing

The module also includes a set of unit tests using the doctest module to verify that the functions work as expected. To run the tests, execute the module as a script:

```bash
python sympy_vector_tools.py
```

## Conclusion

This module provides a powerful set of tools for working with vectors and reference frames in three-dimensional space. It can be utilized in various applications such as physics, engineering, and computer graphics. By leveraging the Sympy physics vector module, it enables symbolic vector operations, making it suitable for analytical calculations and derivations.
