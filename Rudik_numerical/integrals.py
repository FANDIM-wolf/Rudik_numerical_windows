import math
import sympy 
from . import support_tools as support_tools

def integral_rectangle(f, a, b, n):
    """
  Calculates the definite integral of the function f(x) on the segment [a, b] 
    the method of rectangles with n partitions.
    
    Parameters:
    f_str (str): String representation of the integral function.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of partitions of the integration segment.
    
    Returns:
    float: The approximate value of a certain integral.
    """
    
    
    h = (b - a) / n  # length of each partition
    s = 0
    for i in range(n):
        x = a + i * h
        s += f(x)
    return h * s

# Example 1:
#f_str =create_function_from_expr("tan(x/3)+0.5")
#a = 0
#b = 2
#n = 100

#result = integral_rectangle(f_str, a, b, n)
#print(f"Approximate value of the integral: {result:.6f}")

def integral_trapezoids(f, a, b, n):
    """
    Calculates the definite integral of the function f(x) on the segment [a, b] 
    the trapezoid method with n partitions.
    
    Parameters:
    f (function): Function, integral function.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of partitions of the integration segment.
    
    Returns:
    float: The approximate value of a certain integral.
    """
    h = (b - a) / n  # length of each partition
    s = 0.5 * f(a)  # First and last element of the sum
    for i in range(1, n):
        x = a + i * h
        s += f(x)
    s += 0.5 * f(b)  # last element of the sum
    return h * s

# Example  2:
#f_str = create_function_from_expr("tan(x/3)+0.5+x**2")
#a = 0
#b = 2
#n = 100

#result = integral_trapezoids(f_str, a, b, n)
#print(f"Approximate value of the integral: {result:.6f}")


def integral_simpson(f, a, b, n):
    """
    Calculates the definite integral of the function f(x) on the segment [a, b] 
    using Simpson's method with n partitions.
    
    Parameters:
    f (function): The function to integrate.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of partitions of the integration segment (must be even).
    
    Returns:
    float: The approximate value of the definite integral.
    """
    if n % 2 != 0:
        raise ValueError("The number of partitions must be even")
    
    h = (b - a) / n  # The length of each interval
    x = a
    s = f(a) + f(b)
    
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        s += 2 * f(a + i * h)
    
    return h * s / 3

# Example usage
f_str = support_tools.create_function_from_expr("0.0039*x*0.35*exp(-0.00297*1.35)")
a = 0
b = 2
n = 100

result = integral_simpson(f_str, a, b, n)
print(f"Approximate value of the integral 0: {result:.6f}")

f_str = support_tools.create_function_from_expr("-6.7*exp(-6.7*x)")
a = 0
b = 5
n = 100

result = integral_simpson(f_str, a, b, n)
print(f"Approximate value of the integral 1: {result:.6f}")