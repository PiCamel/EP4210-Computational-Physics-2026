import numpy as np

N = int(1e8)

vecs = np.random.rand(10,N)
vecs = 2*vecs-np.ones((10,N))

count = 0
for i in range(N):
    sum = 0
    for j in range(10): sum+=vecs[j][i]**2
    if sum <= 1: count += 1
volume = 2.0**10*count/(N)
print(volume) # pi^5/120 = 2.55016403988
# WORKS