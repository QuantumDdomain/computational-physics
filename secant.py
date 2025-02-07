import math

def fn_1(x):
    return math.exp(2*x)-math.exp(x)-2

def fn_2(x):
    return x**(3) +4*x**(2) - 10

def secant_method(fn, x0, x1, tol=1e-6):
    iterations = 0
    while True:
        x_temp = x1 - fn(x1) * (x1 - x0) / (fn(x1) - fn(x0))
        x0 = x1
        x1 = x_temp
        iterations += 1

        if abs((x1 - x0)/x1) < tol :
            break
    return x1,iterations


root_1,iters_1 = secant_method(fn_1,0, 1)
print(root_1,iters_1)

root_2,iters_2 = secant_method(fn_2,1, 2)
print(root_2,iters_2)