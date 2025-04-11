import numpy as np

coefficients = np.array([
    [2, 1, 1],
    [3,  2, 3],
    [1, 4, 9]
], dtype=float)

constants = np.array([10, 18, 16], dtype=float)

'''coefficients = np.array([[4, -1, 0, 0],
              [-1, 4, -1, 0],
              [0, -1, 4, -1],
              [0, 0, -1, 3]], dtype=float)

constants = np.array([15, 10, 10, 10], dtype=float)'''


def gauss_elimination(A,B):
    n = len(B)

    for i in range(n):
        for j in range(i+1,n):
            scale_factor = A[j][i]/A[i][i]
            A[j] = A[j] - scale_factor * A[i]
            B[j] = B[j] - scale_factor * B[i]
    
    return A,B

X,Y = gauss_elimination(coefficients,constants)

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