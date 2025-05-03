import numpy as np

A = np.array([0, 1, 2, 3])
B = np.array([1, 2, 33, 244])
h = A[1] - A[0]  # Assumes equally spaced A values

def compute_second_derivatives(A, B, h):
    n = len(A) - 1  # Last index
    M = np.zeros(len(A))
    # Natural spline boundary conditions: second derivatives at endpoints are zero
    M[0] = 0
    M[n] = 0
    
    # Build coefficient matrix C for interior points
    C = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        if i == 0 or i == n:
            C[i, i] = 1
        else:
            C[i, i - 1] = (A[i]-A[i-1])/6
            C[i, i] = (A[i+1]-A[i-1])/3
            C[i, i + 1] = (A[i+1]-A[i])/6

    # Build right-hand side vector D using interior points
    D = np.zeros(n - 1)
    for i in range(1, n):
        D[i - 1] = (B[i+1] - B[i])/(A[i+1] - A[i]) - (B[i] - B[i-1])/(A[i] - A[i-1])    
    # Solve for interior second derivatives
    M[1:n] = np.linalg.solve(C[1:n, 1:n], D)
    return M

def get_piecewise_spline_functions(A, B):
    """
    Computes the piecewise cubic spline coefficients for each interval [A[i], A[i+1]].
    
    Returns:
        A list of dictionaries, where each dictionary contains:
            - 'interval': tuple representing the domain (A[i], A[i+1])
            - 'a', 'b', 'c', 'd': coefficients of the cubic polynomial
              S_i(x) = a + b*(x-A[i]) + c*(x-A[i])**2 + d*(x-A[i])**3
    """
    h = A[1] - A[0]  # Assuming equally spaced nodes
    M = compute_second_derivatives(A, B, h)
    piecewise_functions = []
    
    for i in range(len(A) - 1):
        a_i = B[i]
        b_i = (B[i+1] - B[i]) / h - (2 * M[i] + M[i+1]) * h / 6
        c_i = M[i] / 2
        d_i = (M[i+1] - M[i]) / (6 * h)
        
        piecewise_functions.append({
            "interval": (A[i], A[i+1]),
            "a": a_i,
            "b": b_i,
            "c": c_i,
            "d": d_i
        })
    
    return piecewise_functions

# Get the piecewise spline function definitions
piecewise_splines = get_piecewise_spline_functions(A, B)

# Print the spline function for each interval
for spline in piecewise_splines:
    interval = spline["interval"]
    print(f"Interval {interval}:")
    print(f"  S(x) = {spline['a']} + {spline['b']}*(x - {interval[0]}) + {spline['c']}*(x - {interval[0]})^2 + {spline['d']}*(x - {interval[0]})^3")
    print()
