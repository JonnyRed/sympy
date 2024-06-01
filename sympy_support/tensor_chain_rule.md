# Tensor Chain Rule

In multivariate calculus can the chain rule be expressed in tensor calculus notation

In multivariate calculus can the chain tulle be expressed in Einstein summation convention

Yes, the chain rule in multivariate calculus can indeed be expressed using tensor calculus notation. In this context, the chain rule relates the derivatives of composite functions and can be succinctly expressed using partial derivatives and the Einstein summation convention.

## Tensor Notation Chain Rule 1

Let's consider a function $f$ that depends on variables $y^i$, which in turn depend on variables $x^j$. We want to find the partial derivatives of $f$ with respect to $x^j$.

1. **Variables**:
   - $f = f(y^i)$
   - $y^i = y^i(x^j)$

2. **Chain Rule in Tensor Notation**:
   The chain rule for the partial derivative of $f$ with respect to $x^j$ is given by:
   $$
   \frac{\partial f}{\partial x^j} = \frac{\partial f}{\partial y^i} \frac{\partial y^i}{\partial x^j}
   $$

### Einstein Summation Convention

Using the Einstein summation convention, we can write the chain rule without explicitly writing the summation symbol $\sum$. In this convention, repeated indices imply summation over those indices. The chain rule thus becomes:
$$
\frac{\partial f}{\partial x^j} = \frac{\partial f}{\partial y^i} \frac{\partial y^i}{\partial x^j}
$$

Here, the index $i$ is summed over its range (typically 1 to the number of dimensions).

### Example

Consider a function $f$ of two variables $y^1$ and $y^2$, which are themselves functions of two other variables $x^1$ and $x^2$. Explicitly, we have:

- $f = f(y^1, y^2)$
- $y^1 = y^1(x^1, x^2)$
- $y^2 = y^2(x^1, x^2)$

The chain rule in this case can be written as:
$$
\frac{\partial f}{\partial x^j} = \frac{\partial f}{\partial y^1} \frac{\partial y^1}{\partial x^j} + \frac{\partial f}{\partial y^2} \frac{\partial y^2}{\partial x^j}
$$

In Einstein summation convention, this is compactly expressed as:
$$
\frac{\partial f}{\partial x^j} = \frac{\partial f}{\partial y^i} \frac{\partial y^i}{\partial x^j}
$$

### Applying the Chain Rule

To illustrate, let's compute $\frac{\partial f}{\partial x^1}$ and $\frac{\partial f}{\partial x^2}$ step-by-step using the chain rule in tensor notation.

1. For $\frac{\partial f}{\partial x^1}$:
   $$
   \frac{\partial f}{\partial x^1} = \frac{\partial f}{\partial y^1} \frac{\partial y^1}{\partial x^1} + \frac{\partial f}{\partial y^2} \frac{\partial y^2}{\partial x^1}
   $$

2. For $\frac{\partial f}{\partial x^2}$:
   $$
   \frac{\partial f}{\partial x^2} = \frac{\partial f}{\partial y^1} \frac{\partial y^1}{\partial x^2} + \frac{\partial f}{\partial y^2} \frac{\partial y^2}{\partial x^2}
   $$

## Tensor Notation Chain Rule 2

The chain rule describes how to differentiate a composite function, and in the context of tensor calculus, this involves dealing with partial derivatives and transformation rules between different coordinate systems.

### Tensor Calculus for the Chain Rule

Consider a function $f$ that depends on variables $x^i$ (where $i$ runs from 1 to $n$). If these variables $x^i$ themselves are functions of other variables $y^j$ (where $j$ runs from 1 to $m$), we can write $f$ as a composition:

$$f = f(x^1, x^2, \ldots, x^n)$$
$$x^i = x^i(y^1, y^2, \ldots, y^m)$$

To find the partial derivative of $f$ with respect to $y^j$, we apply the chain rule. In tensor notation, this is expressed as:

$$\frac{\partial f}{\partial y^j} = \sum_{i=1}^n \frac{\partial f}{\partial x^i} \frac{\partial x^i}{\partial y^j}$$

Using Einstein summation convention, which implies summation over repeated indices, we can write this more compactly as:

$$\frac{\partial f}{\partial y^j} = \frac{\partial f}{\partial x^i} \frac{\partial x^i}{\partial y^j}$$

Here’s how this works in detail:

1. **Function Composition**: $f$ is a function of $x^i$, and each $x^i$ is a function of $y^j$.
2. **Partial Derivatives**:
   - $\frac{\partial f}{\partial x^i}$ is the partial derivative of $f$ with respect to $x^i$.
   - $\frac{\partial x^i}{\partial y^j}$ is the partial derivative of $x^i$ with respect to $y^j$.

### Example 2

Let’s consider an example where $f$ is a function of two variables $x$ and $z$, and these variables are themselves functions of $y$ and $w$:

$$f = f(x, z)$$
$$x = x(y, w)$$
$$z = z(y, w)$$

To find $\frac{\partial f}{\partial y}$ using the chain rule in tensor notation, we write:

$$\frac{\partial f}{\partial y} = \frac{\partial f}{\partial x} \frac{\partial x}{\partial y} + \frac{\partial f}{\partial z} \frac{\partial z}{\partial y}$$

Using Einstein summation convention, this becomes:

$$\frac{\partial f}{\partial y} = \frac{\partial f}{\partial x^i} \frac{\partial x^i}{\partial y}$$

where $x^i$ runs over $x$ and $z$, i.e., $x^1 = x$ and $x^2 = z$.

Explicitly, this is:

$$\frac{\partial f}{\partial y} = \frac{\partial f}{\partial x} \frac{\partial x}{\partial y} + \frac{\partial f}{\partial z} \frac{\partial z}{\partial y}$$

Similarly, for $\frac{\partial f}{\partial w}$:

$$\frac{\partial f}{\partial w} = \frac{\partial f}{\partial x} \frac{\partial x}{\partial w} + \frac{\partial f}{\partial z} \frac{\partial z}{\partial w}$$

### Summary

The chain rule in multivariate calculus can indeed be elegantly expressed using tensor calculus notation. The key idea is to use partial derivatives and the Einstein summation convention to compactly represent the sums over the intermediate variables. This notation is particularly powerful in theoretical physics and differential geometry, where it provides a concise and clear framework for dealing with transformations between different coordinate systems.
