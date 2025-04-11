import numpy as np

def lagrange_interpolation (x):

    A = np.array([1.2 , 1.3, 1.4, 1.5])
    B = np.array([1.063 , 1.091, 1.119, 1.145])
    n = len(A)
    L = np.zeros(n)

    y = 0
    for i in range(n):
        l = 1
        for j in range(n):
            if (i != j):
                l *= (x-A[j]) / (A[i] - A[j])   
        L[i] = l
        y += B[i] * L[i]

    return y

x = 1.35
solution_1 = lagrange_interpolation(x)
print(solution_1)

#####################################################

A = np.array([1 , 4, 6])
B = np.array([0 , 1.3863, 1.7918])

def lagrangian_polynomial(A,B,x,n):
    
    L = np.zeros(n+1)
    for i in range(n+1):
        prd = 1 
        for j in range(n+1):
            if(i != j):
                prd *= (x - A[j])/(A[i] - A[j])
        L[i] = prd
    
    sum = 0
    for i in range(n+1) :
        sum += B[i] * L[i]
    y = sum
    
    return y

x = 2
solution_2 = lagrangian_polynomial(A,B,x,2)
print(solution_2)