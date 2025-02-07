import numpy as np

def inverse_matrix(A) :

    n= len(A)
    B = np.identity(n)
    
    for j in range (n) :
        for i in range(j+1,n):
                scale_factor = A[j][j]/A[i][j]
                A[i] = (A[i])*scale_factor - A[j]
                B[i] = (B[i])*scale_factor - B[j]

    # RREF
  
    for j in range (n):
        for i in range (j+1,n):
            scale_factor_2 = A[j][i]/A[i][i]
            A[j] =A[j] - ((A[i])*scale_factor_2) 
            B[j] =B[j] - ((B[i])*scale_factor_2)
    
    for i in range (n):

        B[i] = B[i]/A[i][i]
        A[i][i] = 1.0

    return B   




A = np.array([
    [2, 1, 3],
    [1,  2, 1],
    [3, 1, 2]
], dtype=float)

solution = inverse_matrix(A)

print(solution)