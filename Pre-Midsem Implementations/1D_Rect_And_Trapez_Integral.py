import numpy as np

dx = 1e-6 # Modify as per need

def riemann(f:function, a, b): # summation of f(x)*h
    x = a
    I = 0
    while x < b:
        I += f(x)*dx
        x += dx
    return I
# summation of (f(x)+f(x+h))*h/2 = riemann + (f(b)-f(a))*dx/2
def trapezoidal(f:function, a, b): return riemann(f, a, b) + 0.5*dx*(f(b) - f(a))
I1 = np.pi*riemann(np.sinc, 0.0, 1.0/np.pi)
I2 = np.pi*trapezoidal(np.sinc, 0.0, 1.0/np.pi)

print("Rectangular: "+str(I1)+", Trapezoidal: "+str(I2))