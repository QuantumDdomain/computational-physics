from sympy import *
import cmath

def g(z):
    return (z**3 + 1)

def f(z_val):
    z = symbols('z')
    func = g(z)
    derivative = diff(func, z)
    return derivative.subs(z, z_val)

def newton_raphson_complex(z, tol=1e-8):
    iterations = 0
    while True:
        gz = g(z)
        fz = f(z)
        if fz == 0:
            raise ValueError("Derivative is zero. Newton-Raphson method fails.")
        z_new = z - gz / fz
        if abs(N((z_new - z)/z_new)) >= tol:  # Convert to numerical value for comparison
            z = z_new
            iterations += 1
        else:
            break
    return N(z), iterations  # Return the numerical value of the root

try:
    root, iters = newton_raphson_complex(complex(1, 1))
    print('Root found:', root)
    print('Number of iterations:', iters)
except ValueError as e:
    print(e)
