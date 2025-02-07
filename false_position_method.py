import math

def fn_1(x):
    return math.exp(2*x)-math.exp(x)-2

def fn_2(x):
    return x**(3) +4*x**(2) - 10

def false_position_method(fn,a, b, tol=1e-6):
    if fn(a) * fn(b) > 0:
        raise ValueError("The function must have opposite signs at a and b")

    c = a  
    iterations = 0
    while abs(fn(c)) > tol:
        iterations += 1
        c = b - (fn(b) * (b - a)) / (fn(b) - fn(a))
        if fn(a) * fn(c) < 0: 
            b = c
        else:
            a = c
    return c,iterations


try:
    root_1 ,iters_1 = false_position_method(fn_1,0, 1)
    print('Root_1 found: ',root_1)
    print('Iteration_1 value is :',iters_1)
except ValueError as e:
    print(e)

try:
    root_2 ,iters_2 = false_position_method(fn_2,1, 2)
    print('Root_2 found: ',root_2)
    print('Iteration_2 value is :',iters_2)
except ValueError as e:
    print(e)