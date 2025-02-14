import numpy as np

def lagrange_interpolation (x , n):

    A = np.array([1 , 4, 6])
    B = np.array([0 , 1.3863, 1.7918])
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

x = 2
solution_1 = lagrange_interpolation(x , 2)
solution_2 = lagrange_interpolation(x , 3)
print(solution_1)
print(solution_2)