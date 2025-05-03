from sympy import nsimplify, pi, sqrt, E
from fractions import Fraction

def approximation(result):
    expr = result
    try:
        f = Fraction(str(expr)).limit_denominator()
    except Exception:
        return expr  # fallback to raw result if conversion fails
    
    approx_pi = nsimplify(expr, [pi], tolerance=1e-6)
    approx_e  = nsimplify(expr, [E],  tolerance=1e-6)

    sqrt_constants = [2, 3, 5, 7, 10]
    approx_sqrts = [(n, nsimplify(expr, [sqrt(n)], tolerance=1e-6)) for n in sqrt_constants]

    num = f.numerator
    denom = f.denominator

    # Check for pi
    if 'pi' in str(approx_pi) and len(str(approx_pi)) < 9:
        return approx_pi

    # Check for e
    if 'E' in str(approx_e) and len(str(approx_e)) < 8:
        return approx_e

    # Check for "nice" fraction
    if ((num < 100 and denom < 10) or (num < 10 and denom < 100)):
        return f

    # Check for square roots
    for n, approx in approx_sqrts:
        approx_str = str(approx)
        if 'sqrt' in approx_str and len(approx_str) < 14:
            return approx

    # Default to raw float
    return expr

f1 = lambda x,y,z : y*z + x
f2 = lambda x,y,z : x*z + y

def runge_kutta_multivariable(f1 ,f2 ,X ,x_0 ,y_0 ,z_0,h ):
    x_i = x_0
    y_i = y_0
    z_i = z_0
    n = int ((X - x_0)/h)
    for j in range(n):
        k1 = h * f1(x_i, y_i, z_i)
        l1 = h * f2(x_i, y_i, z_i)
        k2 = h * f1(x_i + h/2, y_i + k1/2, z_i + l1/2)
        l2 = h * f2(x_i + h/2, y_i + k1/2, z_i + l1/2)
        k3 = h * f1(x_i + h/2, y_i + k2/2, z_i + l2/2)
        l3 = h * f2(x_i + h/2, y_i + k2/2, z_i + l2/2)
        k4 = h * f1(x_i + h, y_i + k3, z_i + l3)
        l4 = h * f2(x_i + h, y_i + k3, z_i + l3)
        y_i += ((k1 + 2 * (k2 + k3) + k4)/6)
        z_i += ((l1 + 2 * (l2 + l3) + l4)/6)
        x_i += h

    y,z = approximation(y_i),approximation(z_i)
    
    return y,z

solution = runge_kutta_multivariable(f1 ,f2 ,0.1 ,0 ,1 ,-1,0.01 )
result = print(solution)