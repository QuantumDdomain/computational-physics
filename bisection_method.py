import math

def fn_1(x):
    return math.exp(2*x)-math.exp(x)-2

def fn_2(x):
    return x**(3) +4*x**(2) - 10

def bisection_method(fn,a, b, tol=1e-6):
    iterations=0
    while abs((b - a)/b) > tol:
        c = (a + b) / 2
        if fn(c) == 0:
            break
        elif fn(a) * fn(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return (a + b) / 2,iterations

root_1,iters_1 = bisection_method(fn_1,0, 1)
print(root_1,iters_1)

root_2,iters_2 = bisection_method(fn_2,1, 2)
print(root_2,iters_2)
