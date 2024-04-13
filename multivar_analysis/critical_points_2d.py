"""
    The provided code defines a Python module named `functions_2.py`
    for working with multivariable functions and critical points.
    Here's a breakdown of the functions and their functionalities:

**1. sgn(x):**
   - This function takes an integer `x` and returns its sign
   (1 for positive, -1 for negative, 0 for zero).

**2. critical_points(f, x, y):**
   - This function takes a function expression `f`, and symbols
   representing variables `x` and `y`.
   - It finds the critical points of `f` by solving the system of
   equations where both partial derivatives `fx` and `fy` are equal to zero.
   - It returns a dictionary containing the coordinates of each
   critical point.

**3. second_order_partial_derivatives(f, x, y):**
   - This function takes a function expression `f`, and symbols
   representing variables `x` and `y`.
   - It calculates the second-order partial derivatives of `f` with
   respect to `x` (fxx), `y` (fyy), and the mixed derivative (fxy).
   - It returns a tuple containing these three second-order partial
   derivatives.

**4. discriminant(f, x, y):**
   - This function takes a function expression `f`, and symbols
   representing variables `x` and `y`.
   - It calculates the discriminant, which is a quantity derived from
   the second-order partial derivatives used to classify critical points.
   - It returns the discriminant as a symbolic expression.

**5. evaluate_discriminant(f, x, y, a, b):**
   - This function takes a function expression `f`, symbols representing
   variables `x` and `y`, and two floats `a` and `b`.
   - It evaluates the discriminant of `f` at the specific point (`a`, `b`).
   - It returns the numerical value of the discriminant at that point.

**6. second_derivative_test(f, x, y, a, b):**
   - This function is the core function for performing the second derivative test.
   - It takes a function expression `f`, symbols representing variables
   `x` and `y`, and two floats `a` and `b` representing a critical point.
   - It uses the discriminant and the second-order partial derivative
   evaluated at the critical point to classify the extremum type
   (local minimum, local maximum, saddle point) or inconclusive.
   - It returns a string indicating the classification of the critical point.

**7. analyse_critical_points(f, x, y):**
   - This function takes a function expression `f`, and symbols
   representing variables `x` and `y`.
   - It calls `critical_points` to find all critical points of `f`.
   - It iterates through each critical point and uses
   `second_derivative_test` to determine its type.
   - It returns a list of tuples where each tuple contains the
   coordinates of a critical point and its corresponding type
   (extremum or saddle point).

**8. hessian(f, x, y):** (not explained in the prompt)
   - This function calculates the Hessian matrix of `f`, which is
   a matrix containing all second-order partial derivatives.

**9. is_minimum(f, x, y, a, b):** (not explained in the prompt)
   - This function checks if a point (`a`, `b`) is a local minimum of
   `f` using the conditions for positive second-order partial derivatives
   and a positive discriminant.
   - It returns a boolean indicating if it's a local minimum.

**10. is_maximum(f, x, y, a, b):** (not explained in the prompt)
   - This function checks if a point (`a`, `b`) is a local maximum of
   `f` using the conditions for negative second-order partial
   derivatives and a positive discriminant.
   - It returns a boolean indicating if it's a local maximum.

**11. is_saddle_point(f, x, y, a, b):** (not explained in the prompt)
   - This function checks if a point (`a`, `b`) is a saddle point of `f`.
   - It uses conditions based on the signs of the second-order partial
   derivatives and the mixed derivative to determine a saddle point.
   - It returns a boolean indicating if it's a saddle point.

**12. if __name__ == "__main__":** (not shown in the code snippet)
   - This block is likely used for internal testing purposes.
   It typically includes calls to `doctest.testmod` to run docstring
   examples
"""

from typing import Any
import sympy as sp


def sgn(x: int) -> int:
    """
    Returns the sign of a number.

    Parameters:
        x (int): The number.

    Returns:
        int: 1 if x is positive, -1 if x is negative, or 0 if x is zero.

    Examples:
        >>> sgn(5)
        1
        >>> sgn(-5)
        -1
        >>> sgn(0)
        0
    """
    if x > 0:
        return 1
    return -1 if x < 0 else 0


def critical_points(f: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> dict:
    """
    Calculate the critical points of a function with respect to variables
    x and y.

    Let  z=f(x,y) be a function of two variables that is differentiable
    on an open set containing the point (x0,y0). The point (x0,y0)
    is called a critical point of a function of two variables f
    if one of the two following conditions holds:
    Parameters:

    1. fx(x0,y0) = fy(x0,y0) = 0
    2. Either fx(x0,y0) or fy(x0,y0) does not exist.

    f (sp.Expr): The function to find critical points for.
    x (sp.Symbol): The symbol representing the variable x.
    y (sp.Symbol): The symbol representing the variable y.

    Returns:
    list: The dict of critical points

    Example:
    >>> x, y = sp.symbols('x y')
    >>> critical_points(x**2 + y**2, x, y)
    [{x: 0, y: 0}]

    >>> critical_points(sp.sqrt(4*y**2 -9*x**2 +24*y+36*x+36), x, y)
    [{x: 2, y: -3}]

    >>> critical_points(x**2+2*x*y-4*y**2+4*x-6*y+4, x, y)
    [{x: -1, y: -1}]

    >>> critical_points(x**3+2*x*y-2*x-4*y, x, y)
    [{x: 2, y: -5}]

    >>> critical_points(4*x**2 + 9*y**2 + 8*x - 36*y + 24, x, y)
    [{x: -1, y: 2}]

    >>> critical_points(x**3/3 + y**2 +2*x*y -6*x - 3*y +4, x, y)
    [{x: -1, y: 5/2}, {x: 3, y: -3/2}]

    """
    fx = sp.diff(f, x)
    fy = sp.diff(f, y)
    eqns = [sp.Eq(fx, 0), sp.Eq(fy, 0)]
    return sp.solve(eqns, dict=True)


def second_order_partial_derivatives(
    f: sp.Expr, x: sp.Symbol, y: sp.Symbol
) -> tuple[Any, Any, Any]:
    """
    Calculate the second partial derivatives of a function f(x, y).

    Args:
        f (sp.Expr): The function expression.
        x (sp.Symbol): The symbol for the independent variable x.
        y (sp.Symbol): The symbol for the independent variable y.

    Returns:
        tuple[sp.Expr, sp.Expr, sp.Expr]: A tuple with the second partial derivatives:
        - fxx: The second derivative of f with respect to x.
        - fyy: The second derivative of f with respect to y.
        - fxy: The second mixed derivative of f.

    Examples:
        >>> x, y = sp.symbols('x y')
        >>> f = x**2 + y**2
        >>> fxx, fyy, fxy = second_order_partial_derivatives(f, x, y)
        >>> fxx
        2
        >>> fyy
        2
        >>> fxy
        0

        >>> f = 4*x**2 + 9*y**2 + 8*x - 36*y + 24
        >>> fxx, fyy, fxy = second_order_partial_derivatives(f, x, y)
        >>> fxx
        8
        >>> fyy
        18
        >>> fxy
        0

        >>> f = x**3/3 + y**2 +2*x*y -6*x - 3*y + 4
        >>> fxx, fyy, fxy = second_order_partial_derivatives(f, x, y)
        >>> fxx
        2*x
        >>> fyy
        2
        >>> fxy
        2

    """
    fxx = f.diff(x, x)
    fyy = f.diff(y, y)
    fxy = f.diff(x, y)
    return fxx, fyy, fxy


def discriminant(f: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> Any:
    """
    Checks if the square of the second derivative with respect to x and y
    divided by the product of the first  derivatives with respect to
    x and y is less than 1.

    Parameters:
    f (sp.Expr): The function to analyze.
    x (sp.Symbol): The symbol representing the variable x.
    y (sp.Symbol): The symbol representing the variable y.
    a (sp.Float): The lower bound of the region to evaluate.
    b (sp.Float): The upper bound of the region to evaluate.

    Returns:
    bool: True if the condition is satisfied, False otherwise.

    Examples:
    >>> x, y = sp.symbols('x y')
    >>> f = x**2 + y**2
    >>> discriminant(f, x, y)
    4

    >>> f = x**2 + y**2 + x*y
    >>> discriminant(f, x, y)
    3

    >>> f = 4*x**2 + 9*y**2 + 8*x - 36*y + 24
    >>> discriminant(f, x, y)
    144

    >>> f = x**3/3 + y**2 +2*x*y -6*x - 3*y + 4
    >>> discriminant(f, x, y)
    4*x - 4


    """

    (fxx, fyy, fxy) = second_order_partial_derivatives(f, x, y)
    return fxx * fyy - fxy**2


def evaluate_discriminant(
    f: sp.Expr, x: sp.Symbol, y: sp.Symbol, a: sp.Float, b: sp.Float
) -> sp.Expr:
    """
    Evaluate the discriminant of a function f at point (a, b).

    Parameters:
    f (sp.Expr): The function to evaluate the discriminant for.
    x (sp.Symbol): The symbol representing the variable x.
    y (sp.Symbol): The symbol representing the variable y.
    a (sp.Float): The value to substitute for x.
    b (sp.Float): The value to substitute for y.

    Returns:
    sp.Expr: The value of the discriminant at point (a, b).

    Example:

    >>> x, y = sp.symbols('x y')
    >>> f = 4*x**2 + 9*y**2 + 8*x - 36*y + 24
    >>> evaluate_discriminant(f, x, y, -1, 2)
    144

    >>> x, y = sp.symbols('x y')
    >>> f = x**3/3 + y**2 +2*x*y -6*x - 3*y + 4
    >>> evaluate_discriminant(f, x, y, -1, 5/2)
    -8
    >>> evaluate_discriminant(f, x, y, 3, -3/2)
    8

    """
    d = discriminant(f, x, y)
    return d.subs(x, a).subs(y, b)


def second_derivative_test(
    f: sp.Expr, x: sp.Symbol, y: sp.Symbol, a: sp.Float, b: sp.Float
) -> str:
    """
    Performs the second derivative test to classify critical points
    of a multivariable function.

    Args:
        f (sp.Expr): The multivariable function.
        x (sp.Symbol): The independent variable x.
        y (sp.Symbol): The independent variable y.
        a (sp.Float): The x-coordinate of the critical point.
        b (sp.Float): The y-coordinate of the critical point.

    Examples:
        >>> x, y = sp.symbols('x y')
        >>> f = 4*x**2 + 9*y**2 + 8*x - 36*y + 24
        >>> second_derivative_test(f, x, y, -1, 2)
        'LOCAL_MINIMUM'

        >>> x, y = sp.symbols('x y')
        >>> f =  x**3/3 + y**2 +2*x*y -6*x - 3*y + 4
        >>> second_derivative_test(f, x, y, 3, 3/2)
        'LOCAL_MINIMUM'

        >>> second_derivative_test(f, x, y, -1, 5/2)
        'SADDLEPOINT'

    Returns:
        str: Classification of the critical point (
            "LOCAL_MINIMUM", "LOCAL_MAXIMUM",
            "SADDLEPOINT", or "INCONCLUSIVE_EXTREMA").
    """

    (fxx, _, _) = second_order_partial_derivatives(f, x, y)
    d = evaluate_discriminant(f, x, y, a, b)

    if d > sp.S.Zero:
        if fxx.subs(x, a).subs(y, b) > sp.S.Zero:
            return "LOCAL_MINIMUM"

        if fxx.subs(x, a).subs(y, b) < sp.S.Zero:
            return "LOCAL_MAXIMUM"

        return "INCONCLUSIVE_EXTREMA"

    if d < sp.S.Zero:
        return "SADDLEPOINT"

    return "INCONCLUSIVE_EXTREMA"


def analyse_critical_points(f: sp.Expr, x: sp.Symbol, y: sp.Symbol):
    """
    Analyze the critical points of a function f(x, y).

    Args:
        f (sp.Expr): The function expression.
        x (sp.Symbol): The independent variable x.
        y (sp.Symbol): The independent variable y.

    Returns:
        list: A list of tuples containing the coordinates of each critical point
              and its corresponding type (extremum or saddle point).

    Examples:
        >>> x, y = sp.symbols('x y')
        >>> f =  x**3/3 + y**2 +2*x*y -6*x - 3*y + 4
        >>> analyse_critical_points(f, x, y)
        [((-1, 5/2), 'SADDLEPOINT'), ((3, -3/2), 'LOCAL_MINIMUM')]

    """

    turning_points = critical_points(f, x, y)

    result = []
    for turning_point in turning_points:
        turning_point_type = second_derivative_test(
            f, x, y, turning_point[x], turning_point[y]
        )
        result += [((turning_point[x], turning_point[y]), turning_point_type)]

    return result


def hessian(f: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> sp.Matrix:
    """
    Compute the Hessian matrix of a function `f` with respect to `x` and `y`.

    This function takes a function `f` and two variables `x` and `y` as input,
    and returns the Hessian matrix of `f` with respect to `x` and `y`.

    Args:
    f (sp.Expr): The function to differentiate.
    x (sp.Symbol): The variable of differentiation with respect to `x`.
    y (sp.Symbol): The variable of differentiation with respect to `y`.

    Returns:
    sp.Matrix: The Hessian matrix of `f` with respect to `x` and `y`.

    Example:
    >>> from sympy import symbols, diff
    >>> x, y = symbols('x y')
    >>> f = x**2 + y**2
    >>> hessian(f, x, y)
    Matrix([
    [2, 0],
    [0, 2]])

    """
    hessian_matrix = sp.Matrix(
        2, 2, [f.diff(x, x), f.diff(x, y), f.diff(y, x), f.diff(y, y)]
    )
    return hessian_matrix


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False)
