import numpy as np

def gauss_jordan(A,B) :
    n= len(A)
    C = np.identity(n)
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
            C[j] =C[j] - ((C[i])*scale_factor_2)
    
    for i in range (n):

        C[i] = C[i]/A[i][i]
        A[i][i] = 1.0

    X = np.dot(C,B)

    return(X)

coefficients = np.array([
    [2, 1, 1],
    [3,  2, 3],
    [1, 4, 9]
], dtype=float)

constants = np.array([10, 18, 16], dtype=float)


R = gauss_jordan(coefficients,constants)

print(R)