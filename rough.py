import numpy as np
import sympy as sp

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

def exact_integral(f_sym, a, b):
    x = sp.symbols('x')
    return sp.integrate(f_sym, (x, a, b)).evalf()

def truncation_error(exact, approx):
    return abs(exact - approx)

# Define functions
f1 = lambda x: x**3 + 1
f1_sym = sp.symbols('x')**3 + 1

# Intervals
a1, b1 = 1, 2
a2, b2 = 1, 1.5

# Exact integrals
exact1 = exact_integral(f1_sym, a1, b1)
exact2 = exact_integral(f1_sym, a2, b2)

# Numerical approximations
I1_n2 = trapezoidal_rule(f1, a1, b1, 2)
I1_n4 = trapezoidal_rule(f1, a1, b1, 4)
I2_n2 = trapezoidal_rule(f1, a2, b2, 2)
I2_n4 = trapezoidal_rule(f1, a2, b2, 4)

# Errors
error1_n2 = truncation_error(exact1, I1_n2)
error1_n4 = truncation_error(exact1, I1_n4)
error2_n2 = truncation_error(exact2, I2_n2)
error2_n4 = truncation_error(exact2, I2_n4)

print(f"Exact integral for [1,2]: {exact1}")
print(f"Trapezoidal (n=2): {I1_n2}, Error: {error1_n2}")
print(f"Trapezoidal (n=4): {I1_n4}, Error: {error1_n4}\n")
print(f"Exact integral for [1,1.5]: {exact2}")
print(f"Trapezoidal (n=2): {I2_n2}, Error: {error2_n2}")
print(f"Trapezoidal (n=4): {I2_n4}, Error: {error2_n4}\n")

# Second set of integrals
integrals = [
    (lambda x: 3*x**2 + 2*x - 5, sp.symbols('x')**2 * 3 + sp.symbols('x')*2 - 5, 0, 2),
    (lambda x: np.exp(x), sp.exp(sp.symbols('x')), -1, 1),
    (lambda x: 3*np.cos(x) + 5, 3*sp.cos(sp.symbols('x')) + 5, 0, np.pi)
]

for i, (func, func_sym, a, b) in enumerate(integrals, 1):
    exact = exact_integral(func_sym, a, b)
    I_n2 = trapezoidal_rule(func, a, b, 2)
    I_n4 = trapezoidal_rule(func, a, b, 4)
    error_n2 = truncation_error(exact, I_n2)
    error_n4 = truncation_error(exact, I_n4)
    print(f"Integral {i}: Exact = {exact}")
    print(f"Trapezoidal (n=2): {I_n2}, Error: {error_n2}")
    print(f"Trapezoidal (n=4): {I_n4}, Error: {error_n4}\n")
