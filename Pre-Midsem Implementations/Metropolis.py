import numpy as np
import matplotlib.pyplot as plt

N = int(1e5)
x0 = 0.5

def metropolis(x0:float, f:function):
    x_cur = x0
    x_samples = np.zeros(N)
    for i in range(N):
        dx = np.random.normal(0,0.1)
        x_prop = x_cur + dx
        a = 1.0
        if f(x_cur)!= 0: a = min(1, f(x_prop)/f(x_cur))
        r = np.random.uniform(0,1)
        if r < a:
            x_cur += dx
            x_samples[i] = x_cur
    return x_samples

a = metropolis(x0, np.sin)
plt.hist(a, 100)
plt.show()
