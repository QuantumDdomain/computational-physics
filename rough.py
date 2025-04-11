import numpy as np

A = np.array([0, 1, 2, 3])
B = np.array([1, 2, 33, 244])
h = A[1] - A[0]
m = len(A)

def spline_interpolation(x):
    M = np.zeros(m)
    C = np.zeros((m, m))
    M[0] = 0
    M[m] = 0
    for i in range(m-1):
        if (i == 1):
            C[0][0] = 0 
            C[0][1] = 4
            C 

