import numpy as np

def jacobi_multivariable(x,y,z,tol = 1e-6):

    while True :
        a = (3 + y - z)/4
        b = (1 + z - 2*x)/5
        c = (2 + x - y)/4

        if abs(a - x) < tol and abs(b - y) < tol and abs(c - z) < tol:
            break
        
        x, y, z = a, b, c 

    return x,y,z    

P,Q,R = jacobi_multivariable(x = 0,y = 0,z = 0)

print( )
print(P)
print( )
print(Q)
print( )
print(R)
