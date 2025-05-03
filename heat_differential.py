import numpy as np

# Parameters
k = 0.835  # thermal diffusivity
L, Ct = 10, 0.2  # length (m), total time (s)
dx, dt = 2, 0.1  # spatial and time step

m, n = int(L/dx), int(Ct/dt)  # grid points
p = k * dt / dx**2

# Initialize temperature grid
A = np.full((m+1, n+1), 0.0)

# Boundary conditions
A[0, :] = 100
A[m, :] = 50

def heat_conduction_1d(A, p):
    m, n = A.shape[0] - 1, A.shape[1] - 1
    for j in range(n):
        for i in range(1, m):
            A[i, j+1] = A[i, j] + p * (A[i+1, j] - 2*A[i, j] + A[i-1, j])
    return A

result = heat_conduction_1d(A, p)
print(np.round(result, 2))
