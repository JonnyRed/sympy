"""
This module provides a set of tools for working with vectors and reference
frames in three-dimensional space.
The module is implemented using the Sympy physics vector module, which
provides a set of tools for working with vectors and vector operations.

The functions in the module include:

    reference_frame(frame, x=r"\imath", y=r"\jmath", z=r"\mathbf k") 
        Creates a reference frame in Sympy, which is a coordinate system \
            used to define vectors.

    vector(frame, rx, ry, rz=0)
        Creates a vector in a specified reference frame, with components \
            defined along the x, y, and z axes.

    vector_cos(frame, magnitude, theta, phi, psi=sp.pi / 2)
        Creates a vector with components defined by cosine values in a \
            specified reference frame.

    vector_to_list(frame, v)
        Converts a vector in a reference frame to a list of components.

    vector_line(start, finish)
        Calculates the vector difference between two points, representing
        a line segment.

    vector_line_eqn(frame, start, finish, lamda)
        Calculates a vector equation for a line segment in a specified
        reference frame.

    angle_between_vectors(a, b)
        Calculates the angle in radians between two vectors.

    create_3d_components(*args)
        Creates 3D components for given symbols.

    create_vectors(frame, *args)
        Creates a list of vectors in a specified reference frame.

    print_aligned_latex_equations(*args)
        Prints aligned LaTeX equations using IPython display.

The module also includes a set of unit tests using the doctest module, \
    which verifies that the functions are working as expected.

Overall, this module provides a set of tools for working with vectors and \
    reference frames in three-dimensional space, which can be useful in a \
    variety of applications, including physics, engineering, and <
    computer graphics.
By using the Sympy physics vector module, the functions in this module \
    can be used to perform symbolic vector operations, which can be useful \
    for analytical calculations and derivations.
"""

import IPython.display as ipd
import sympy as sp
import sympy.physics.vector as spv


HALF = sp.S.Half
ONE = sp.S.One
PI = sp.pi
E = sp.exp
POSITIVEINFINITY = sp.S.Infinity
NEGATIVEINFINITY = sp.S.NegativeInfinity


def reference_frame(
    frame: str, x=r"\imath", y=r"\jmath", z=r"\mathbf k"
) -> spv.ReferenceFrame:
    """
    Create a reference frame in SymPy.

    Args:
        frame (str): Name of the reference frame.
        x (str, optional): LaTeX representation of the x unit vector.
        y (str, optional): LaTeX representation of the y unit vector.
        z (str, optional): LaTeX representation of the z unit vector.

    Returns:
        spv.ReferenceFrame: The created reference frame.

    Examples:
        >>> F = reference_frame("F")
        >>> F
        F
        >>> F.x
        F.x
        >>> F.y
        F.y
        >>> F.z
        F.z
    """
    return spv.ReferenceFrame(
        frame,
        latexs=(
            rf"\; {{}}^\mathcal {frame} \hat {x}",
            rf"\;{{}}^\mathcal {frame} \hat {y}",
            rf"\: {{}}^\mathcal {frame} \hat {{z}}",
        ),
    )


def vector(frame: spv.ReferenceFrame, rx, ry, rz=0) -> spv.Vector:
    """
    Create a vector in a specified reference frame.

    Args:
        frame (spv.ReferenceFrame): The reference frame in which the
        vector is defined.
        rx (float): The coefficient of the x-axis vector component.
        ry (float): The coefficient of the y-axis vector component.
        rz (float, optional): The coefficient of the z-axis vector
        component (default: 0).

    Returns:
        spv.Vector: The vector composed of the specified components
        in the given reference frame.

    Examples:
        >>> N = spv.ReferenceFrame('N')
        >>> vector(N, 1, 0, 0)
        N.x

        >>> vector(N, 0, 1, 0)
        N.y

        >>> vector(N, 0, 0, 1)
        N.z

        >>> vector(N, 1, 2)
        N.x + 2*N.y

        >>> vector(N, 1, 2, 3)
        N.x + 2*N.y + 3*N.z

        >>> vector(N, 5.0, 5.1, 7.7)
        5.0*N.x + 5.1*N.y + 7.7*N.z

        >>> vector(N, 1, 2, 3)
        N.x + 2*N.y + 3*N.z
    """
    return rx * frame.x + ry * frame.y + rz * frame.z


def vector_cos(
    frame: spv.ReferenceFrame, magnitude, theta, phi, psi=sp.pi / 2
) -> spv.Vector:
    """
    Create a vector with components defined by cosine values in a
    specified reference frame.

    Args:
        frame (spv.ReferenceFrame): The reference frame in which the
        vector is defined.

        magnitude (float): The magnitude of the vector.

        theta (float): The angle (in radians) between the vector and
        the x-axis.

        phi (float): The angle (in radians) between the vector and the
        y-axis.

        psi (float, optional): The angle (in radians) between the
            vector and the z-axis (default: pi/2).

    Returns:
        spv.Vector: The vector with components determined by the cosine
        values in the given reference frame.

    Examples:
        >>> N = spv.ReferenceFrame('N')

        >>> vector_cos(N, 1, PI/2, 0)
        N.y

        >>> vector_cos(N, 1, 0, PI/2)
        N.x

        >>> vector_cos(N, sp.sqrt(2), PI/4, PI/4)
        N.x + N.y

        >>> vector_cos(N, 1, PI/2, 0)
        N.y

        >>> vector_cos(N, 41, PI/2 + PI/4, 2*PI/3, PI/3)
        - 41*sqrt(2)/2*N.x - 41/2*N.y + 41/2*N.z

        >>> n = sp.sqrt(93)
        >>> vector_cos(N, n, 5/n, 2/n, 8/n)
        sqrt(93)*cos(5*sqrt(93)/93)*N.x + sqrt(93)*cos(2*sqrt(93)/93)*N.y\
 + sqrt(93)*cos(8*sqrt(93)/93)*N.z

    """

    return magnitude * (
        sp.cos(theta) * frame.x + sp.cos(phi) * frame.y + sp.cos(psi) * frame.z
    )


def vector_to_list(frame: spv.ReferenceFrame, v: spv.Vector) -> list:
    """change a vector in a reference frame to a list of components

    Args:
        frame (spv.ReferenceFrame): Reference frame for conversion
        v (spv.Vector): Vector to convert to list in frame

    Returns:
        list: List of components of v in frame

    Examples:
        >>> N = spv.ReferenceFrame('N')
        >>> v = 3 * N.x + 4 * N.y + 5 * N.z
        >>> vector_to_list(N, v)
        [3, 4, 5]

        >>> v = 3 * N.x + 4 * N.y
        >>> vector_to_list(N, v)
        [3, 4, 0]

    """
    return [v.dot(frame.x), v.dot(frame.y), v.dot(frame.z)]


def vector_line(start: spv.Vector, finish: spv.Vector) -> spv.Vector:
    """Returns the vector that represents the line connecting the two given vectors

    Args:
        start (spv.Vector): start vector position
        finish (spv.Vector): end vector position

    Returns:
        spv.Vector: line connecting the two given vectors
    """
    return finish - start


def vector_line_eqn(
    start: spv.Vector,
    finish: spv.Vector,
    lamda: sp.Symbol,
) -> spv.Vector:
    """
    Calculate a vector equation for a line segment in a specified
    reference frame.

    Args:
        frame (spv.ReferenceFrame): The reference frame in which the vector
        equation is defined.

        start (spv.Vector): The starting vector point of the line segment.
        finish (spv.Vector): The ending vector point of the line segment.

        lamda (sp.Symbol): A symbolic scalar value determining the position
        along the line segment.

    Returns:
        spv.Vector: The vector equation representing the line segment in
        the given reference frame.

    Examples:
        >>> A = spv.ReferenceFrame('A')
        >>> start = A.x*0 + A.y*0 + A.z*0  # Zero vector
        >>> finish = 3 * A.x + 4 * A.y + 5 * A.z
        >>> lamda = sp.symbols('lambda')
        >>> vector_line_eqn(start, finish, lamda)
        3*lambda*A.x + 4*lambda*A.y + 5*lambda*A.z

        >>> start = 2 * A.x - A.y
        >>> finish = 4 *A.y + 3 * A.z
        >>> vector_line_eqn(start, finish, lamda)
        (2 - 2*lambda)*A.x + (5*lambda - 1)*A.y + 3*lambda*A.z
    """
    return start + vector_line(start, finish) * lamda


def angle_between_vectors(a: spv.Vector, b: spv.Vector):
    """
    Calculate the angle in radians between two vectors.

    Args:
        a (spv.Vector): The first vector.
        b (spv.Vector): The second vector.

    Returns:
        float: The angle in radians between the two vectors.

    Examples:
        >>> A = spv.ReferenceFrame('A')
        >>> a = 3 * A.x + 4 * A.y
        >>> b = 2 * A.x - A.y
        >>> angle_between_vectors(a, b)
        acos(2*sqrt(5)/25)

        >>> v1 = A.x
        >>> v2 = A.y
        >>> v1.angle_between(v2)
        pi/2

        >>> v3 = A.x + A.y + A.z
        >>> v1.angle_between(v3)
        acos(sqrt(3)/3)

    """

    return a.angle_between(b)


def create_3d_components(*args):
    """
    Create 3D components for given symbols.

    Args:
        *args (str): Variable names for which 3D components are to be created.

    Returns:
        list: A list containing 3D component symbols for each input variable.

    Examples:
        >>> create_3d_components('a')
        [(a_{x}, a_{y}, a_{z})]

        >>> create_3d_components('a', 'b')
        [(a_{x}, a_{y}, a_{z}), (b_{x}, b_{y}, b_{z})]

    """
    return [sp.symbols(f"{ch}_{{x:z}}", real=True) for ch in args]


def create_vectors(frame: spv.ReferenceFrame, *args) -> list:
    """
    Create a list of vectors in a specified reference frame.

    This function takes a reference frame and multiple sets of components
    as arguments and returns a list of vectors created from these
    components in the given reference frame.

    Args:
        frame (spv.ReferenceFrame): The reference frame in which the
        vectors are defined.

        *args: Variable-length argument list containing sets of vector
        components.

    Returns:
        list: A list of vectors composed of the specified components in
        the given reference frame.

    Examples:
        >>> N = spv.ReferenceFrame('N')
        >>> create_vectors(N, "a")
        [a_{x}*N.x + a_{y}*N.y + a_{z}*N.z]

        >>> create_vectors(N, "a", "b")
        [a_{x}*N.x + a_{y}*N.y + a_{z}*N.z, b_{x}*N.x + b_{y}*N.y + b_{z}*N.z]

    """
    return [vector(frame, *c) for c in create_3d_components(*args)]


def print_aligned_latex_equations(*args):
    """
    Prints aligned LaTeX equations using IPython display.

    Args:
        *args: Variable number of LaTeX equation strings to be aligned.

    Returns:
        None

    """
    result = r"\\".join(
        [
            r"\begin{equation} ",
            r"\begin{split}",
            *args,
            r"\nonumber"+ r"\end{split}",
            r"\end{equation}",
        ]
    )

    ipd.display(ipd.Math(rf"{result}"))  # type: ignore


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
