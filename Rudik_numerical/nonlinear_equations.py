import numpy as np
import sympy as sp

def solve_equations(z1_str, z2_str, initial_x, initial_y, precision=1e-5):
    # Convert the strings to Sympy expressions
    x, y = sp.symbols('x y')
    z1 = sp.sympify(z1_str)
    z2 = sp.sympify(z2_str)

    # Find the partial derivatives
    dZ1x = sp.diff(z1, x)
    dZ1y = sp.diff(z1, y)
    dZ2x = sp.diff(z2, x)
    dZ2y = sp.diff(z2, y)

    # Convert the symbolic expressions to functions using numpy
    f1 = sp.lambdify([x, y], z1, modules='numpy')
    f2 = sp.lambdify([x, y], z2, modules='numpy')
    dF1x = sp.lambdify([x, y], dZ1x, modules='numpy')
    dF1y = sp.lambdify([x, y], dZ1y, modules='numpy')
    dF2x = sp.lambdify([x, y], dZ2x, modules='numpy')
    dF2y = sp.lambdify([x, y], dZ2y, modules='numpy')

    # Initialize variables
    x = initial_x
    y = initial_y
    err = precision
    n = 0

    # Iterate until the error is less than the precision
    while err >= precision:
        F1 = f1(x, y)
        F2 = f2(x, y)
        hF2y = dF2y(x, y)
        hF2x = dF2x(x, y)
        hF1y = dF1y(x, y)
        hF1x = dF1x(x, y)
        dF = np.array([[dF1x(x, y), dF1y(x, y)], [dF2x(x, y), dF2y(x, y)]])
        J = np.linalg.det(dF)
        x1 = x
        y1 = y
        x = x1 - (1/J)*(F1*hF2y - F2*hF1y)
        y = y1 + (1/J)*(F1*hF2x - F2*hF1x)
        if abs(x1 - x) > abs(y1 - y):
            err = abs(x1 - x)
        else:
            err = abs(y1 - y)
        n += 1

    return x, y, n

# Get the initial approximation from user input
initial_x = float(input('initial approximation x='))
initial_y = float(input('initial approximation y='))

# Solve the equations
result_x, result_y, iterations = solve_equations("tan(x*y+0.2)-x**2", "x**2+2*y**2-1", initial_x, initial_y)

# Print the result
print(f'x = {result_x:.5f}, y = {result_y:.5f}, iterations = {iterations}')