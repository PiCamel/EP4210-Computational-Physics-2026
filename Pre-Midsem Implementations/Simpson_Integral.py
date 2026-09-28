import numpy as np
N = int(1e6)
a = 0.0
b = 1
dx = (b-a)/N
def simpson(f:function, a, b):
    #1/3 times endpoints + 4/3 times odd indices + 2/3 times even indices
    xarr = np.linspace(a,b,N+1)
    f_arr = np.vectorize(f)
    yarr = f_arr(xarr)
    I = (yarr[0]+yarr[N]+4*yarr[N-1])*dx/3.0
    for i in range(1,N-2,2):
        I += (4*yarr[i]+2*yarr[i+1])*dx/3.0
    return I

integral = simpson(np.exp, a, b)
print(integral+1) # neat, weird way of getting e
