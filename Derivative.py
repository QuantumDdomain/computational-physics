import math

f1 = lambda x: math.sin(x)
f2 = lambda x: math.cos(x)
f3 = lambda x: math.tan(x)

def point_3_dy(fn ,x1 ,h1 ) :  
    return (fn(x1 + h1) - fn(x1-h1))/(2*h1)

def point_5_dy(fn ,x1 ,h1 ) :  
    return (-fn(x1 + 2*h1) + 8*fn(x1 + h1) - 8*fn(x1-h1) + fn(x1 - 2*h1))/(12*h1)    

def d2y(fn ,x2 ,h2 ) :
    return (fn(x2 + h2) - 2*fn(x2) + fn(x2 - h2))/(h**2)

x = 0.5
h = 0.01
print()

a = point_3_dy(f1 ,x ,h )
b = point_5_dy(f1 ,x ,h )
c = d2y(f1 ,x ,h )

print(a)
print(b)
print(c)