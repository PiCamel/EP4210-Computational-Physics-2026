import numpy as np

N = int(1e7)

xarr = np.random.rand(N)
yarr = np.random.rand(N)
xarr = 2*xarr-np.array([1.0]*N)
yarr = 2*yarr-np.array([1.0]*N)

count = 0
for i in range(N):
    if xarr[i]**2 + yarr[i]**2 <= 1: count+=1
area = 4.0*count/(N)
print(area) # pi