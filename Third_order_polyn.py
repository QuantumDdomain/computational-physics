import numpy as np

X = np.array([1 , 4, 6, 5])
Y = np.array([0 , 1.3863, 1.7918 , 1.6094])

def iii_order_polynomial(X ,Y , x):
    n = len(X)
    b = np.zeros(n)

    temp = 1
    b[0] = Y[0]
    for i in range(1,n):
        add = b[0]
        for j in range(i):
            prd = 1   
            for k in range(j):
                prd *= (X[i] - X[k])
                if (k == j - 1 and (j == i - 1)) :
                    temp = prd
            prd *= b[j] 
            add += prd
        b[i] = (Y[i] - add)/(temp * (X[i] - X[j]))

    add = b[0]
    for i in range(1,n):
        prd = 1
        if i!= 0 :
            for j in range (i):
                prd *= (x - X[j]) 
            prd *= b[i]
        add += prd    
    
    y = add

    return y

x = 2
solution_1 = iii_order_polynomial(X ,Y , x)
print (solution_1)

######################################################

f = lambda i : (Y[i+1] - Y[i])/(X[i+1] - X[i])

def third_order_polynomial(X,Y,x):
    b_0 = f(0)
    b_1 = (f(1) - f(0))/(X[2] - X[0])
    b_2 = (((f(2) - f(1))/(X[3] - X[1])) - ((f(1) - f(0))/(X[2] - X[0])))/(X[3] - X[0])

    y = Y[0] + b_0 *(x - X[0]) + b_1 *(x - X[0])*(x - X[1]) + b_2 * (x - X[0])*(x - X[1])*(x -X[2]) 
    return y

x = 2
solution_2 = third_order_polynomial(X,Y,x)
print (solution_2)