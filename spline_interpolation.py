import numpy as np
import matplotlib.pyplot as plt

A = np.array([0, 1, 2, 3])
B = np.array([1, 2, 33, 244])
h = A[1] - A[0]

def compute_second_derivatives(A, B, h):
    n = len(A) - 1 
    M = np.zeros(len(A))
    # Natural spline boundary conditions: second derivatives at endpoints are zero
    M[0] = 0
    M[n] = 0
    
    C = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        if i == 0:
            C[i, i] = 1
        elif i == n:
            C[i, i] = 1
        else:
            C[i, i - 1] = 1
            C[i, i] = 4
            C[i, i + 1] = 1

    D = np.zeros(n - 1)
    for i in range(1, n):
        D[i - 1] = 6 * (B[i + 1] - 2 * B[i] + B[i - 1]) / (h ** 2)
    
    # Solve the linear system for the interior second derivatives M[1] to M[n-1]
    M[1:n] = np.linalg.solve(C[1:n, 1:n], D)
    return M

M = compute_second_derivatives(A, B, h)

def spline(x):
    # Determine the interval index for the given x
    i = np.searchsorted(A, x) 
    # Clamp i so it stays within valid bounds (0 to len(A)-2)
    i = max(min(i, len(A) - 1), 0)

    a_1 = ((((A[i] - x)**3) * (M[i-1]) + ((x - A[i-1])**3)*M[i])/(6*h))
    b_1 = (((A[i] - x)*(B[i-1]-((h**2)*M[i-1])/6))/h)
    c_1 = (((x - A[i-1]) * (B[i] - ((h**2)*M[i])/6))/h)

    return   a_1 + b_1 + c_1

print("Second Derivatives M:")
print(M)

x_val = 1.5
print(f"Spline interpolation at x = {x_val}: {spline(x_val)}")
# Generate dense x-values for plotting the spline and the real function
x_dense = np.linspace(A[0], A[-1], 400)
spline_values = np.array([spline(x) for x in x_dense])
real_function_values = 1 + (x_dense * (5*x_dense - 6)**2)

# Plot the real function and the spline interpolation
plt.figure(figsize=(8, 6))
plt.plot(x_dense, real_function_values, label='Real function 1 + x(5x - 6)^2', color='blue')
plt.plot(x_dense, spline_values, label='Spline interpolation', linestyle='--', color='red')
plt.scatter(A, B, color='black', zorder=5, label='Data points (nodes)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Spline Interpolation vs Real Function f(x) = 1 + x(5x - 6)^2')
plt.legend()
plt.grid(True)
plt.show()