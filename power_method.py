import numpy as np

matrix = np.array([[6,-2],
    [-2,6]])
initial_V = np. array([[1],[6]])

def transpose(A) :

    m = len(A)
    n = len(A[0])
    B = np.zeros((n,m))

    for i in range (m):
        for j in range (n):
            B[j][i] = A[i][j]

    return B  

def power_method(A ,V):

    V_new = V/np.linalg.norm(V)

    while True :
        V_temp = V_new
        V_new = np.dot(A,V_new)
        V_new = V_new/np.linalg.norm(V_new)

        if (np.linalg.norm(V_new - V_temp) < 1e-6) :
            break
    dominant_eigenvalue = np.matmul(transpose(V_new),np.matmul(A,V_new))/np.matmul(transpose(V_new),V_new)

    return np.linalg.norm(dominant_eigenvalue),V_new

eigenvalue ,eigenvector = power_method(matrix,initial_V)
print (round(eigenvalue,3))
print(eigenvector)