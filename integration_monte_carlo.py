import random

f = lambda x , y:  y**2  - 4*x

def monte_carlo_integration(f, a, b, c, d, n):

    count_inside = 0
    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        if f(x, y) <= 0:
            count_inside += 1

    area = (b - a) * (d - c)
    return area * (count_inside / n)

Area = monte_carlo_integration(f, 0, 4, -4, 4, 1000000) 
print(Area)