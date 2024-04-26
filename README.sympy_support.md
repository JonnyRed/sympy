# Sympy Support

## generalised_chain_rule_for and generalised_chain_rule

* This code defines two functions in Python, `generalised_chain_rule_for`
and `generalised_chain_rule`, both of which are related to the concept of
the chain rule in calculus.
* `generalised_chain_rule_for` is a function that takes in four arguments:
`j, f`, variables, and `args`. `j` is an integer representing the index of
the variable with respect to which the differentiation is performed. `f`
is a symbolic function, variables is a dictionary containing the independent
variables and their corresponding expressions, and `args` is a tuple of the
independent variables.
* The function returns the differential of the composite function `f` with
respect to the `j`-th component of `args`, calculated using the chain rule.
The chain rule is implemented using a sum of the product of the partial
derivative of f with respect to each independent variable and the derivative
of the corresponding expression with respect to the `j`-th component of `args`.
* The function also includes two examples to illustrate its usage.
  * The first example calculates the differential of the composite function
  `f(x, y)` with respect to `r` using the chain rule, where `x` and `y`
  are expressed in terms of `r` and theta.
  * The second example calculates the differential of the same composite
  function with respect to `theta` using the chain rule.

* generalised_chain_rule is a function that takes in three arguments:
`w`, variables, and `args`. `w` is a symbolic function, variables is a
dictionary containing the independent variables and their corresponding
expressions, and `args` is a tuple of the independent variables.
* The function returns the differential of the composite function `w`
with respect to the independent variables args, calculated using the chain rule.
The chain rule is implemented using a sum of the product of the
partial derivative of w with respect to each independent variable and the
derivative of the corresponding expression with respect to the
independent variables.

```python
>>> import sympy as sp
>>> from  sympy_support.generalised_chain_rule import generalised_chain_rule_for, generalised_chain_rule

>>> x, y, z, r, theta = sp.symbols("x, y, z, r, theta", real=True)
>>> f = sp.symbols("f", cls=sp.Function)

>>> generalised_chain_rule_for(0, f, {x: r * sp.cos(theta), y: r * sp.sin(theta)}, r, theta)
sin(theta)*Derivative(f(x, y), y) + cos(theta)*Derivative(f(x, y), x)

>>> generalised_chain_rule_for(1, f, {x: r * sp.cos(theta), y: r * sp.sin(theta)}, r, theta)
-r*sin(theta)*Derivative(f(x, y), x) + r*cos(theta)*Derivative(f(x, y), y)

# w = f(x,y), x = sin(t), y = cos(t) calculate df/dt
>>> x, y, t = sp.symbols("x, y, t", real=True)
>>> dependents = {x: sp.sin(t), y: sp.cos(t)}
>>> f = sp.Function("f")
>>> generalised_chain_rule(f, dependents, t)
(Eq(Derivative(f(t), t), -sin(t)*Derivative(f(x, y), y) + cos(t)*Derivative(f(x, y), x)),)

>>> generalised_chain_rule(f, dependents, t)[0].lhs
Derivative(f(t), t)

>>> generalised_chain_rule(f, dependents, t)[0].rhs
-sin(t)*Derivative(f(x, y), y) + cos(t)*Derivative(f(x, y), x)


```

## find_dependent_variable_differentials

* `find_dependent_variable_differentials` that calculates the partial
derivatives of a given function `w` (represented as a SymPy Function symbol)
with respect to a set of independent variables `args`. The function
takes into account the dependencies of the variables on other variables,
which are provided in the variables dictionary.
* The function  defines the `find_dependent_variable_differentials` function,
which takes in the function symbol `w`, the dictionary of dependent variables,
and the independent variables args.
* The function then calculates the partial derivatives of the function `w`
with respect to each of the independent variables in args. It does this
by using the chain rule to express the partial derivatives in terms of
the partial derivatives of the dependent variables in variables.
* The function returns a list of equations, where each equation gives
the partial derivative of the function w with respect to one of the
independent variables in args.
* The example provided in the docstring demonstrates how to use the function.
  * It defines two dependent variables `x` and `y` in terms of the
  independent variables r and theta
  * It then uses `find_dependent_variable_differentials` to calculate
  the partial derivatives of a function `f` with respect to `x` and `y`.

```python
>>> import sympy as sp
>>> from  sympy_support.generalised_chain_rule import find_dependent_variable_differentials
>>> x, y, r, theta = sp.symbols("x, y, r, theta", real=True)
>>> dependents = {x: r * sp.cos(theta), y: r * sp.sin(theta)}
>>> f = sp.Function("f")

>>> result = find_dependent_variable_differentials(f, dependents, r, theta)
>>> result[sp.Derivative(f(x, y), x)]
cos(theta)*Derivative(f(r, theta), r) - sin(theta)*Derivative(f(r, theta), theta)/r

>>> result[sp.Derivative(f(x, y), y)]
sin(theta)*Derivative(f(r, theta), r) + cos(theta)*Derivative(f(r, theta), theta)/r

```
