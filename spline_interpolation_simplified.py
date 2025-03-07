import numpy as np

A = np.array([0, 1, 2, 3])
B = np.array([1, 2, 33, 244])
h = A[1] - A[0]
m = len(A)

def compute_second_derivatives(A, B, h):
    n = len(A) - 1  
    M = np.zeros(len(A))

    C = np.zeros((m, m))
    C[0, 0] = 1  
    C[n, n] = 1  

    for i in range(1, n):
        C[i, i - 1] = 1
        C[i, i] = 4
        C[i, i + 1] = 1

    D = np.zeros(m)
    for i in range(1, n):
        D[i] = 6 * (B[i + 1] - 2 * B[i] + B[i - 1]) / (h ** 2)
    
    return C, D

def gauss_jordan(A, B):
    n = len(B)
    
    for i in range(n):
        factor = A[i, i]
        A[i] /= factor
        B[i] /= factor

        for j in range(n):
            if i != j:
                factor = A[j, i]
                A[j] -= factor * A[i]
                B[j] -= factor * B[i]

    return B    

coefficients, constants = compute_second_derivatives(A, B, h)
M = gauss_jordan(coefficients, constants)

def spline(x):
    if x < A[0] or x > A[-1]:
        raise ValueError("x is outside the interpolation range.")

    i = 0
    for j in range(m - 1):
        if A[j] <= x and x < A[j + 1]:  
            i = j
            break
    
    # If x is exactly the last element, use the last interval
    if x == A[-1]:
        i = m - 2  

    a_1 = ((((A[i + 1] - x) ** 3) * M[i] + ((x - A[i]) ** 3) * M[i + 1]) / (6 * h))
    b_1 = (((A[i + 1] - x) * (B[i] - ((h ** 2) * M[i]) / 6)) / h)
    c_1 = (((x - A[i]) * (B[i + 1] - ((h ** 2) * M[i + 1]) / 6)) / h)

    return a_1 + b_1 + c_1

print("Second Derivatives M:")
print(M)

x_val = 1.5
print(f"Spline interpolation at x = {x_val}: {spline(x_val)}")
