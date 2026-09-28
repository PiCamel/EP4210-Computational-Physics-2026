import numpy as np

e = 1e-6

def df_dx(f:function, x):
    h = 1e-6
    return (f(x+h)-f(x-h)/(2.0*h))

def NRroot(x, f:function):
    x_i = float(x)
    while abs(f(x_i)>e): x_i = x_i - f(x_i)/df_dx(f, x_i)
    return x_i

root = NRroot(1, np.cos)
print(root)