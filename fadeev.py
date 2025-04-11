import numpy as np

A = np.array([[4,1],[2,3]])

def my_trace(A):
    sum = 0
    n = len(A)
    for i in range(n):
        sum += A[i][i]
    return sum

def fadeev(B):
    A = B
    n = len(A)
    I = np.identity(n)
    alpha = np.zeros(n+1)
    alpha[0] = 1
    c_k = A
    for i in range(1,n+1):
        alpha[i] = -my_trace(c_k)/i
        c_k = np.dot(A,c_k) + alpha[i] * np.dot(A,I)
  
    def poly_fn(x):
        return sum(alpha[i] * x**(n-i) for i in range(n+1))
    
    return poly_fn

f = fadeev(A)
print(f)

def secant_method(fn, x0, x1):
    iterations = 0
    tol=1e-6
    while True:
        x_temp = x1 - fn(x1) * (x1 - x0) / (fn(x1) - fn(x0))
        x0 = x1
        x1 = x_temp
        iterations += 1

        if abs((x1 - x0)/x1) < tol :
            break
    return x1


solution = secant_method(f,0,3)
print(solution)

        