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
                if (k == 0 and (j == i - 1)) :
                    temp = prd
            prd *= b[j] 
        add += prd
        b[i] = (Y[i] - add)/(temp * (X[i] - X[j]))
    #return b

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
solution = iii_order_polynomial(X ,Y , x)
print (solution)