''' E(yx) = a*E(x**2) + b*E(x**0.5)'''
''' E(yx**(-0.5)) = a*E(x**(0.5)) + b*E(x**(-1))'''

import numpy as np

def curve_fitting():
    A = np.array([0.2 ,0.3 ,0.5 ,1.0 ,2.0])
    B = np.array([16 ,14 ,11 ,6 ,3])
    n = len(A)

    X_1 = 0
    for i in range(n):
        X_1 += (A[i])**2
    
    X_2 = 0
    for i in range(n):
        X_2 += (A[i])**(0.5)

    Y_1 = 0
    for i in range(n):
        Y_1 += (A[i])**(0.5)    

    Y_2 = 0
    for i in range(n):
        Y_2 += (A[i])**(-1)

    C_1 = 0
    for i in range(n):
        C_1 += A[i] * B[i] 

    C_2 = 0
    for i in range(n):
        C_2 += B[i] * (A[i])**(-0.5) 

    tol = 1e-6    

    x = 1
    y = 7
    while True :
        a = (C_1 - (Y_1)*y)/X_1
        b = (C_2 - (X_1)*x)/Y_2

        if abs(a - x) < tol and abs(b - y) < tol:
            break
    
        x, y = a, b   
    return x,y

a,b = curve_fitting()
print(a,b)