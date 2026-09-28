import numpy as np

# Given endpoints a, b, f(a)*f(b) < 0
err = 1e-4

def findRoot(a,b,f:function) -> float:
    if (f(a)*f(b) > 0):
        print("Can't run algorithm.")
        return np.inf
    elif (f(a)*f(b) == 0):
        return (a if f(a) == 0 else b)
    else:
        low = a
        up = b
        root = np.inf
        e = abs(f(low))
        while e > err:
            mid = 0.5*(low+up)
            e = abs(f(mid))
            if e < err:
                root = mid
                break
            if f(mid)*f(up) < 0: low = mid
            else: up = mid
        return root

root = findRoot(-1, 3, np.cos)
print(root)