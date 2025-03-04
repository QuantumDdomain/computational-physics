import math

def fn(x) :
    return 2 + math.log(x)  # X = 2+log(X)

def fixed_point(fn, a, tol=1e-6) :
    x = a
    while True :
        y=fn(x)

        if (abs(y-x) >= tol ) :
            x=y
        
        else :
            break

    return x

a = 1.0
solution = fixed_point(fn ,a )

print("value is :" ,solution)