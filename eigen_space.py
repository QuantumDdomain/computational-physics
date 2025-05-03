import numpy as np
import math

matrix = ([
    [0,1,0],
    [0,0,1],
    [2,-5,4]
])

def trace(A):
     
    n = len(A)
    sum = 0
    for i in range(n):
        sum += A[i][i]

    return sum    

def faddeev_leverrier(A):
    A = np.array(A)
    n = A.shape[0]  
    C_low = np.identity(n)
    C_mid = A
    scalar = np.zeros(n + 1)
    scalar[0] = 1  

    for i in range(1, n + 1):
        scalar[i] = -trace(C_mid) / i  
        C_high = np.dot(A, C_mid) + scalar[i] * np.dot(A ,C_low)  
        C_mid = C_high

    return scalar

def polynomial_solve(scalar):
    roots = np.roots(scalar)

    return roots

def eigenvector (A,eigenvalues):
    n = len(eigenvalues)
    p = len(A)

    for i in range(n):
        print (round(abs(eigenvalues[i]), 3))
        shifted_A = A - round(abs(eigenvalues[i]), 3) * np.identity(p)
        #print(shifted_A)
        eigenvector = gauss_elimination(shifted_A)
        matrix_zeta = np.array(eigenvector)
        print(matrix_zeta)
    

def gauss_elimination(A) :

    n = len(A)
    # Forward elimination
    for i in range(n):
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            

    X=np.zeros(n)
    for i in range(n - 1, -1, -1):
        if all (element <= 1e-6 for element in A[i]):
            X[i] = 1

        else:
            sum_values = 0
            for j in range(i + 1, n):
                sum_values += A[i][j] * X[j]
            X[i] = (0 - sum_values) / A[i][i]
        
            
    return(X)

scalar = faddeev_leverrier(matrix)
eigenvalue = polynomial_solve(scalar)
eigenvector(matrix, eigenvalue)
