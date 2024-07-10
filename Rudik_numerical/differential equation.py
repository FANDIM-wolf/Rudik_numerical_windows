import numpy as np
import sympy as sp
from support_tools import create_function_from_expr_for_differential_equation


def euler(f, x0, y0, t_span, n):
    """
    Solves a first-order ordinary differential equation using the Euler method.
    
    Parameters:
    f (function): The right-hand side of the differential equation dy/dt = f(t, y).
    x0 (float): The initial value of the independent variable (e.g., time).
    y0 (float): The initial value of the dependent variable.
    t_span (tuple): A tuple containing the start and end values of the independent variable.
    n (int): The number of steps to take.
    
    Returns:
    numpy.ndarray: The values of the independent variable.
    numpy.ndarray: The approximate solution of the differential equation.
    """
    t0, tf = t_span
    h = (tf - t0) / n
    
    t = np.linspace(t0, tf, n+1)
    y = np.zeros_like(t)
    y[0] = y0
    
    for i in range(n):
        y[i+1] = y[i] + h * f(t[i], y[i])
    
    return t, y

# Example usage sin(t/(1+y**2)
#expr = sp.sin(sp.Symbol('t') / (1 + sp.Symbol('y')**3))
#f = create_function_from_expr_for_differential_equation(expr)

#x0 = 0
#y0 = 1
#t_span = (0, 2)
#n = 40

#t, y = euler(f, x0, y0, t_span, n)

#print("Independent variable (t):")
#print(t)
#print("\nApproximate solution (y):")
#print(y)