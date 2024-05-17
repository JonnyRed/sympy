"""
This module provides various utility functions for working with
Sympy and Sympy's vector module.

It includes functions for creating vectors, calculating the angle
between vectors, and defining lines and planes in 3D space.
It also includes functions for printing aligned LaTeX equations.

The module uses Sympy's vector module for vector operations and
Sympy's solvers module for solving # equations. It also uses
IPython's display module for displaying LaTeX equations.

The module includes the following functions:

  * vector(frame: sv.CoordSys3D, rx, ry, rz=0) -> sv.Vector:
    Creates a vector in a specified reference frame.
  * vector_cos(frame: sv.CoordSys3D, magnitude, theta, phi, psi=sp.pi / 2) -> sv.Vector:
    Creates a vector with components defined by cosine values in a
    specified reference frame.
  * vector_to_list(frame: sv.CoordSys3D, v: sv.Vector) -> List[float]:
     Converts a vector in a reference frame to a list of components.
  * create_3d_components(*args) -> List[Tuple[sympy.Symbol, sympy.Symbol, sympy.Symbol]]:
    Creates 3D components for given symbols.
  * create_vectors(frame: sv.CoordSys3D, *args) -> List[sv.Vector]:
        Creates a list of vectors in a specified reference frame.
  * angle_between_two_vectors(frame: sv.CoordSys3D, v1: sv.Vector, v2: sv.Vector) -> sympy.Symbol:
    Calculates the smallest angle between two vectors.
  * cosine_of_angle_between_vectors(v: sv.CoordSys3D, u: sv.CoordSys3D, theta: sympy.Symbol)
    -> sympy.Symbol:
        Calculates the cosine of the angle between two vectors.
  * square_of_sine_of_angle_between_vectors(v: sv.CoordSys3D, u: sv.CoordSys3D, theta: sympy.Symbol)
    -> sympy.Expr:
       Calculates the square of the sine of the angle between two vectors.
  * vector_line(start: sv.Vector, finish: sv.Vector) -> sv.Vector:
    Calculates the vector line through two vectors.
  * vector_line_eqn(frame: sv.CoordSys3D, start: sv.Vector, finish: sv.Vector, lamda: sympy.Symbol)
    -> sv.Vector:
        Calculates the vector equation for a line segment in a specified reference frame.
  * vector_plane(frame: sv.CoordSys3D, r1: sv.Vector, r2: sv.Vector, r3: sv.Vector)
    -> Tuple[sympy.Eq, Tuple[sympy.Symbol, sympy.Symbol, sympy.Symbol]]:
        Defines a plane through three non-collinear points.
  * laplacian(f: sympy.Expr) -> sympy.Expr: Calculates the Laplacian of an expression.
  * print_aligned_latex_equations(*args): Prints LaTeX equations in an aligned format.

The module also includes various constants and symbols used throughout
the code.
"""

import IPython.display as ipd
import sympy as sp
import sympy.vector as sv

sp.init_printing()



HALF = sp.S.Half
ZERO = sp.S.Zero
ONE = sp.S.One
PI = sp.pi
E = sp.exp
POSITIVEINFINITY = sp.S.Infinity
NEGATIVEINFINITY = sp.S.NegativeInfinity


def vector(frame: sv.CoordSys3D, rx, ry, rz=0) -> sv.Vector:
    """
    Create a vector in a specified reference frame.

    Args:
        frame (sv.CoordSys3D): The reference frame in which the vector is defined.
        rx (float): The coefficient of the x-axis vector component.
        ry (float): The coefficient of the y-axis vector component.
        rz (float, optional): The coefficient of the z-axis vector component (default: 0).

    Returns:
        sv.Vector: The vector composed of the specified components in the given reference frame.

    Examples:
        >>> N = sv.CoordSys3D('N')
        >>> vector(N, 1, 0, 0)
        N.i

        >>> vector(N, 0, 1, 0)
        N.j

        >>> vector(N, 0, 0, 1)
        N.k

        >>> vector(N, 1, 2)
        N.i + 2*N.j

        >>> vector(N, 1, 2, 3)
        N.i + 2*N.j + 3*N.k

        >>> vector(N, 5.0, 5.1, 7.7)
        5.0*N.i + 5.1*N.j + 7.7*N.k

        >>> vector(N, 1, 2, 3)
        N.i + 2*N.j + 3*N.k
    """
    return rx * frame.i + ry * frame.j + rz * frame.k

# pylint: disable=C0301
def vector_cos(frame: sv.CoordSys3D, magnitude, theta, phi, psi=sp.pi / 2) -> sv.Vector:
    """
    Create a vector with components defined by cosine values in a specified reference frame.

    Args:
        F (sv.CoordSys3D): The reference frame in which the vector is defined.
        magnitude (float): The magnitude of the vector.
        theta (float): The angle (in radians) between the vector and the x-axis.
        phi (float): The angle (in radians) between the vector and the y-axis.
        psi (float, optional): The angle (in radians) between the
            vector and the z-axis (default: pi/2).

    Returns:
        sv.Vector: The vector with components determined by the cosine
        values in the given reference frame.

    Examples:
        >>> N = sv.CoordSys3D('N')
        >>> vector_cos(N, 1, PI/2, sp.Float(0))
        N.j

        >>> vector_cos(N, 1, 0, PI/2)
        N.i

        >>> vector_cos(N, sp.sqrt(2), PI/4, PI/4).simplify()
        N.i + N.j

        >>> vector_cos(N, 1, PI/2, 0)
        N.j

        >>> vector_cos(N, 41, PI/2 + PI/4, 2*PI/3, PI/3)
        (-41*sqrt(2)/2)*N.i + (-41/2)*N.j + 41/2*N.k

        >>> n = sp.sqrt(93)
        >>> vector_cos(N, n, 5/n, 2/n, 8/n)
        (sqrt(93)*cos(5*sqrt(93)/93))*N.i + (sqrt(93)*cos(2*sqrt(93)/93))*N.j + (sqrt(93)*cos(8*sqrt(93)/93))*N.k
    """

    return magnitude * (
        sp.cos(theta) * frame.i + sp.cos(phi) * frame.j + sp.cos(psi) * frame.k
    )


def vector_to_list(frame: sv.CoordSys3D, v: sv.Vector):
    """
    Convert a vector in a reference frame to a list of components.

    Args:
        frame (sv.CoordSys3D): Reference frame for conversion.
        v (sv.Vector): Vector to convert to list in frame.

    Returns:
        List[float]: List of components of v in frame.

    Examples:
        >>> N = sv.CoordSys3D('N')
        >>> v = 3 * N.i + 4 * N.j + 5 * N.k
        >>> vector_to_list(N, v)
        [3, 4, 5]

        >>> N = sv.CoordSys3D('N')
        >>> v = 3 * N.i + 4 * N.j
        >>> vector_to_list(N, v)
        [3, 4, 0]

    """
    return [v.dot(frame.i), v.dot(frame.j), v.dot(frame.k)]


def create_3d_components(*args):
    """
    Create 3D components for given symbols.

    Args:
        *args (str): Variable names for which 3D components are to be created.

    Returns:
        list: A list containing 3D component symbols for each input variable.

    Examples:
        >>> create_3d_components('a')
        [(a_x, a_y, a_z)]

        >>> create_3d_components('a', 'b')
        [(a_x, a_y, a_z), (b_x, b_y, b_z)]

    """
    return [sp.symbols(f"{ch}" "_x:z", real=True) for ch in args]


def create_vectors(frame: sv.CoordSys3D, *args) -> list:
    """
    Create a list of vectors in a specified reference frame.

    This function takes a reference frame and multiple sets of components as arguments
    and returns a list of vectors created from these components in the given reference frame.

    Args:
        frame (sv.CoordSys3D): The reference frame in which the vectors are defined.
        *args: Variable-length argument list containing sets of vector components.

    Returns:
        list: A list of vectors composed of the specified components in the given reference frame.

    Examples:
        >>> N = sv.CoordSys3D('N')
        >>> create_vectors(N, "a")
        [a_x*N.i + a_y*N.j + a_z*N.k]

        >>> create_vectors(N, "a", "b")
        [a_x*N.i + a_y*N.j + a_z*N.k, b_x*N.i + b_y*N.j + b_z*N.k]

    """
    return [vector(frame, *c) for c in create_3d_components(*args)]


def angle_between_two_vectors(v1: sv.Vector, v2: sv.Vector):
    """Smallest angle between two vectors

    Args:The reference frame in which the vectors are defined.
        v1 (sv.Vector): first vector
        v2 (sv.Vector): second vector

    Returns:
        Any: arcos of smallest angle between two vectors

        Examples:
        >>> N = sv.CoordSys3D('N')
        >>> a = 3*N.i + 4*N.j
        >>> b = 2*N.i - N.j
        >>> round(angle_between_two_vectors(a, b).evalf(), 4)
        0.1789

        >>> v1 = N.i
        >>> v2 = N.j
        >>> angle_between_two_vectors(v1, v2)
        0

        >>> v3 = N.i + N.j + N.k
        >>> angle_between_two_vectors(v1, v3)
        sqrt(3)/3

        >>> a = N.i + N.j
        >>> b = 2*N.i + 2*N.j
        >>> angle_between_two_vectors(a, b)
        1

        >>> a = 2*N.i - 4*N.j - 1*N.k
        >>> b = 5 * N.j +2*N.k
        >>> angle_between_two_vectors(a, b)
        -22*sqrt(609)/609

        >>> import math
        >>> N = sv.CoordSys3D('N')
        >>> vec_A, vec_B = 5*N.i - 2*N.j + 4*N.k, 3*N.i + 1*N.j + 7*N.k
        >>> cos_angle = angle_between_two_vectors(vec_A, vec_B)
        >>> round(math.degrees(sp.acos(cos_angle)), 1) # doctest: +NORMALIZE_WHITESPACE
        37.3

    """
    return sv.dot(v1, v2) / v1.magnitude() / v2.magnitude()


def cosine_of_angle_between_vectors(
    v: vector, u: vector, theta: sp.Symbol
) -> sp.Symbol:
    """Using the cosine rule determine the angle between vectors.

    Args:
        v (vector): first vector
        u (vector): second vector
        theta (sp.Symbol): symbol for angle between two vectors

    Returns:
        sp.Symbol: cosine of angle between two vectors

    Examples:
        >>> N = sv.CoordSys3D('N')
        >>> alpha = sp.symbols("alpha", real=True)
        >>> a, b = N.i, N.j
        >>> sp.acos(cosine_of_angle_between_vectors(a, b, alpha))
        pi/2

        >>> N = sv.CoordSys3D('N')
        >>> alpha = sp.symbols("alpha", real=True)
        >>> a, b = N.i, N.i + N.j
        >>> sp.acos(cosine_of_angle_between_vectors(a, b, alpha))
        pi/4

        >>> N = sv.CoordSys3D('N')
        >>> alpha = sp.symbols("alpha", real=True)
        >>> a = vector_cos(N, 4, PI/12, PI*5/12)
        >>> b = vector_cos(N, 8, PI/4, PI/4)
        >>> sp.acos(cosine_of_angle_between_vectors(a, b, alpha))
        pi/6

    """

    cosine_rule = sp.Eq(
        ((v - u).magnitude()) ** 2,
        u.magnitude() ** 2
        + v.magnitude() ** 2
        - 2 * u.magnitude() * v.magnitude() * sp.cos(theta),
    )

    return sp.solve(cosine_rule, sp.cos(theta))[0].simplify()


def square_of_sine_of_angle_between_vectors(
    v: vector, u: vector, theta: sp.Symbol
) -> sp.Expr:
    """Find the square of the sine of angle between 2 vectors

    Args:
        v (vector): first vector
        u (vector): second vector
        theta (sp.Symbol): symbol for angle between two vectors

    Returns:
        sp.Expr: square of the sine of angle between 2 vectors

    Examples:
        >>> N = sv.CoordSys3D('N')
        >>> alpha = sp.symbols("alpha", real=True)
        >>> a, b = N.i, N.j
        >>> sq = square_of_sine_of_angle_between_vectors(a, b, alpha)
        >>> sq
        1

        N = sv.CoordSys3D('N')
        alpha = sp.symbols("alpha", real=True)
        a = vector_cos(N, 4, PI/12, PI*5/12)
        b = vector_cos(N, 8, PI/4, PI/4)
        square_of_sine_of_angle_between_vectors(a, b, theta)
        1/4

    """

    return 1 - cosine_of_angle_between_vectors(v, u, theta) ** 2


def vector_line(start: sv.Vector, finish: sv.Vector) -> sv.Vector:
    """Determine line through two vectors

    Args:
        start (sv.Vector): Start vector
        finish (sv.Vector): End vector

    Returns:
        sv.Vector: vector displacement
    """
    return finish - start


def vector_line_eqn(
    start: sv.Vector, finish: sv.Vector, lamda: sp.Symbol
) -> sv.Vector:
    """
    Calculate a vector equation for a line segment in a specified reference frame.

    Args:
        frame (sv.CoordSys3D): The reference frame in which the vector equation is defined.
        start (sv.Vector): The starting vector point of the line segment.
        finish (sv.Vector): The ending vector point of the line segment.
        lamda (sp.Symbol): A symbolic scalar value determining the position along the line segment.

    Returns:
        sv.Vector: The vector equation representing the line segment in the given reference frame.

    Examples:
        >>> A = sv.CoordSys3D('A')
        >>> start = sv.Vector.zero
        >>> finish = 3 * A.i + 4 * A.j + 5 * A.k
        >>> lamda = sp.symbols('lambda')
        >>> vector_line_eqn(start, finish, lamda)
        3*lambda*A.i + 4*lambda*A.j + 5*lambda*A.k

        >>> start = 2 * A.i - A.j
        >>> finish = 4 * A.j + 3 * A.k
        >>> vector_line_eqn(start, finish, lamda)
        (2 - 2*lambda)*A.i + (5*lambda - 1)*A.j + 3*lambda*A.k

    """

    return start + vector_line(start, finish) * lamda


def vector_plane(
    frame: sv.CoordSys3D, r1: sv.Vector, r2: sv.Vector, r3: sv.Vector
) -> sp.Expr:
    """Define a plane through 3 non-collinear points

    Args:
        frame (sv.CoordSys3D): Coordinate system of plane
        r1 (sv.Vector): vector position on plane
        r2 (sv.Vector): vector position on plane
        r3 (sv.Vector): vector position on plane

    Returns: sp.Expr

    Examples:
    >>> N = sv.CoordSys3D("N")
    >>> vector_plane(N, vector(N, -1, -1, -1), vector(N, 1, 1, 1), vector(N, 1, -1, 0))
    (Eq(x, -y + 2*z), (x, y, z))

    """

    vec_line1 = vector_line(r1, r2)
    vec_line2 = vector_line(r2, r3)
    normal = vec_line1.cross(vec_line2)

    coefficients = sp.symbols("x, y, z", real=True)
    vec_r = vector(frame, *coefficients)
    return sp.Eq((vec_r - r1).dot(normal), 0).simplify(), coefficients  # type: ignore


def laplacian(f: sp.Expr) -> sp.Expr:
    """Determine the Laplacian of an expression

    Args:
        f (sp.Expr): Expression fo determine the Laplacian

    Returns:
        sp.Expr: the Laplacian

    Examples:
    >>> N = sv.CoordSys3D("N")
    >>> f = N.x**2 + 3 * N.y**2 + 2 * N.x * N.y + 3 * N.x + 5
    >>> laplacian(f)
    8
    """

    nabla = sv.Del()
    return nabla.dot(nabla.gradient(f)).doit()


def print_aligned_latex_equations(*args):
    """
    print LaTeX equations.

    This function takes in any number of LaTeX equations as arguments
    and prints them in an aligned format using the 'split' environment.
    """
    result = r"\\".join(
        [
            r"\begin{equation}",
            r"\begin{split}",
            *args,
            r"\nonumber",
            r"\end{split}",
            r"\end{equation}",
        ]
    )

    ipd.display(ipd.Math(rf"{result}"))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False)
