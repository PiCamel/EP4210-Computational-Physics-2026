import numpy as np

N = int(1e4)
ax = -1.0
bx = 1.0
dx = (bx-ax)/N

def f(x): 
    return np.exp(-(x**2))

def simpson(f:function, a:float, b:float, N:int):
    #1/3 times endpoints + 4/3 times odd indices + 2/3 times even indices
    xarr = np.linspace(a,b,N+1)
    f_arr = np.vectorize(f)
    yarr = f_arr(xarr)
    I = (yarr[0]+yarr[N]+4*yarr[N-1])*dx/3.0
    for i in range(1,N-2,2):
        I += (4*yarr[i]+2*yarr[i+1])*dx/3.0
    return I

# Mass of unit radius disc with sigma = exp(-x^2 - y^2)
def fx(x):
    ay = -np.sqrt(1-x**2)
    by = np.sqrt(1-x**2)
    n = int((by-ay)/dx)
    n += n%2 #roughly making the thing equally grid spaced
    Ix = simpson(f, ay, by, n)
    return Ix

def fint(x):
    return f(x)*fx(x)

integral = simpson(fint, ax, bx, N)
print(integral) # IT WORKS!!