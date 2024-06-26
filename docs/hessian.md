# Hessian

1. **Discriminant**:
   - The **discriminant** is a mathematical concept used to determine the 
   nature of critical points (extrema) of a multivariable function.
   - Specifically, it helps us identify whether a critical point corresponds 
   to a local maximum, local minimum, or a saddle point.
   - The **second partial derivatives** of the function play a crucial 
   role in calculating the discriminant.

2. **Procedure for Finding Extrema of Multivariable Functions**:
   - Given a function $f(x, y)$, follow these steps:
     1. Calculate the **gradient** of $f$ and set each component to zero 
     to find the critical points.
     2. Use the **Hessian matrix**, which contains second partial derivatives, 
     to analyze the critical points.
     3. Check the **determinant** of the Hessian matrix:
        - If the determinant is **positive**, the point is either a 
        **local maximum** or a **local minimum**.
        - If the determinant is **negative**, the point is a **saddle point**.
        - If the determinant is **indefinite**, the second derivative 
        test is inconclusive.

3. **Example**:
   - Consider the function $f(x, y) = x^2 + y^2$.
   - Calculate the gradient: $\nabla f = (2x, 2y)$.
   - Set each component to zero: $2x = 0$ and $2y = 0$.
   - Solve for $x$ and $y$ to obtain the critical point $(0, 0)$.
   - Compute the Hessian matrix:
     $\displaystyle H =
        \begin{bmatrix}
            \frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\
            \frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2}
        \end{bmatrix}
    $
   - Evaluate the second partial derivatives and substitute them into the Hessian matrix.
   - Calculate the determinant of $H$:
     - If $\text{det}(H) > 0$, the critical point is a local maximum or minimum.
     - If $\text{det}(H) < 0$, the critical point is a saddle point.
     - If $\text{det}(H)$ is indefinite, further analysis is needed.

Remember that the discriminant helps us classify critical points based 
on their behaviour in multivariable functions. 🌟
