import numpy as np

def linear_interpolation (x):

    A = np.array([1 , 4, 9, 16])
    B = np.array([1 , 2, 3, 4])
    n = len(A)

    for i in range(n) :
        if(A[i] <= x <= A[i+1]) :
            C = (x - A[i])*((B[i+1] - B[i])/(A[i+1] - A[i])) + B[i]

    return C

x = 2
solution = linear_interpolation(x)
print(solution)

