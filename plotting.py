import numpy as np
import math
import matplotlib.pyplot as plt

f2 = lambda x,y : 3*(x**2)*y
x2 = 3

def fourth_order_runge_kutta_method(f ,X ,x_0 ,y_0 ,h ):
    x_i = x_0
    y_i = y_0
    x_values = [x_i]
    y_values = [y_i]
    n = int ((X - x_0)/h)
    for j in range(n):
        k1 = h * f(x_i, y_i)
        k2 = h * f(x_i + h/2, y_i + k1/2)
        k3 = h * f(x_i + h/2, y_i + k2/2)
        k4 = h * f(x_i + h, y_i + k3)
        y_i += ((k1 + 2 * (k2 + k3) + k4)/6)
        x_i += h

        x_values.append(x_i)
        y_values.append(y_i)
    y = y_i
    
    return x_values, y_values ,y

x_vals, y_vals,_ = fourth_order_runge_kutta_method(f2, x2, 1, 1, 0.01)
# Plot the result
plt.plot(x_vals, y_vals, label='RK4 Approximation', color='purple')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of dy/dx = 3(x**2)y using RK4')
plt.grid(True)
plt.legend()
plt.show()
