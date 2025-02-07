import math

sum=1
power=1
factorial=1

x=0.5

for i in range(1,20):
    power *= float(x)
    factorial *= i
    sum += power/factorial

print('sum =',sum)
exact_value = math.exp(float(x))
print('Exact value of exp(x) is :',exact_value)