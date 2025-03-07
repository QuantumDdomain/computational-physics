import math
import numpy as np

A = np.array([0,5,10,15,20])
B = np.array([0,3,9,18,30])

def point_2_dy(A ,B ,x) :
    i = np.searchsorted(A, x)
    return ((B[i+1] - B[i])/(A[i+1] - A[i]))

def point_3_dy(A ,B ,x) :
    i = np.searchsorted(A, x)
    return ((B[i+1] - B[i-1])/(A[i+1] - A[i-1]))

def point_5_dy(A ,B ,x) :  
    i = np.searchsorted(A, x)
    return ((-B[i + 2] + 8*B[i + 1] - 8*B[i-1] + [i - 2])/(3*(A[i+2]-A[i-2])))    

x = 10
print()

a = point_2_dy(A ,B ,x )
b = point_3_dy(A ,B ,x )
c = point_5_dy(A ,B ,x )

print(a)
print(b)
print(c)