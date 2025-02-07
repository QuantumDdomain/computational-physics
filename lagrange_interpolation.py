import numpy as np

def lagrange_interpolation (x):

    A = np.array([1.2 , 1.3, 1.4, 1.5])
    B = np.array([1.063 , 1.091, 1.119, 1.145])
    n = len(A)
    L = np.zeros(n)

    y = 0
    for i in range(n):
        l = 1
        for j in range(n):
            if (i != j):
                l *= (x-A[j]) / (A[i] - A[j])   
        L[i] = l
        y += B[i] * L[i]

    return y

x = 1.35
solution = lagrange_interpolation(x)
print(solution)