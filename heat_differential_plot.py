import numpy as np
import matplotlib.pyplot as plt

k = 1.4129e-5
L, Ct = 0.05, 8          
dx, dt = 0.01, 2       

m, n = int(L/dx), int(Ct/dt)  
p = k * dt / dx**2

# Initialize temperature grid
A = np.full((m+1, n+1), 20.0)

# Boundary conditions
A[0, :] = 100
A[m, :] = 25

def heat_conduction_1d(A, p):
    m, n = A.shape[0] - 1, A.shape[1] - 1
    for j in range(n):
        for i in range(1, m):
            A[i, j+1] = A[i, j] + p * (A[i+1, j] - 2*A[i, j] + A[i-1, j])
    return A


result = heat_conduction_1d(A, p)

time_values = [0, Ct/2, Ct]  # e.g., at 0s, midpoint, and end
indices = [int(t / dt) for t in time_values]  # Convert times to step indices

# Plot temperature distribution at the chosen times
x = np.linspace(0, L, m+1)

plt.figure(figsize=(10, 6)) # width, height in inches
for j in indices:
    plt.plot(x, result[:, j], label=f"t = {j*dt:.1f} s")

plt.xlabel("Position along the rod (m)")
plt.ylabel("Temperature (°C)")
plt.title("1D Heat Conduction Over Time")
plt.legend()
plt.grid(True)
plt.show()
