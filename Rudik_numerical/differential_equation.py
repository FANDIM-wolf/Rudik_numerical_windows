import numpy as np
import sympy as sp
def create_function_from_expr_for_differential_equation(expr):
    t = sp.Symbol('t')
    y = sp.Symbol('y')
    f = sp.lambdify([t, y], expr, modules=['numpy'])
    return f

def create_function_from_string(f_str):
    """
    Translates a string representation of a function into a Python function.
    
    Parameters:
    f_str (str): String representation of the function.
    
    Returns:
    function: Python function that can be used in the euler_method().
    """
    t, y = sp.symbols('t y')
    expr = sp.sympify(f_str)
    f = sp.lambdify([t, y], expr, modules=['numpy'])
    return f

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
expr = sp.sin(sp.Symbol('t') / (1 + sp.Symbol('y')**3))
f = create_function_from_expr_for_differential_equation(expr)

#x0 = 0
#y0 = 1
#t_span = (0, 2)
#n = 40

#t, y = euler(f, x0, y0, t_span, n)

#print("Independent variable (t):")
#print(t)
#print("\nApproximate solution (y):")
#print(y)



import sympy as sp
import numpy as np
import math

def euler_method(f, x0, y0, x_end, n):
    """
    Solves a first order linear differential equation using Euler's method.
    
    Parameters:
    f (function): Function representing the right-hand side of the equation dy/dt = f(t, y).
    x0 (float): The initial value of x.
    y0 (float): The initial value of y.
    x_end (float): The end value of x.
    n (int): Number of steps.
    
    Returns:
    numpy.ndarray: An array of x values.
    numpy.ndarray: Array of y values.

  
    """
    h = (x_end - x0) / n
    t_values = np.linspace(x0, x_end, n+1)
    y_values = np.zeros_like(t_values)
    y_values[0] = y0
    
    for i in range(n):
        y_values[i+1] = y_values[i] + h * f(t_values[i], y_values[i])
    
    return t_values, y_values

# Example of using 
f_str = "2*y - sin(t) - 0.2"
f_str= "sin(y)+sqrt(t+2)+2*y**2"
f_func = create_function_from_string(f_str)

x0 = 0
y0 = 1
x_end = 2
n = 10

x_values, y_values = euler_method(f_func, x0, y0, x_end, n)

print("t:", x_values)
print("y:", y_values)