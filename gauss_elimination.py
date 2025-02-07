import numpy as np

def gauss_elimination(A,B) :

    n = len(A)
    # Forward elimination
    for i in range(n):
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            B[j] -= factor * B[i]
            

    X=np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range (i + 1 ,n ):
            if A[i][i] == 0:
                raise ValueError("Division by zero encountered in back substitution.")
            sum += ((A[i][j])*X[j])

        X[i] = (B[i] - sum)/A[i][i]
            
    return(A,B,X)

coefficients = np.array([
    [4, -1, 1],
    [2,  2, 3],
    [5, -2, 6]
], dtype=float)

constants = np.array([-5, 10, 1], dtype=float)

P,Q,R = gauss_elimination(coefficients,constants)

print( )
print(P)
print( )
print(Q)
print( )
print(R)