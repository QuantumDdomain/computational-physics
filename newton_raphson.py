from sympy import symbols, exp, diff

def g_1(x):
    return exp(2 * x) - exp(x) - 2

def g_2(x):
    return x**(3) +4*x**(2) - 10

def f_1(x_val):
    x = symbols('x')
    func=g_1(x)
    derivative = diff(func, x)
    return derivative.subs(x, x_val)

def newton_raphson_1(x, tol=1e-6):
    iterations = 0
    while True:
        gx = g_1(x) 
        fx = f_1(x)  
        if fx == 0:
            raise ValueError("Derivative is zero. Newton-Raphson method fails.")
        x_new = x - gx / fx 
        if abs((x_new - x)/x_new) >= tol: 
            x = x_new
            iterations += 1
        else:
            break 
    return x,iterations

def f_2(x_val):
    x = symbols('x')
    func=g_2(x)
    derivative = diff(func, x)
    return derivative.subs(x, x_val)

def newton_raphson_2(x, tol=1e-6):
    iterations = 0
    while True:
        gx = g_2(x) 
        fx = f_2(x)  
        if fx == 0:
            raise ValueError("Derivative is zero. Newton-Raphson method fails.")
        x_new = x - gx / fx 
        if abs((x_new - x)/x_new) >= tol: 
            x = x_new
            iterations += 1
        else:
            break 
    return x,iterations

try:
    root_1 ,iters_1 = newton_raphson_1(0.5)
    print('root_1 found :',root_1)
    print('Iteration_1 value is :',iters_1)
except ValueError as e:
    print(e)

try:
    root_2 ,iters_2 = newton_raphson_2(1.5)
    print('root_2 found :',root_2)
    print('Iteration_2 value is :',iters_2)
except ValueError as e:
    print(e)