"""
Module Documentation: generalised_chain_rule

This module provides functions for applying the generalized chain rule in SymPy.

1. Imports:

   • doctest: Used for testing the module's functionality with examples.
   • sympy as sp: Imports the SymPy library for symbolic manipulation.

2. Constants:

   • HALF: Represents the constant 1/2 as a symbolic expression using
   sp.S.Half.
   • PI: Represents the constant π as a symbolic expression using sp.pi.
   • E: Represents the mathematical constant e (base of the natural logarithm)
   using sp.exp.
   • POSITIVEINFINITY: Represents positive infinity as a symbolic
   expression using sp.S.Infinity.

3. Functions:

a. generalised_chain_rule_for(j, w, variables, *args)

   • Description: Calculates the j'th term of the chain rule for a given
   function and variables.
   • Arguments:
        ◦ j: The index in args that is to be differentiated for.
        ◦ w: The function to be differentiated.
        ◦ variables: A dictionary containing dependent variables and
        their definitions as symbolic expressions.
        ◦ *args: Independent variables.
   • Returns:
        ◦ A symbolic expression representing the partial derivative of
        w with respect to the j'th component of args.
   • Examples:
        ◦ Demonstrates how to use the function for specific cases involving
        polar coordinates and other
          transformations.

b. generalised_chain_rule(w, variables, *args)

   • Description: Applies the generalized chain rule to a function with
   multiple variables and composite arguments.
   • Arguments:
        ◦ w: A SymPy function symbol to be differentiated.
        ◦ variables: A dictionary containing dependent variables and their
        definitions as symbolic expressions.
        ◦ *args: Independent variables.
   • Returns:
        ◦ A list of sympy.Eq objects, each representing an equation expressing
        the partial derivative of w with respect to one of the independent
        variables in args.
   • Examples:
        ◦ Shows how to use the function to find the derivative of a composite
        function with respect to an independent
          variable, involving substitutions and simplifications.

c. chain_rule_derivative(expr, variables, *args)

   • Description: Differentiates an expression with respect to independent
   variables using the chain rule.
   • Arguments:
        ◦ expr: The expression to be differentiated.
        ◦ variables: A dictionary containing dependent variables and their
        definitions as symbolic expressions.
        ◦ *args: Independent variables.
   • Returns:
        ◦ A list of sympy.Eq objects, each representing an equation expressing
        the derivative of expr with respect to
          one of the independent variables in args.
   • Examples:
        ◦ Demonstrates how to use the function with a specific function and
        its definition involving dependent
          variables, showing the resulting equations after differentiation and
          simplification.

4. if __name__ == "__main__": block:

   • This block uses doctest.testmod(verbose=False) to run the doctests
   defined in the examples within the functions for testing purposes.

Note:

   • The module uses a custom Function symbol named "f" for consistency in the
   examples. You can replace it with your actual function symbol in
   your applications.
   • Remember to import the sympy_chain_rule module and use its functions with
   appropriate arguments for your specific differentiation needs.

"""

import doctest

import sympy as sp

HALF = sp.S.Half
PI = sp.pi
E = sp.exp
POSITIVEINFINITY = sp.S.Infinity


def generalised_chain_rule_for(j, w, variables, *args):
    """The j'th term of the args that w is to be differentiate for.

    partial w/partial tj = partial w/partial xi partial xi/partial tj  ESC

    Args:
        j (_type_): the index in args that is to be differentiated for.
        w (_type_): the function to be differentiated
        variables (dict[sp.Symbol, sp.Expr]): dictionary of variables
            with their function definitions
        args: independent variables

    Returns:
        sp.Expr: The differential with respect to the j'th component of args

    Examples:
        >>> x, y, z, r, theta = sp.symbols("x, y, z, r, theta", real=True)
        >>> f = sp.symbols("f", cls=sp.Function)

        >>> generalised_chain_rule_for(0, f, {x: r * sp.cos(theta), y: r * sp.sin(theta)}, r, theta)
        sin(theta)*Derivative(f(x, y), y) + cos(theta)*Derivative(f(x, y), x)

        >>> generalised_chain_rule_for(1, f, {x: r * sp.cos(theta), y: r * sp.sin(theta)}, r, theta)
        -r*sin(theta)*Derivative(f(x, y), x) + r*cos(theta)*Derivative(f(x, y), y)
    """

    return sum(
        (w(*variables.keys()).diff(xi)) * expr.diff(args[j])
        for xi, expr in variables.items()
    )


def generalised_chain_rule(w: sp.Function, variables: dict[sp.Symbol, sp.Expr], *args):
    """The chain rule allows the differentiation of composite functions.

    A composite function is a function whose output is used as the
    input for another function. The generalized chain rule extends
    the basic chain rule to functions with multiple variables
    and composite arguments.

    The simple chain rule extended to functions of more than one independent
    variable, in which each independent variable may depend on one or more other variables

    Let w=f(x1,x2,…,xm) be a differentiable function of m  independent
    variables, and for each  i∈1,…,m,  let  xi=xi(t1,t2,…,tn)  be a
    differentiable function of n  independent variables. Then

    partial w/partial tj = partial w/partial xi partial xi/partial tj  ESC

    Given a composition of functions (e.g.,  f(x(t),y(t))), the intermediate
    variables are the variables that are independent in the outer function
    but dependent on other variables as well; in the function  f(x(t),y(t)),
    the variables  x and  y are examples of intermediate variables.

    Args:
        w (sp.Function): function symbol to be differentiated
        variables (dict[sp.Symbol, sp.Expr]): dictionary of variables
            with their function definitions
        args: independent variables

    Returns:
        list[sp.Eq]: list of equations giving function  differentiated
            wrt args

    Examples:
        w = f(x,y), x = sin(t), y = cos(t) calculate df/dt
        >>> x, y, t = sp.symbols("x, y, t", real=True)
        >>> dependents = {x: sp.sin(t), y: sp.cos(t)}
        >>> f = sp.Function("f")
        >>> generalised_chain_rule(f, dependents, t)
        (Eq(Derivative(f(t), t), -sin(t)*Derivative(f(x, y), y) + cos(t)*Derivative(f(x, y), x)),)

        >>> generalised_chain_rule(f, dependents, t)[0].lhs
        Derivative(f(t), t)

        >>> generalised_chain_rule(f, dependents, t)[0].rhs
        -sin(t)*Derivative(f(x, y), y) + cos(t)*Derivative(f(x, y), x)
    """

    result = ()
    for j, _ in enumerate(args):
        result = result + (
            sp.Eq(
                w(*args).diff(args[j]),
                generalised_chain_rule_for(j, w, variables, *args),
            ),
        )

    return result


def chain_rule_derivative(expr: sp.Expr, variables: dict[sp.Symbol, sp.Expr], *args):
    """Differentiate and expression with independent variables

    Args:
        expr (sp.Expr): function to be differentiated
        variables (dict[sp.Symbol, sp.Expr]): dictionary of variables
            with their function definitions
        args: independent variables

    Examples:
    >>> x, y, z, u, v = sp.symbols("x, y, z, u, v", real=True)
    >>> w = 3 * x**2 - 2 * x * y + 4 * z**2
    >>> dependents = {x: sp.exp(u) * sp.sin(v), y: sp.exp(u) * sp.cos(v), z: sp.exp(u)}
    >>> result = chain_rule_derivative(w, dependents, u, v)

    >>> result[0].lhs
    Derivative(f(u, v), u)
    >>> result[0].rhs
    2*(3*sin(v)**2 - sin(2*v) + 4)*exp(2*u)
    >>> result[0]
    Eq(Derivative(f(u, v), u), 2*(3*sin(v)**2 - sin(2*v) + 4)*exp(2*u))

    >>> result[1].lhs
    Derivative(f(u, v), v)
    >>> result[1].rhs
    (3*sin(2*v) - 2*cos(2*v))*exp(2*u)
    >>> result[1]
    Eq(Derivative(f(u, v), v), (3*sin(2*v) - 2*cos(2*v))*exp(2*u))

    """
    f = sp.Function("f")

    result = [
        sp.Eq(
            eqn.lhs,
            eqn.rhs.subs(
                f(*variables.keys()),
                expr,
            )
            .doit()
            .subs(variables)
            .simplify(),  # type: ignore
        )
        for eqn in generalised_chain_rule(f, variables, *args)
    ]

    return result


def find_dependent_variable_differentials(
    w: sp.Function, variables: dict[sp.Symbol, sp.Expr], *args
):
    """Find the intermediate differentials of the function

    Args:
        w (sp.Function): function symbol to be differentiated
        variables (dict[sp.Symbol, sp.Expr]): dictionary of variables
            with their function definitions
        args: independent variables

    Returns:
        list[sp.Eq]: list of equations giving function  differentiated
            wrt args

    Examples:
        >>> x, y, r, theta = sp.symbols("x, y, r, theta", real=True)
        >>> dependents = {x: r * sp.cos(theta), y: r * sp.sin(theta)}
        >>> f = sp.Function("f")
        >>> result = find_dependent_variable_differentials(f, dependents, r, theta)

        >>> result[sp.Derivative(f(x, y), x)]
        cos(theta)*Derivative(f(r, theta), r) - sin(theta)*Derivative(f(r, theta), theta)/r

        >>> result[sp.Derivative(f(x, y), y)]
        sin(theta)*Derivative(f(r, theta), r) + cos(theta)*Derivative(f(r, theta), theta)/r

    """
    independent_variable_differentials = generalised_chain_rule(w, variables, *args)
    differentials = [(w(*variables.keys()).diff(xi)) for xi in variables.keys()]
    return {
        a: b.simplify()
        for a, b in sp.solve(independent_variable_differentials, differentials).items()
    }


if __name__ == "__main__":
    doctest.testmod(verbose=False)
