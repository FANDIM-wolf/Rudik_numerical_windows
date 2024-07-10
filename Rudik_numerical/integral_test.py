from Rudik_numerical import integrals
from Rudik_numerical.support import support_tools

f_str = support_tools.create_function_from_expr("-6.7*exp(-6.7*x)")
a = 0
b = 5
n = 100

result = integrals.integral_simpson(f_str, a, b, n)
print(f"Approximate value of the integral 1: {result:.6f}")