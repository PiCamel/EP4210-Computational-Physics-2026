import numpy as np

N = int(1e5)
a = 0
b = 3*np.pi/2.0
xarr = 3*np.pi/2.0 * np.random.rand(N)
yarr = 2*np.random.rand(N)-np.ones(N)

def counter(f:function, x, y):
    if 0 <= y <= f(x): return +1
    elif 0 > y > f(x): return -1
    else: return 0

counts = np.vectorize(counter)
carr = counts(np.cos, xarr, yarr)
total = sum(carr)
integral = total*(3.0*np.pi)/N
print(integral) # -1, WORKS