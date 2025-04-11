import numpy as np

coefficients = np.array([
    [2, 1, 1],
    [3,  2, 3],
    [1, 4, 9]
], dtype=float)

constants = np.array([10, 18, 16], dtype=float)

def gauss_jordan(A,B):
    n = len(B)
    
    #RREF
    for i in range(n):
        for j in range(i+1,n):
            scale_factor_1 = A[j][i]/A[i][i]
            A[j] = A[j] - scale_factor_1 * A[i]
            B[j] = B[j] - scale_factor_1 * B[i]
    for i in range(n):
        for j in range(i+1,n):
            scale_factor_2 = A[j][j]/A[i][j]
            A[i] = A[i] * scale_factor_2 - A[j]
            B[i] = B[i] * scale_factor_2 - B[j]


    return A,B

X,Y = gauss_jordan(coefficients,constants)

def back_substitution(A,B):
    n = len(B)
    C = np.zeros(n)
    for i in range(n-1 , -1 ,-1):
        sum = 0
        for j in range(1,n-i):
            sum += A[i][i+j] * C[i+j]
        C[i] = (B[i] - sum)/A[i][i] 
    
    return C


solution = back_substitution(X,Y)
print(solution)