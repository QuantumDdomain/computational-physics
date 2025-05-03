import numpy as np
L,W = 2.4 , 3
dx ,dy= 0.6 , 0.6
m, n = int(L/dx), int(W/dy)
A = np.zeros((m+1, n+1))

# Boundary conditions
A[0, :] = 75
A[:, n] = 300
A[m, :] = 100
A[:, 0] = 50

def laplace(A, k, omega):
    m, n = A.shape[0] - 1, A.shape[1] - 1
    for _ in range(k):
        for i in range(1, m):
            for j in range(1, n):
                old = A[i, j]
                A[i, j] = (1 - omega) * old + omega * 0.25 * (A[i+1,j] + A[i-1,j] + A[i,j+1] + A[i,j-1])
    return A

k = 1000
omega = 1.4  # Over-relaxation factor (1 < omega < 2 usually helps)
result = laplace(A, k, omega)
print(np.round(result, 2))
