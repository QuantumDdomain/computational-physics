import numpy as np

def gauss_jordan(A,B) :

    n= len(A)
    for j in range (n) :
        for i in range(j+1,n):
            if(i>j):
                scale_factor_1 = A[j][j]/A[i][j]
                A[i] = (A[i])*scale_factor_1 - A[j]
                B[i] = (B[i])*scale_factor_1 - B[j]
            
            if(i <= j) :
                break

# RREF
  
    for j in range (n):
        for i in range (j+1,n):
            scale_factor_2 = A[j][i]/A[i][i]
            A[j] =A[j] - ((A[i])*scale_factor_2) 
            B[j] =B[j] - ((B[i])*scale_factor_2)
    
    for i in range (n):

        B[i] = B[i]/A[i][i]
        A[i][i] = 1.0

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
    [2, 1, 1],
    [3,  2, 3],
    [1, 4, 9]
], dtype=float)

constants = np.array([10, 18, 16], dtype=float)

P,Q,R = gauss_jordan(coefficients,constants)

print( )
print(P)
print( )
print(Q)
print( )
print(R)